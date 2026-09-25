def get_positive_number(prompt, minimum=0, maximum=None):
    while True:
        try:
            value = float(input(prompt))
            if value < minimum:
                print("Value cannot be below", minimum)
            elif maximum is not None and value > maximum:
                print("Value cannot be above", maximum)
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


def get_integer(prompt, minimum=1, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print("Value must be at least", minimum)
            elif maximum is not None and value > maximum:
                print("Value cannot be above", maximum)
            else:
                return value
        except ValueError:
            print("Please enter a valid whole number.")


def get_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value == "yes" or value == "y":
            return True
        elif value == "no" or value == "n":
            return False
        else:
            print("Please enter Yes or No.")


def collect_day(day_number):
    print("\n---------- Day", day_number, "----------")

    study = get_positive_number("Study hours: ", 0, 24)
    sleep = get_positive_number("Sleep hours: ", 0, 24)
    tasks = get_integer("Tasks completed: ", 0, 100)
    workout = get_yes_no("Workout/activity completed? (Yes/No): ")
    mood = get_integer("Mood rating (1-5): ", 1, 5)

    return {
        "day": day_number,
        "study": study,
        "sleep": sleep,
        "tasks": tasks,
        "workout": workout,
        "mood": mood
    }


def collect_records():
    days = get_integer("Enter number of days to analyze (3-30): ", 3, 30)
    records = []

    for day in range(1, days + 1):
        records.append(collect_day(day))

    return records
