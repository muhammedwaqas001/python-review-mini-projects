scores = [85, 92, 67, 95, 78, 88]

print("Sorted scores: ", sorted(scores))
print("Highest score: ", max(scores))
print("Lowest scores: ", min(scores))
print("Total scores: ", sum(scores))
print("Any score >= 90:", any(score >= 90 for score in scores))
print("All scores >= 60: ", all(score >= 60 for score in scores))