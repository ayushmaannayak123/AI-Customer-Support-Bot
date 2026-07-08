# graph.py

from langgraph.graph import StateGraph, END

from state import SupportState

from classifier import classify_intent

from agents.sales import sales_agent
from agents.technical import technical_agent
from agents.billing import billing_agent
from agents.account import account_agent

from memory import (
    memory_agent,
    save_conversation
)

from approval import human_approval

from supervisor import supervisor_agent


# ---------------------------------------------------
# Save Conversation Node
# ---------------------------------------------------

def save_node(state: SupportState):
    """
    Saves the customer conversation into SQLite.
    """

    save_conversation(
        state["customer_name"],
        state["query"],
        state["response"]
    )

    return state


# ---------------------------------------------------
# Routing Function
# ---------------------------------------------------

def route_department(state: SupportState):
    """
    Routes the query to the correct department.
    """
    return state["department"]


# ---------------------------------------------------
# Build Graph
# ---------------------------------------------------

builder = StateGraph(SupportState)


# ---------------------------------------------------
# Add Nodes
# ---------------------------------------------------

builder.add_node("Classifier", classify_intent)

builder.add_node("Sales", sales_agent)
builder.add_node("Technical", technical_agent)
builder.add_node("Billing", billing_agent)
builder.add_node("Account", account_agent)

builder.add_node("Memory", memory_agent)

builder.add_node("Approval", human_approval)

builder.add_node("Supervisor", supervisor_agent)

builder.add_node("Save", save_node)


# ---------------------------------------------------
# Entry Point
# ---------------------------------------------------

builder.set_entry_point("Classifier")


# ---------------------------------------------------
# Classifier Routing
# ---------------------------------------------------

builder.add_conditional_edges(
    "Classifier",
    route_department,
    {
        "Sales": "Sales",
        "Technical": "Technical",
        "Billing": "Billing",
        "Account": "Account",
        "Memory": "Memory"
    }
)


# ---------------------------------------------------
# Department -> Approval
# ---------------------------------------------------

builder.add_edge("Sales", "Approval")
builder.add_edge("Technical", "Approval")
builder.add_edge("Billing", "Approval")
builder.add_edge("Account", "Approval")


# ---------------------------------------------------
# Memory -> Supervisor
# ---------------------------------------------------

builder.add_edge("Memory", "Supervisor")


# ---------------------------------------------------
# Approval -> Supervisor
# ---------------------------------------------------

builder.add_edge("Approval", "Supervisor")


# ---------------------------------------------------
# Supervisor -> Save
# ---------------------------------------------------

builder.add_edge("Supervisor", "Save")


# ---------------------------------------------------
# Save -> END
# ---------------------------------------------------

builder.add_edge("Save", END)


# ---------------------------------------------------
# Compile Graph
# ---------------------------------------------------

graph = builder.compile()