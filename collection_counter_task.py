from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple

AIModel = namedtuple("AIModel", ["name", "framework", "parameters"])
model = AIModel("GPT", "PyTorch", "7B")
print(model.name)
print(model.framework)
print(model.parameters)
# tasks = deque(["Load Data", "Train Model"])

# tasks.append("Evaluate Model")
# tasks.appendleft("Preprocess Data")
# tasks.popleft()
# print(tasks)
# student_dict = defaultdict(list)
# student_dict["Waqas"].append("Python")
# student_dict["Waqas"].append("NumPy")
# student_dict["Ali"].append("Machine Learning")

# print(student_dict)

# languages = [
#     "Python",
#     "Java",
#     "Python",
#     "JavaScript",
#     "Python",
#     "Java",
#     "C++",
#     "Python",
#     "JavaScript"
# ]

# lang_count = Counter(languages)
# print(lang_count)
# print(lang_count["Python"])
# print(lang_count.most_common(2))