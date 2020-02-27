import random


def apply(func, iterable):
    return list(map(func, iterable))


def weighted_choice(population, weights):
    [choice] = random.choices(population, weights, k=1)
    return choice
