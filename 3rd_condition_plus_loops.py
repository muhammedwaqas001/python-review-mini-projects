scores = [45, 82, 67, 91, 38, 76, 88]

for score in scores:
    if score >= 80:
        print("Excellent")
    elif score >= 60 and score <= 79:
        print("Good")
    elif score >= 40 and score <= 59:
        print("Needs Improvement")
    else:
        print("Failed")        