from state import SupportState
from rag import retrieve_context
from llm import generate_response


def sales_agent(state: SupportState):

    context = retrieve_context(
        state["query"],
        "Sales"
    )

    prompt = f"""
You are a professional Sales Support Executive for ABC Technologies.

Answer ONLY using the knowledge provided below.

Customer Question:
{state["query"]}

Knowledge Base:
{context}

Rules:
- Be polite.
- Be professional.
- Don't invent information.
- If the answer isn't available, say so.
"""

    state["retrieved_context"] = context
    state["response"] = generate_response(prompt)
    state["approval_required"] = False

    return state