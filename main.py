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
    from pydantic import ValidationError

    print("--- 1. Successful Creation ---")
    input_data = {"id": 1, "name": "Alice", "email": "alex@example.com"}
    created = create_user(**input_data)
    print(f"Created User: {created}")

    print("---2. Input Validation Failure Triggered ----")
    try:
        bad_input_data = {"id": 43, "name": "B", "email": "not-an-email"}
        bad_input_failure = create_user(**bad_input_data)
    except ValidationError as e:
        print(f"Validation Error: {e}")
        print(e.json(indent=2))

    print("--- 3. Successful Update ---")
    update_data = {"name": "Bob Parker", "email": "bob_parker@example.com"}
    updated = update_user(1, **update_data)
    print(f"Updated User: {updated}")

    main()
