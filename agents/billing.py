from state import SupportState
from rag import retrieve_context
from llm import generate_response


HIGH_RISK = [

    "refund",

    "cancel",

    "cancellation",

    "account closure",

    "close account",

    "compensation",

    "management"

]


def billing_agent(state: SupportState):

    context = retrieve_context(
        state["query"],
        "Billing"
    )

    prompt = f"""
You are a Billing Support Executive.

Customer Question:
{state["query"]}

Knowledge Base:
{context}

Rules:
- Be polite.
- Never approve refunds.
- Never approve cancellations.
- Explain the policy.
"""

    query = state["query"].lower()

    state["approval_required"] = any(
        word in query
        for word in HIGH_RISK
    )

    state["retrieved_context"] = context
    state["response"] = generate_response(prompt)

    return state