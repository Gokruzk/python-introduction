from hello import hello


def test_default():
    hello() == "hello, world"


def test_argument():
    hello("David") == "hello, David"


def test_argument_loop():
    for name in ["Hermione", "Harry", "Ron"]:
        hello("David") == f"hello, {name}"
