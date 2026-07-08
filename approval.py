from state import SupportState


def human_approval(state: SupportState):
    """
    Simulates a human supervisor approval.
    """

    if state["approval_required"]:

        print("\n-----------------------------")
        print("HUMAN APPROVAL REQUIRED")
        print("-----------------------------")

        print(state["response"])

        decision = input(
            "\nApprove response? (yes/no): "
        )

        if decision.lower() == "yes":

            state["approval_status"] = True

        else:

            state["approval_status"] = False

            state["response"] = (
                "Your request has been forwarded "
                "to our human support team."
            )

    else:

        state["approval_status"] = True

    return state