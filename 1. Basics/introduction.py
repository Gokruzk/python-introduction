# hello world
print("hello, world")

print("\n")

"""
Is a comment
"""

# ? input/output
print('hello, "friend"')
print("hello, \"friend\"")

name = input("What's your name? ")
#? remove whitespace from str
name = name.strip()

#? capitalize str
name = name.capitalize()

# ? end has "\n" value by default, we can change that
print("hello, ", end="")
print(name)

print("hello, " + name)
print("hello,", name)
print(f"hello, {name}")
