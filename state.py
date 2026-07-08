# state.py

from typing import TypedDict, List


class SupportState(TypedDict):
    """
    Shared state that travels through the LangGraph workflow.
    """

    customer_name: str

    query: str

    department: str

    retrieved_context: str

    response: str

    approval_required: bool

    approval_status: bool

    conversation_history: List[str]