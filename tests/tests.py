from django.utils.crypto import get_random_string

from ab_tests.models import Experiment, Variation
from .lib.case import BaseApiTestCase


class GroupTestCase(BaseApiTestCase):
    total_probability: int = 100

    def test_get_experiments(self) -> None:
        experiments = self.api.get_experiments()
        self.assertEqual(len(experiments), 1)

        [experiment] = experiments
        self.assertEqual(experiment.name, self.experiment_name)
        self.assertEqual(len(experiment.variations), 1)

        [variation] = experiment.variations
        self.assertEqual(variation.name, self.variation_name)
        self.assertEqual(variation.probability, self.variation_probability)

    def test_get_groups(self) -> None:
        groups = self.api.get_groups(self.idfa)

        self.assertEqual(len(groups), 1)
        [group] = groups
        self.assertEqual(group.name, self.experiment_name)
        self.assertEqual(group.value, self.variation_name)

    def test_idfa_group_persistence(self) -> None:
        groups_1 = self.api.get_groups(self.idfa)
        groups_2 = self.api.get_groups(self.idfa)

        self.assertEqual(groups_1, groups_2)

    def setUp(self) -> None:
        self.idfa = get_random_string(32)
        self.experiment_name = get_random_string(100)
        self.variation_name = get_random_string(10)
        self.variation_probability = self.total_probability

        self.create_varied_experiment()

    def create_varied_experiment(self) -> None:
        e = Experiment.objects.create(name=self.experiment_name)
        Variation.objects.create(experiment=e, name=self.variation_name, probability=self.variation_probability)
