# Dictionary

def main():
    students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin"
    }
    # printDict(students)
    students2 = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None}
    ]
    moreStudents(students2)


def printDict(d):
    for student in d:
        print(f"{student}: {d[student]}")


def moreStudents(st):
    for ss in st:
        print(ss["name"], ss["house"], ss["patronus"], sep=", ")


main()
