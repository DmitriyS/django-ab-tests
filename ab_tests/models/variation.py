from django.db.models import CASCADE, CharField, ForeignKey, Model, PositiveIntegerField

from .experiment import Experiment


class Variation(Model):
    experiment: Experiment = ForeignKey(Experiment, related_name='variations', on_delete=CASCADE)
    name: str = CharField(max_length=255)
    probability: int = PositiveIntegerField()

    class Meta:
        db_table = 'variations'

    def __str__(self) -> str:
        return self.name
