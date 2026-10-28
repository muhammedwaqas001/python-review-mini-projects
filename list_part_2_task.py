model_scores = [85, 72, 91, 72, 64, 88]
model_scores.remove(64)
print(model_scores.count(72))
print(model_scores.index(91))
model_scores.extend([95, 87])
model_scores.sort(reverse= True)
print(model_scores)