
def main():
    # print_column(3)
    # print_row(4)
    print_square2(4)


def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    print("?" * width)


def print_square(size):
    # ? for each row in square
    for i in range(size):
        # ? for each row in square
        for j in range(size):
            # ? print brick
            print("#", end="")
        # ? print a new line
        print()

def print_square2(size):
    for i in range(size):
        print_row(size)

main()
