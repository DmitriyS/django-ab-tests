from __future__ import annotations

from dataclasses import dataclass

from ab_tests.models import Variation, Experiment, Group


@dataclass
class ExperimentViewModel:
    experiment: Experiment
    variations: list[Variation]

    @classmethod
    def from_experiment(cls, experiment: Experiment) -> ExperimentViewModel:
        return cls(experiment=experiment, variations=list(experiment.variations.all()))


@dataclass
class GroupViewModel:
    experiment: Experiment
    variation: Variation

    @classmethod
    def from_group(cls, group: Group) -> GroupViewModel:
        return cls(experiment=group.variation.experiment, variation=group.variation)
