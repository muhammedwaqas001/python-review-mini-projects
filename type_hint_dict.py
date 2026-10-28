from typing import TypedDict
ModelMetrics = dict[str, float]
metrics: ModelMetrics = {
    "accoracy": 0.95,
        "loss": 0.08
}
print(metrics)
# class StudentResult(TypedDict):
#     name: str
#     marks: int
#     passed: bool

# student = {
#     "name": "Waqas",
#     "marks": 95,
#     "passed": True
# }
# print(student)
