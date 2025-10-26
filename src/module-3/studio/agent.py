from langchain_openai import ChatOpenAI
from IPython.display import Image, display
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import MessagesState
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

def tyre_strat(Laps_Remaining: int,Laps_Done: int,Safety_Car: bool) -> str:
    """
    This is used to suggest if the Driver needs to Box and Change Tyres
    """
    if Laps_Done > 15  :
        return "Box for New Hards"
    elif (Laps_Remaining<15 and Safety_Car):
        return "Box for a set of Softs and time to Turn and Burn"
    else:
        return "Stay Out!! Stay Out!! Stay Out!!"

def Wet_Condition(is_raining: bool,drivability: bool) -> str:
    """
    If there exists a wet condition use this
    """
    if drivability:
        return "Let's drive in until the brink of toughness"
    elif is_raining and (not drivability):
        return "Box for Wets and Unleash Hell"
    else:
        return "Stay Out!! Stay Out!! Stay Out!!"


tools = [tyre_strat,Wet_Condition]
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

# System message
sys_msg = SystemMessage(content="You are a F1 Race Engineer to driver and help the driver")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Graph
builder = StateGraph(MessagesState)

# Define nodes: these do the work
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Define edges: these determine the control flow
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")

memory = MemorySaver()
graph = builder.compile(interrupt_before=["assistant"])

