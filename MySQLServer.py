import mysql.connector

def create_database(host, user, password, database_name):
    """
    Creates a MySQL database if it doesn't already exist.

    Args:
        host: The hostname of the MySQL server.
        user: The username for the MySQL server.
        password: The password for the MySQL server.
        database_name: The name of the database to create.

    Returns:
        True if the database was created successfully, False otherwise.
    """
    try:
        # Connect to the MySQL server without specifying the database
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()

        # Attempt to create the database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS alx_book_store") 

        # Commit the changes
        conn.commit()

        print(f"Database '{database_name}' created successfully!")
        return True

    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
        return False

    finally:
        # Close the connection
        if conn:
            conn.close()

if __name__ == "__main__":
    # Replace with your actual MySQL server credentials
    host = "localhost"
    user = "your_username"
    password = "your_password"
    database_name = "alx_book_store"

    if create_database(host, user, password, database_name):
        print("Database creation successful.")
    else:
        print("Database creation failed.")