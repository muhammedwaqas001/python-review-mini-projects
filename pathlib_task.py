from pathlib import Path

data_path = Path("data")
print(data_path.exists())
file_path = Path("data/employee.json")
print("Name: ", file_path.name)
print("File name: ", file_path.stem)
print("Extension:", file_path.suffix)
print("Parent folder: ", file_path.parent)
print(file_path.exists())

for item in data_path.iterdir():
    print(item.name)


