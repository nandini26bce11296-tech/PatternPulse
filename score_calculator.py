def study_score(study_hours):
    if study_hours >= 6:
        return 20
    elif study_hours >= 4:
        return 15
    elif study_hours >= 2:
        return 10
    else:
        return 5


def sleep_score(sleep_hours):
    if 7 <= sleep_hours <= 9:
        return 20
    elif 6 <= sleep_hours < 7 or 9 < sleep_hours <= 10:
        return 15
    elif 5 <= sleep_hours < 6 or 10 < sleep_hours <= 11:
        return 10
    else:
        return 5


def task_score(tasks):
    if tasks >= 7:
        return 20
    elif tasks >= 5:
        return 15
    elif tasks >= 3:
        return 10
    else:
        return 5


def activity_score(workout):
    if workout:
        return 20
    return 10


def mood_score(mood):
    return mood * 4


def calculate_score(record):
    total = (
        study_score(record["study"])
        + sleep_score(record["sleep"])
        + task_score(record["tasks"])
        + activity_score(record["workout"])
        + mood_score(record["mood"])
    )

    record["score"] = total
    return total


def calculate_all_scores(records):
    for record in records:
        calculate_score(record)

    return records
