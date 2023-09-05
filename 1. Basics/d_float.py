
# * Float
x = float(input("What's x? "))  # ? 1.2
y = float(input("What's y "))  # ? 3.4

z = round(x + y)
print(z)  # ? 5

print('\n')

z = float(input("z? "))  # ? 1000
print(f'{z:,}')  # ? 1,000

print('\n')

# ? number of digits
z = x / y
print(f'{z:.2f}')  # ? two digits

z = round(x / y, 2)  # ? two digits
print(z)
