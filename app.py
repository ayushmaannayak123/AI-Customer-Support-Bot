# app.py

from memory import initialize_database
from graph import graph


def create_initial_state(customer_name, query):
    """
    Creates the initial state required by the LangGraph workflow.
    """

    return {
        "customer_name": customer_name,
        "query": query,
        "department": "",
        "retrieved_context": "",
        "response": "",
        "approval_required": False,
        "approval_status": False,
        "conversation_history": []
    }


def main():

    print("=" * 60)
    print("ABC Technologies - AI Customer Support")
    print("=" * 60)

    initialize_database()

    while True:

        print()

        customer_name = input("Customer Name: ").strip()

        query = input("Customer Query: ").strip()

        state = create_initial_state(
            customer_name,
            query
        )

        final_state = graph.invoke(state)

        print("\n" + "=" * 60)

        print("Department:")
        print(final_state["department"])

        print("\nRetrieved Context:")
        print(final_state["retrieved_context"])

        print("\nApproval Required:")
        print(final_state["approval_required"])

        print("\nApproval Status:")
        print(final_state["approval_status"])

        print("\nFinal Response:")
        print(final_state["response"])

        print("=" * 60)

        again = input("\nAnother query? (yes/no): ")

        if again.lower() != "yes":
            break


if __name__ == "__main__":
    main()