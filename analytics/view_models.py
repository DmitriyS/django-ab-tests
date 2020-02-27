from typing import List

from analytics.models import Variation, Experiment, Group


class ExperimentViewModel:
    def __init__(self, experiment: Experiment, variations: List[Variation]):
        self.experiment = experiment
        self.variations = variations

    @classmethod
    def from_experiment(cls, experiment: Experiment) -> 'ExperimentViewModel':
        return cls(experiment=experiment, variations=list(experiment.variations.all()))


class GroupViewModel:
    def __init__(self, experiment: Experiment, variation: Variation):
        self.experiment = experiment
        self.variation = variation

    @classmethod
    def from_group(cls, group: Group) -> 'GroupViewModel':
        return cls(experiment=group.variation.experiment, variation=group.variation)
