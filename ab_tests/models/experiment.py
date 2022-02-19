from __future__ import annotations

from django.db.models import CharField, Model, QuerySet

from ..types import Idfa


class ExperimentQuerySet(QuerySet):
    def select_experiments_with_variations(self) -> ExperimentQuerySet:
        return self.prefetch_related('variations').all()

    def select_experiments_that_groups_do_not_participate_in(self, idfa: Idfa) -> ExperimentQuerySet:
        return self.select_experiments_with_variations().exclude(variations__group__idfa=idfa)


class Experiment(Model):
    name: str = CharField(max_length=255)

    objects: ExperimentQuerySet = ExperimentQuerySet.as_manager()

    class Meta:
        db_table = 'experiments'

    def __str__(self) -> str:
        return self.name
