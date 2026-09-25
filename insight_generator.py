def generate_insights(records, pattern_data, consistency_data):
    insights = []

    if pattern_data["score_trend"] == "Increasing":
        insights.append("The overall PatternPulse score shows an increasing trend.")
    elif pattern_data["score_trend"] == "Decreasing":
        insights.append("The overall PatternPulse score shows a decreasing trend.")
    else:
        insights.append("The overall PatternPulse score shows a mixed or stable trend.")

    if pattern_data["study_trend"] == "Increasing":
        insights.append("Recorded study hours generally increased across the observations.")
    elif pattern_data["study_trend"] == "Decreasing":
        insights.append("Recorded study hours generally decreased across the observations.")

    if pattern_data["task_trend"] == "Increasing":
        insights.append("Task completion generally increased across the observations.")
    elif pattern_data["task_trend"] == "Decreasing":
        insights.append("Task completion generally decreased across the observations.")

    workout_average, non_workout_average = pattern_data["workout_comparison"]

    if workout_average > 0 and non_workout_average > 0:
        if workout_average > non_workout_average:
            insights.append(
                "Workout/activity days had a higher average task completion "
                "than non-workout days in the recorded dataset."
            )
        elif workout_average < non_workout_average:
            insights.append(
                "Non-workout days had a higher average task completion "
                "than workout/activity days in the recorded dataset."
            )
        else:
            insights.append(
                "Workout/activity and non-workout days had the same average "
                "task completion in the recorded dataset."
            )

    insights.append(pattern_data["pattern_chain"])
    insights.append(
        "Consistency classification: " + consistency_data["label"] + "."
    )

    return insights
