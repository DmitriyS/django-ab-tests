from .lib.case import BaseApiTestCase


class GroupTestCase(BaseApiTestCase):
    def test_get_experiments(self) -> None:
        experiments = self.api.get_experiments()

        self.assertEqual(len(experiments), self.experiments_count)
        for e in experiments:
            self.assertEqual(len(e.variations), self.variations_count)

    def test_get_groups(self) -> None:
        experiments = self.api.get_experiments()
        groups = self.api.get_groups(self.idfa)

        self.assertEqual(len(groups), self.experiments_count)
        for g in groups:
            self.assertIn(g.name, [e.name for e in experiments])
            self.assertIn(g.value, [v.name for e in experiments for v in e.variations])

    def test_idfa_group_persistence(self) -> None:
        groups_1 = self.api.get_groups(self.idfa)
        groups_2 = self.api.get_groups(self.idfa)

        self.assertEqual(groups_1, groups_2)

    def setUp(self) -> None:
        self.idfa = self.generator.idfa()
        self.experiments_count = self.generator.random_count()
        self.variations_count = self.generator.random_count()
        self.generator.create_varied_experiments(self.experiments_count, self.variations_count)
