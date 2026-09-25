def print_separator():
    print("=" * 55)


def print_daily_scores(records):
    print_separator()
    print("                 DAILY SCORES")
    print_separator()

    print("Day | Study | Sleep | Tasks | Workout | Mood | Score")

    for record in records:
        workout = "Yes" if record["workout"] else "No"

        print(
            record["day"], "|",
            record["study"], "|",
            record["sleep"], "|",
            record["tasks"], "|",
            workout, "|",
            record["mood"], "|",
            record["score"]
        )

    print()


def print_report(records, pattern_data, consistency_data, insights):
    study_average = sum(r["study"] for r in records) / len(records)
    sleep_average = sum(r["sleep"] for r in records) / len(records)
    task_average = sum(r["tasks"] for r in records) / len(records)

    highest = pattern_data["highest_day"]
    lowest = pattern_data["lowest_day"]

    print()
    print_separator()
    print("                 PATTERNPULSE REPORT")
    print_separator()

    print("Days Analyzed          :", len(records))
    print("Average Study Hours    :", round(study_average, 2))
    print("Average Sleep Hours    :", round(sleep_average, 2))
    print("Average Tasks Completed:", round(task_average, 2))

    print("Highest Score Day      :", "Day", highest["day"],
          "(", highest["score"], ")")
    print("Lowest Score Day       :", "Day", lowest["day"],
          "(", lowest["score"], ")")

    print("Consistency Score      :", consistency_data["score"])
    print("Consistency Level      :", consistency_data["label"])

    print()
    print("----------------------------------------")
    print("PATTERN ANALYSIS")
    print("----------------------------------------")

    print("Study Trend :", pattern_data["study_trend"])
    print("Sleep Trend :", pattern_data["sleep_trend"])
    print("Task Trend  :", pattern_data["task_trend"])
    print("Score Trend :", pattern_data["score_trend"])

    print()
    print("----------------------------------------")
    print("PATTERN CHAIN")
    print("----------------------------------------")
    print(pattern_data["pattern_chain"])

    print()
    print("----------------------------------------")
    print("GENERATED INSIGHTS")
    print("----------------------------------------")

    for number, insight in enumerate(insights, 1):
        print(str(number) + ".", insight)

    print()
    print_separator()


def generate_full_report(records, pattern_data, consistency_data, insights):
    print_daily_scores(records)
    print_report(records, pattern_data, consistency_data, insights)
