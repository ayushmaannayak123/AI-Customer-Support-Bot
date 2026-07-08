# memory.py

import sqlite3


DATABASE = "database/memory.db"


def initialize_database():
    """
    Creates the SQLite database and table if they do not already exist.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS conversations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            customer_name TEXT,

            query TEXT,

            response TEXT

        )
        """
    )

    connection.commit()

    connection.close()


def save_conversation(customer_name, query, response):
    """
    Stores a conversation inside SQLite.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO conversations
        (customer_name, query, response)

        VALUES (?, ?, ?)
        """,
        (customer_name, query, response),
    )

    connection.commit()

    connection.close()


def load_previous_issue(customer_name):
    """
    Retrieves the most recent issue raised by the customer.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT query

        FROM conversations

        WHERE customer_name=?

        ORDER BY id DESC

        LIMIT 1
        """,
        (customer_name,),
    )

    result = cursor.fetchone()

    connection.close()

    if result:

        return result[0]

    return "No previous issue found."
def memory_agent(state):
    """
    Retrieves the customer's previous issue
    from SQLite memory.
    """

    previous_issue = load_previous_issue(
        state["customer_name"]
    )

    state["response"] = (
        f"Your previous support issue was:\n\n{previous_issue}"
    )

    return state