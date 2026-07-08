from state import SupportState
from llm import llm


def supervisor_agent(state: SupportState):

    if state["approval_required"] and not state["approval_status"]:
        prompt = f"""
You are a customer support supervisor at ABC Technologies.

The customer's request requires human approval.

Rewrite the following response in a professional and polite manner.

Mention that the request has been forwarded to a human representative.

IMPORTANT:
Return ONLY the final customer response.
Do NOT explain your reasoning.
Do NOT use markdown.
Do NOT add headings.

Customer Query:
{state["query"]}

Draft Response:
{state["response"]}
"""
    else:
        prompt = f"""
You are a customer support supervisor at ABC Technologies.

Rewrite the following response so that it is:

- Professional
- Polite
- Grammatically correct
- Clear and concise

IMPORTANT:
Return ONLY the response that will be sent to the customer.
Do NOT explain anything.
Do NOT say "Here is the improved response".
Do NOT use markdown.
Do NOT use bullet points.
Do NOT add headings.

Customer Query:
{state["query"]}

Draft Response:
{state["response"]}
"""

    response = llm.invoke(prompt)

    state["response"] = response.content.strip()

    return state