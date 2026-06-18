INTEREST_WEIGHTS = {
    "Historical": 70,
    "Museum": 70,
    "Nature": 70,
    "Entertainment": 70,
}


def calculate_score(category, rating):
    interest_score = INTEREST_WEIGHTS.get(category, 0)

    return interest_score + (rating * 20)