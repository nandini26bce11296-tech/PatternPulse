from input_handler import collect_records
from score_calculator import calculate_all_scores
from pattern_analyzer import analyze_patterns
from consistency_analyzer import analyze_consistency
from insight_generator import generate_insights
from report_generator import generate_full_report


def show_menu():
    print()
    print("========================================")
    print("              PATTERNPULSE")
    print("========================================")
    print("1. Enter / Replace Daily Data")
    print("2. View Daily Scores")
    print("3. Analyze Patterns")
    print("4. Analyze Consistency")
    print("5. Generate Full Report")
    print("6. Exit")


def has_data(records):
    if len(records) == 0:
        print("\nNo data available. Please enter daily data first.")
        return False
    return True


def main():
    records = []
    pattern_data = None
    consistency_data = None
    insights = []

    print("Welcome to PatternPulse!")
    print("A Personal Routine Pattern Analyzer")

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                records = collect_records()
                records = calculate_all_scores(records)
                pattern_data = None
                consistency_data = None
                insights = []
                print("\nData collected successfully.")

            elif choice == 2:
                if has_data(records):
                    for record in records:
                        print(
                            "Day", record["day"],
                            "| Score:", record["score"]
                        )

            elif choice == 3:
                if has_data(records):
                    pattern_data = analyze_patterns(records)

                    print("\nStudy Trend :", pattern_data["study_trend"])
                    print("Sleep Trend :", pattern_data["sleep_trend"])
                    print("Task Trend  :", pattern_data["task_trend"])
                    print("Score Trend :", pattern_data["score_trend"])
                    print("\n" + pattern_data["pattern_chain"])

            elif choice == 4:
                if has_data(records):
                    consistency_data = analyze_consistency(records)

                    print("\nConsistency Score :", consistency_data["score"])
                    print("Consistency Level :", consistency_data["label"])
                    print(consistency_data["message"])

            elif choice == 5:
                if has_data(records):
                    pattern_data = analyze_patterns(records)
                    consistency_data = analyze_consistency(records)
                    insights = generate_insights(
                        records,
                        pattern_data,
                        consistency_data
                    )
                    generate_full_report(
                        records,
                        pattern_data,
                        consistency_data,
                        insights
                    )

            elif choice == 6:
                print("\nThank you for using PatternPulse!")
                break

            else:
                print("Please select a number from 1 to 6.")

        except ValueError:
            print("Invalid choice. Please enter a whole number.")


if __name__ == "__main__":
    main()
