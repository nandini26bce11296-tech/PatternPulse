def calculate_range(records, key):
    values = []

    for record in records:
        values.append(record[key])

    if len(values) == 0:
        return 0

    return max(values) - min(values)


def calculate_consistency(records):
    if len(records) == 0:
        return 0

    score_range = calculate_range(records, "score")

    if score_range <= 15:
        return 90
    elif score_range <= 30:
        return 75
    elif score_range <= 45:
        return 60
    else:
        return 40


def consistency_label(consistency_score):
    if consistency_score >= 90:
        return "HIGH"
    elif consistency_score >= 75:
        return "GOOD"
    elif consistency_score >= 60:
        return "MODERATE"
    else:
        return "IRREGULAR"


def analyze_consistency(records, minimum_days=3):
    if len(records) < minimum_days:
        return {
            "score": 0,
            "label": "Insufficient data",
            "message": "At least " + str(minimum_days) + " days are required."
        }

    score = calculate_consistency(records)

    return {
        "score": score,
        "label": consistency_label(score),
        "message": "Consistency is based on the spread of daily PatternPulse scores."
    }
