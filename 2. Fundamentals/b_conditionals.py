# Conditionals

def main():

    # * Symbols: > >= < <= == !=
    # introduction()

    print('\n')

    # * Symbols: + - * / %

    # TODO: check if number is odd or even
    x = int(input("What's x? "))
    if is_even(x):
        print(f'{x} is an even number')
    else:
        print(f'{x} is an odd number')

    # ? match
    house()


def introduction():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    # TODO: use > and <
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")

    print('\n')

    # TODO: use or
    if x < y or x > y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

    # TODO: use ==
    if x == y:
        print("x is equal to y")
    else:
        print("x is not equal to y")

    print("\n")

    # TODO: use and
    score = int(input("Score: "))

    if score >= 90 and score <= 100:
        print("Grade: A")
    elif score >= 80 and score < 90:
        print('Grade: B')
    elif score >= 70 and score < 80:
        print('Grade: C')
    elif score >= 60 and score < 70:
        print('Grade: D')
    else:
        print('Grade: F')

    if 90 <= score <= 100:
        print("Grade: A")
    elif 80 <= score < 90:
        print('Grade: B')
    elif 70 <= score < 80:
        print('Grade: C')
    elif 60 <= score < 70:
        print('Grade: D')
    else:
        print('Grade: F')

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print('Grade: B')
    elif score >= 70:
        print('Grade: C')
    elif score >= 60:
        print('Grade: D')
    else:
        print('Grade: F')


def is_even(n):
    return n % 2 == 0


def house():
    name = input("What's your name? ")

    match name:
        case "Harry":
            print("Gryffindor")
        case "Hermione":
            print("Gryffindor")
        case "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")

main()
