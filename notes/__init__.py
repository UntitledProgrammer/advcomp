import sqlite3
import constants
import logging


def __get_connection() -> sqlite3.Connection:
    """
    Initialises a connection to a SQLite database, where the notes database table is located.
    (The notes database table is automatically created, if it is not present in the SQLite database).
    :return: sqlite3.Connection
    """

    try:
        # Establish a connection to the SQL database.
        connection: sqlite3.Connection = sqlite3.Connection(constants.DATABASE_NAME)

        # Ensure the notes database table is initialised.
        connection.execute(f'CREATE TABLE IF NOT EXISTS {constants.NOTES_TABLE_NAME} (username TEXT NOT NULL, title TEXT, description TEXT, date INTEGER);')

    except sqlite3.Error as error:

        # Log the error for future record.
        logging.error(f"Error establishing a SQL database connection: {error}")

        # Raise the SQLite error.
        raise error


