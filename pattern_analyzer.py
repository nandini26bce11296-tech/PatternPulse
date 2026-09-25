def average(records, key):
    if len(records) == 0:
        return 0

    total = 0
    for record in records:
        total += record[key]

    return total / len(records)


def find_highest_score_day(records):
    return max(records, key=lambda record: record["score"])


def find_lowest_score_day(records):
    return min(records, key=lambda record: record["score"])


def trend(records, key):
    if len(records) < 2:
        return "Insufficient data"

    increases = 0
    decreases = 0

    for i in range(1, len(records)):
        if records[i][key] > records[i - 1][key]:
            increases += 1
        elif records[i][key] < records[i - 1][key]:
            decreases += 1

    if increases > decreases:
        return "Increasing"
    elif decreases > increases:
        return "Decreasing"
    else:
        return "Mixed / Stable"


def repeated_condition(records, key, threshold, higher=True, minimum_occurrences=2):
    count = 0

    for record in records:
        if higher and record[key] >= threshold:
            count += 1
        elif not higher and record[key] < threshold:
            count += 1

    return count >= minimum_occurrences, count


def detect_pattern_chain(records, minimum_occurrences=2):
    if len(records) < minimum_occurrences:
        return "Not enough data for Pattern Chain analysis."

    sleep_average = average(records, "sleep")
    study_average = average(records, "study")
    task_average = average(records, "tasks")

    high_sleep_days = 0
    high_sleep_and_study_days = 0
    high_sleep_study_task_days = 0

    for record in records:
        if record["sleep"] >= sleep_average:
            high_sleep_days += 1

            if record["study"] >= study_average:
                high_sleep_and_study_days += 1

                if record["tasks"] >= task_average:
                    high_sleep_study_task_days += 1

    if high_sleep_study_task_days >= minimum_occurrences:
        return (
            "Pattern Chain Detected: In the recorded dataset, "
            "higher-than-average sleep repeatedly occurred together "
            "with higher-than-average study hours and task completion."
        )

    if high_sleep_and_study_days >= minimum_occurrences:
        return (
            "Partial Pattern Chain Detected: In the recorded dataset, "
            "higher-than-average sleep repeatedly occurred together "
            "with higher-than-average study hours."
        )

    return "No repeated Pattern Chain met the detection threshold."


def compare_workout_days(records):
    workout_tasks = []
    non_workout_tasks = []

    for record in records:
        if record["workout"]:
            workout_tasks.append(record["tasks"])
        else:
            non_workout_tasks.append(record["tasks"])

    workout_average = sum(workout_tasks) / len(workout_tasks) if workout_tasks else 0
    non_workout_average = sum(non_workout_tasks) / len(non_workout_tasks) if non_workout_tasks else 0

    return workout_average, non_workout_average


def analyze_patterns(records):
    return {
        "study_trend": trend(records, "study"),
        "sleep_trend": trend(records, "sleep"),
        "task_trend": trend(records, "tasks"),
        "score_trend": trend(records, "score"),
        "highest_day": find_highest_score_day(records),
        "lowest_day": find_lowest_score_day(records),
        "pattern_chain": detect_pattern_chain(records),
        "workout_comparison": compare_workout_days(records)
    }
