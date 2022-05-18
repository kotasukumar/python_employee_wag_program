import random


def check_attendence(total_days):
    daily_wage = present_days = working_hours = 0
    while present_days != 20 and working_hours != 100:
        random_number = random.randint(0, 2)
        if random_number == 0:
            daily_wage += (8 * 20)
            present_days += 1
            working_hours += 8
        elif random_number == 1:
            daily_wage += (8 * 20)
            present_days += 1
            working_hours += 8
        else:
            daily_wage += 0

    return daily_wage


if __name__ == "__main__":
    wage = check_attendence(20)
    print(wage)
