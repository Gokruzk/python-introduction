# Loops

def main():
    # whileMeow()
    # forWoof2()
    # print("xd\n" * 3, end="")
    # number = get_number()
    # printHello(number)
    print_list2()


def whileMeow():
    i = 0
    while i <= 2:
        print("meow")
        i += 1


def forWoof():
    for i in [0, 1, 2]:
        print("woof")


def forWoof2():
    for _ in range(3):
        print("woof")


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def printHello(n):
    for _ in range(n):
        print("hello")

def print_list():
    students = ["Hermione", "Harry", "Ron"]
    for student in students:
        print(student)

def print_list2():
    students = ["Hermione", "Harry", "Ron"]
    for i in range(len(students)):
        print(i + 1, students[i])

main()
