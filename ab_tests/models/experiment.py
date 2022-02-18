from typing import List, Union

from django.db.models import Model, CharField, Manager, QuerySet

from ab_tests.types import Idfa


Experiments = Union[QuerySet, List['Experiment']]


class ExperimentManager(Manager):
    def select_experiments_with_variations(self) -> Experiments:
        return self.all().prefetch_related('variations')

    def select_experiments_that_groups_do_not_participate_in(self, idfa: Idfa) -> Experiments:
        return self.select_experiments_with_variations().exclude(variations__group__idfa=idfa)


class Experiment(Model):
    name = CharField(max_length=255)

    objects = ExperimentManager()

    class Meta:
        db_table = 'experiments'

    def __str__(self):
        return self.name
