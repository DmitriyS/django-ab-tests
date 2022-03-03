import random
from typing import Iterable

from django.utils.crypto import get_random_string

from ab_tests.models import Experiment, Variation


class Generator:
    total_variations_probability: int = 100

    def idfa(self) -> str:
        return get_random_string(32)

    def create_varied_experiments(self, experiments_count: int = 1, variations_count: int = 1) -> None:
        for _ in range(experiments_count):
            e = Experiment.objects.create(name=get_random_string(100))
            for variation_probability in self.split_variations(variations_count):
                Variation.objects.create(experiment=e, name=get_random_string(10), probability=variation_probability)

    def split_variations(self, variations_count: int) -> Iterable[int]:
        probability_left: int = self.total_variations_probability
        for i in range(variations_count - 1):
            variation_probability = random.randint(1, probability_left - variations_count + i)
            yield variation_probability
            probability_left -= variation_probability
        yield probability_left

    def random_count(self, low: int = 1, high: int = 3) -> int:
        return random.randint(low, high)
