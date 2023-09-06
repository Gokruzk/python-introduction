
# * Functions

def main():

    name = input("What's your name? ").strip().title()
    hello()  # ? Hello world
    hello(name)

    x = int(input("What's x? "))
    print("x squared is ", square(x))


# TODO: define a function with default value in argument


def hello(to='world'):
    print(f'Hello, {to}')

# TODO: define a function to return the square of number


def square(n):
    return n ** 2


main()
