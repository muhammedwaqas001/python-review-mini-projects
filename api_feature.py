def get_user(name):
    return f"User {name} API is working"


print(get_user("Waqas"))
def get_user(name: str) -> str:
    if not name.strip():
        raise ValueError("Username cannot be empty.")

    return f"User {name} API is working"


print(get_user("Waqas"))

try:
    print(get_user(""))
except ValueError as error:
    print(error)
