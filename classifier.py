# classifier.py

from state import SupportState

# Keywords for each support department
INTENT_KEYWORDS = {

    "Sales": [
        "price",
        "pricing",
        "subscription",
        "plan",
        "upgrade",
        "purchase",
        "buy",
        "quote"
    ],

    "Billing": [
        "refund",
        "invoice",
        "payment",
        "billing",
        "charged",
        "receipt",
        "cancel",
        "cancellation",
        "compensation"
    ],

    "Account": [
        "password",
        "login",
        "account",
        "profile",
        "username",
        "activate",
        "deactivate",
        "reset"
    ],

    "Technical": [
        "error",
        "crash",
        "bug",
        "issue",
        "upload",
        "installation",
        "install",
        "configuration",
        "configure",
        "slow",
        "loading",
        "exception"
    ],

    "Memory": [
        "previous issue",
        "previous support issue",
        "last issue",
        "history",
        "earlier issue"
    ]
}


def classify_intent(state: SupportState):
    """
    Classifies the customer's query using keyword scoring.
    """

    query = state["query"].lower()

    scores = {}

    # Calculate score for each department
    for department, keywords in INTENT_KEYWORDS.items():

        score = 0

        for keyword in keywords:

            if keyword in query:
                score += 1

        scores[department] = score

    # Highest score obtained
    highest_score = max(scores.values())

    # If nothing matches, default to Technical
    if highest_score == 0:
        state["department"] = "Technical"
        return state

    # Departments with highest score
    candidates = [
        department
        for department, score in scores.items()
        if score == highest_score
    ]

    # Priority order in case of ties
    priority = [
        "Memory",
        "Billing",
        "Technical",
        "Account",
        "Sales"
    ]

    for department in priority:
        if department in candidates:
            state["department"] = department
            break

    return state