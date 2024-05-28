from db_manager import create_connection, create_table, add_user, authenticate_user

def main():
    database = "users.db"
    conn = create_connection(database)

    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")

    # Example usage:
    add_user(conn, "user1", "password123")
    authenticate_user(conn, "user1", "password123")

if __name__ == '__main__':
    main()
