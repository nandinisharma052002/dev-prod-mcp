from typing import TypedDict
from langgraph.graph.message import add_messages

from typing import Annotated


class AgentState(TypedDict):

    messages: Annotated[
        list,
        add_messages
    ]