def main():
    names = []

    name = input("What's your name? ")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")

    with open("names.txt") as file2:
        for line in file2:
            names.append(line.rstrip())

    for name in sorted(names):
        print(f"hello, {name}")


if __name__ == "__main__":
    main()
