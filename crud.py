import datetime

# Simple In-Memory Database
db = {}

# logger = logging.getLogger("crud")
# logger.setLevel(logging.INFO)
# if not logger.handlers:
#     _handler = logging.FileHandler("logs.txt")
#     _handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
#     logger.addHandler(_handler)


def create_user(user_id: int, name: str, email: str) -> dict:
    if user_id in db:
        raise ValueError(f"User with ID {user_id} already exists.")
    user_data = {"name": name, "email": email}
    db[user_id] = user_data
    # logger.info(f"User created: id={user_id}, name={name}, email={email}")
    # Return the user data after creation

    # Capture the created user in logs.txt
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a") as log_file:
        log_file.write(
            f"{timestamp} - User created: id={user_id}, name={name}, email={email}\n"
        )
    return user_data
    # return db[user_id]


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
