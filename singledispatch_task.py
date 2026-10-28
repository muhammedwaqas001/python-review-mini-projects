from functools import singledispatch

@singledispatch
def analyze_data(data):
    print(f"General data received: {data}")
@analyze_data.register
def _(data: int):
    print(f"Integer received: {data}")
@analyze_data.register
def _(data: float):
    print(f"Float received: {data}")
@analyze_data.register
def _(data: list):
    print(f"Total items in list is {len(data)}")        

analyze_data(25)
analyze_data(["Python", "NumPy", "Pandas"])
analyze_data(3.5)
