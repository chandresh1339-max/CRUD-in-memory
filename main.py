from crud import create_user, read_user, update_user, delete_user, db


def main():
    print("--- Initializing CRUD Operations ---")

    # 1. Create
    create_user(1, "Alice", "alice@example.com")
    create_user(2, "Bob", "bob@example.com")
    print(f"Database after creation: {db}")

    # 2. Read
    print(f"Reading User 1: {read_user(1)}")

    # 3. Update
    update_user(1, email="alice_new@example.com")
    print(f"Database after updating User 1: {read_user(1)}")

    # 4. Delete
    delete_user(2)
    print(f"Database after deleting User 2: {db}")


if __name__ == "__main__":
    main()
