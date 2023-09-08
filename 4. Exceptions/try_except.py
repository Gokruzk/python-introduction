# Exceptions

def run():
    # print("Hello world) # ? syntax error
    # handle_error_input()
    # while_handle_error_input()
    # print(f"x is {get_int()}")
    print(f"x is {get_int_pass('Whats x? ') }")


def handle_error_input():
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not integer")
    else:
        print(f"x is {x}")


def while_handle_error_input():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not integer")
        else:
            break

    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not integer")


def get_int_pass(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


run()
