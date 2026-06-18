from recommendation.attraction_engine import calculate_score


def rank_attractions(attractions):

    ranked = []

    for attraction in attractions:

        score = calculate_score(
            attraction.category,
            attraction.rating
        )

        ranked.append({
            "name": attraction.name,
            "score": score
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked