from agent.state import AgentState
from agent.tools import list_files_tool

def hello_node(state: AgentState):
    """
    A simple node that returns a greeting message.
    """
    print("Hello node executed")

    state["answer"] = (
        f"Processed question: {state['question']}"
    )

    return state


def router_node(state: AgentState):
    """
    A router node that decides which tool to use based on the question.
    """
    question = state["question"].lower()

    if "list files" in question:
        state["selected_tool"] = "list_files_tool"
    else:
        state["selected_tool"] = "none"
    
    return state

def tool_node(state: AgentState):
    
    if state["selected_tool"] == "list_files_tool":
        result = list_files_tool()
        state["tool_result"] = result
        state["answer"] = result

        state["answer"] = (
            f"Files found: {', '.join(result)}"
        )
    else:
        state["answer"] = "No tool required."

    return state