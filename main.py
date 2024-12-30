from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
    }
    user_birthdays = {day: [] for day in weekdays.values()}
    today = date.today()
    next_week = today + timedelta(days=7)

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        birthday_next_year = user["birthday"].replace(year=today.year + 1)

        if today <= birthday_this_year <= next_week:
            birthday = birthday_this_year
        elif today <= next_week and birthday_next_year <= next_week:
            birthday = birthday_next_year
        else:
            continue

        weekday = birthday.weekday()

        if weekday == 5 or weekday == 6:
            user_birthdays["Monday"].append(user["name"].split(" ")[0])
        else:
            user_birthdays[weekdays[weekday]].append(user["name"].split(" ")[0])

    user_birthdays = {day: names for day, names in user_birthdays.items() if names}
    return user_birthdays

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
