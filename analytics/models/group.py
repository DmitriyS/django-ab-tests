from typing import List, Union

from django.db.models import Model, CharField, ForeignKey, CASCADE, Manager, QuerySet

from analytics.types import Idfa


Experiments = Union[QuerySet, List['Group']]


class GroupManager(Manager):
    def select_groups(self, idfa: Idfa) -> Experiments:
        return self.filter(idfa=idfa).prefetch_related('variation', 'variation__experiment')


class Group(Model):
    idfa = CharField(max_length=64)
    variation = ForeignKey('analytics.Variation', on_delete=CASCADE)

    objects = GroupManager()

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.idfa
