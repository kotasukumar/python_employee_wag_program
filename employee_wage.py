import random


def check_attendence(random_number):
    if random_number == 0:
        daily_wage = 8 * 20
    elif random_number == 1:
        daily_wage = 8 * 20
    else:
        daily_wage = 0

    return daily_wage


if __name__ == "__main__":
    random = random.randint(0, 2)
    wage = check_attendence(random)
    print(wage)
