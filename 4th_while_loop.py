scores = [85, 72, 91, -1, 88, 95]

index = 0

while index < len(scores):
    score = scores[index]

    if score == -1:
        print("Invalid score found. Stopping...")
        break

    if score < 80:
        index += 1
        continue

    print(f"Processing score: {score}")

    index += 1