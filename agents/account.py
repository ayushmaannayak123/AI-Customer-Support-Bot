from state import SupportState
from rag import retrieve_context
from llm import generate_response


def account_agent(state: SupportState):

    context = retrieve_context(
        state["query"],
        "Account"
    )

    prompt = f"""
You are an Account Support Executive.

Customer Question:
{state["query"]}

Knowledge Base:
{context}

Rules:
- Be professional.
- Answer only using the supplied information.
- If information isn't available, tell the customer politely.
"""

    

    state["retrieved_context"] = context
    state["response"] = generate_response(prompt)
    state["approval_required"] = False

    return state