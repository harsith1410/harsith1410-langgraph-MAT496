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