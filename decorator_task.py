def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print("Starting process...")
        func(*args, **kwargs)
        print("Process completed.")
    return wrapper

@start_end_decorator
def run_ai_model(model_name, version):
    print(f"Running {model_name}, Version {version}")

run_ai_model("GPT", version="2.0")            