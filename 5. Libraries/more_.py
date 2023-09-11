import statistics
import sys

n = statistics.mean([100, 90])
print(n)

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# ? check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
    # sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1:])

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)
