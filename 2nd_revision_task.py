model_score = 85
passing_score = 70
bonus = 5

final_score = model_score + bonus
print(final_score)
if final_score >= passing_score:
    print("Final score is greater than or equal to passing score")
else:
    print("Final score is smallar than passing score")

if model_score == 85:
    print("Model score is equal to 85.")
if model_score < passing_score:
    print("Model score is smaller.")
elif model_score > passing_score:
    print("Model score is larger.")
else:
    print("Model score is equal to passing score.")   

half_score = model_score/2
print(half_score)
if final_score >= passing_score and model_score == 85:
    print("Final score meets the passing score AND model score is 85.")
if model_score < passing_score or bonus > 0:
    print("Model score is below passing score OR bonus is greater than 0.")
if not (model_score < passing_score):
    print("Model score is not below the passing score.")        