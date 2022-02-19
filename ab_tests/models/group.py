from __future__ import annotations

from django.db.models import CASCADE, CharField, ForeignKey, Model, QuerySet

from .variation import Variation
from ..types import Idfa


class GroupQuerySet(QuerySet):
    def select_groups(self, idfa: Idfa) -> GroupQuerySet:
        return self.filter(idfa=idfa).prefetch_related('variation', 'variation__experiment')


class Group(Model):
    idfa: Idfa = CharField(max_length=64)
    variation = ForeignKey(Variation, on_delete=CASCADE)

    objects: GroupQuerySet = GroupQuerySet.as_manager()

    class Meta:
        db_table = 'groups'

    def __str__(self) -> str:
        return str(self.idfa)
