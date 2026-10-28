from functools import wraps

def execution_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("AI Model execution started.")
        result = func(*args, **kwargs)
        print("AI Model execution completed.")
        return result
    return wrapper

@execution_logger
def run_model(model_name):
    """Run the selected AI Model""" 
    return f"Running {model_name}"
print(run_model("GPT"))
print(run_model.__name__)
print(run_model.__doc__)           