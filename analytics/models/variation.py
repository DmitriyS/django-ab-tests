from django.db.models import Model, ForeignKey, CASCADE, PositiveIntegerField, CharField


class Variation(Model):
    experiment = ForeignKey('analytics.Experiment', related_name='variations', on_delete=CASCADE)
    name = CharField(max_length=255)
    probability = PositiveIntegerField()

    class Meta:
        db_table = 'variations'

    def __str__(self):
        return self.name
