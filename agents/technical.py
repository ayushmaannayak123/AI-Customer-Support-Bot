from state import SupportState
from rag import retrieve_context
from llm import generate_response


def technical_agent(state: SupportState):

    context = retrieve_context(
        state["query"],
        "Technical"
    )

    prompt = f"""
You are a Technical Support Engineer for ABC Technologies.

Customer Question:
{state["query"]}

Knowledge Base:
{context}

Rules:
- Answer only using the provided knowledge.
- Be professional.
- Give clear troubleshooting steps.
- Never invent information.
"""

    state["retrieved_context"] = context
    state["response"] = generate_response(prompt)
    state["approval_required"] = False

    return state