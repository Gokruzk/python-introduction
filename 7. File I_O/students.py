import csv

def main():
    students = []
    with open("names.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row['name'], "house": row['house']})

    def get_name(student):
        return student["name"]

    for student in sorted(students, key=get_name):
        print(f"{student['name']} is in {student['house']}")
    print("\n")
    for student in sorted(students, key=lambda student: student["house"]):
        print(f"{student['name']} is in {student['house']}")


if __name__ == "__main__":
    main()
