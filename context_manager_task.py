class Modelsession:
    def __enter__(self):
        print("Model session stsrted.")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Model session closed.")
    def run(self):
        print("AI model is procesing data.")

with Modelsession() as session:
    session.run()