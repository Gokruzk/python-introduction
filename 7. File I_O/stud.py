import csv


def main():
    name = input("What's your name? ")
    house = input("What's your house? ")
    with open("students.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house"])
        file.write("\n")
        writer.writerow({"name": name, "house": house})


if __name__ == "__main__":
    main()
