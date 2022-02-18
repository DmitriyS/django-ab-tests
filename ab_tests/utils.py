import random
from typing import Any, Callable, Iterable, Sequence, TypeVar


Object = TypeVar('Object')
FunctionReturnValue = TypeVar('FunctionReturnValue', bound=Any)
Function = Callable[[Object], FunctionReturnValue]


def apply(func: Function, iterable: Iterable[Object]) -> list[FunctionReturnValue]:
    return list(map(func, iterable))


def weighted_choice(population: Sequence[Object], weights: list[int]) -> Object:
    [choice] = random.choices(population, weights, k=1)
    return choice
