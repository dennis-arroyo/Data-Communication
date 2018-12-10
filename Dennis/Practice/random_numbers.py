import random


def get_numbers(orientation):
    numbers = str(random.randrange(orientation))

    counter = 0

    while counter < 5:
        numbers += "," + str(random.randrange(orientation))
        counter += 1

    return numbers

