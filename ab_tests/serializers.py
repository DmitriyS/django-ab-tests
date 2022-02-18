from ab_tests.base import BaseViewSerializer
from ab_tests.models import Variation
from ab_tests.utils import apply
from ab_tests.view_models import ExperimentViewModel, GroupViewModel


class ExperimentListSerializer(BaseViewSerializer):
    def serialize(self, experiments: list[ExperimentViewModel]) -> dict:
        return {
            'tests': apply(self.serialize_experiment, experiments),
        }

    def serialize_experiment(self, experiment_view: ExperimentViewModel) -> dict:
        return {
            'name': experiment_view.experiment.name,
            'groups': apply(self.serialize_variation, experiment_view.variations),
        }

    def serialize_variation(self, variation: Variation) -> dict:
        return {
            'name': variation.name,
            'probability': variation.probability,
        }


class GroupListSerializer(BaseViewSerializer):
    def serialize(self, groups: list[GroupViewModel]) -> dict:
        return {
            'groups': apply(self.serialize_group, groups),
        }

    def serialize_group(self, group_view: GroupViewModel) -> dict:
        return {
            'name': group_view.experiment.name,
            'value': group_view.variation.name,
        }
