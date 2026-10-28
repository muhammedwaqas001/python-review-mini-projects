scores = [90, 75, 45, 88, -1, 95]

index = 0

while index < len(scores):
    score = scores[index]

    if score == -1:
        print("Invalid score found. Stopping...")
        break
    if score < 50:
        index += 1
        continue
    print(f"Processing score: {score}")

    index += 1    