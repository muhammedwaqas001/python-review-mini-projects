from contextlib import contextmanager

@contextmanager
def database_session():
    print("Database connection opened.")
    try:
        yield
    finally:
        print("Database connection closed.")

with database_session() as connection:
    print("Fetching AI training data.")