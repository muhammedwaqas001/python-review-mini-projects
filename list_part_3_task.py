models = [
    ["GPT", 95],
    ["Claude", 92],
    ["Gemini", 90]
]
print(models[0][0])
print(models[0][1])
print(models[2][1])
copied_model = models.copy()
copied_model[0][1] = 100
print(models)
print(copied_model)
print(models == copied_model)
print(models is copied_model)