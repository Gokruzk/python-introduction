

# * Strings

# TODO: remove whitespace from str
name = input("What's your name? ")
name = name.strip()

# TODO: capitalize str
name = name.capitalize()

# ? end has "\n" value by default, we can change that
print("hello, ", end="")
print(name)

# ? concatenations
print("hello, " + name)
print("hello,", name)
print(f"hello, {name}")

# TODO: remove whitespace and capitalize each word
myname = '  nigell jama  '
myname = myname.strip().title()
print(f"hello, {myname}")  # ? hello, Nigell Jama

# TODO: read, remove whitespace and capitalize each word
myname = input("What's your name? ").strip().title()
print(f"hello, {myname}")

# TODO: split user's name into first name and last name
first, name = myname.split(' ')
print(f'hello {first}')
