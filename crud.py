# Simple In-Memory Database
db = {}


def create_user(user_id: int, name: str, email: str) -> dict:
    if user_id in db:
        raise ValueError(f"User with ID {user_id} already exists.")
    db[user_id] = {"name": name, "email": email}
    # Return the user data after creation
    return db[user_id]


def read_user(user_id: int) -> dict:
    if user_id not in db:
        raise KeyError(f"User with ID {user_id} not found.")
    return db[user_id]


def update_user(user_id: int, name: str = None, email: str = None) -> dict:
    if user_id not in db:
        raise KeyError(f"User with ID {user_id} not found.")
    if name:
        db[user_id]["name"] = name
    if email:
        db[user_id]["email"] = email
    return db[user_id]


def delete_user(user_id: int) -> str:
    if user_id not in db:
        raise KeyError(f"User with ID {user_id} not found.")
    del db[user_id]
    return f"User {user_id} deleted successfully."
