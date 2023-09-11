import random
# from random import choice

# TODO: choice a random option
coin = random.choice(["heads", "tails"])
# coin = choice(["heads","tails"])
print(coin)

# TODO: get random number between 1 and 10
number = random.randint(1, 10)
print(number)

# TODO: shuffle a list
musics = ["creep", "overglow", "lift", "yellow"]
random.shuffle(musics)
for music in musics:
    print(music)
