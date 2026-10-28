def calculate_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)
print(calculate_average([80, 90, 100]))


def get_score(score: int | None) -> str:
    if score == None:
        return "Score not available."
    return f"Score: {score}"


print(get_score(85))
print(get_score(None))