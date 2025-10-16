# Introduction to LangGraph

---
## Module 1

* In Video 1 we saw about why do we need to learn this course
  * We saw how LLM's work, the flow of control for a LLM
  * We defined an agent as a something that controls the flow defined by a LLM
    * It basically says what to do next
  * There are two main types of agents 
    * Router - In which at a particular point in the control flow it chooses which step to take
    * Fully Autonomous - In this case no steps are given and based on the input it chooses it own set of steps 
    * In Router it happens only after a particular step whereas in Autonomous no steps are predefined ran in the Control flow.
    * Routers are more reliable but LLM has less control where the vice versa for the Autonomous
    * This is where Langgraph comes into play where it maintains the reliability

---

* In Video 2 we saw on how to construct a basic graph and using conditional edges.
  * This is basically the implementation of the Router Agent but we have just not used a LLM model but rather we made it to a random.
  * We also saw that the START and END special nodes that indicate the start and the end of the graph
  * ![img.png](img.png)

---

* In Video 3 we used the LangGraph Studio to plot the graphs.
  * We used some of the predefined stuctures that were given in the course content to use tool call LLMs and show the flow through the graphs
  * We saw that instead of a simple hardcoded inputs we where able to give inputs in realtime to work like a chatbot and it would follow the flow of control
  * ![img_1.png](img_1.png)
  * We see the working of the graph over here with the logs showing the control flow

---

* In Video 4 we saw how chain works using basic examples
  * We saw how chains functions through various different methods
    * We first saw where we created a few **AIMessage** and **HumanMessage** and simulated a conversation like we see in LLM's like ChatGPT or Google Gemini
    * We next used a ChatModel to take an input of Messages and respond to it
    * We also built tools that can be invoked by the LLM model based on the input
    * The workflow graph has also been plotted and presented
    * ![img_2.png](img_2.png)
      *  This is in the case of a tool calling LLM model where if the input asks for a particular tool function that we have specified in the model then it uses else we see that it just uses its own response to respond to the call 
    * We also saw about reducer function that makes sure that our previous responses are being stored and are not getting overridden by the current response. This in actual Chatbots can be used to create a context to how the answer should look like or it tells the model on what we expect

---

