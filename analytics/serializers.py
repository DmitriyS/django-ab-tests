from typing import List

from analytics.base import BaseViewSerializer
from analytics.models import Variation
from analytics.utils import apply
from analytics.view_models import ExperimentViewModel, GroupViewModel


class ExperimentListSerializer(BaseViewSerializer):
    def serialize(self, experiments: List[ExperimentViewModel]) -> dict:
        return {'tests': apply(self.serialize_experiment, experiments)}

    def serialize_experiment(self, experiment_view: ExperimentViewModel) -> dict:
        return {
            'name': experiment_view.experiment.name,
            'groups': apply(self.serialize_variation, experiment_view.variations),
        }

    def serialize_variation(self, variation: Variation) -> dict:
        return {'name': variation.name, 'probability': variation.probability}


class GroupListSerializer(BaseViewSerializer):
    def serialize(self, groups: List[GroupViewModel]) -> dict:
        return {'groups': apply(self.serialize_group, groups)}

    def serialize_group(self, group_view: GroupViewModel) -> dict:
        return {'name': group_view.experiment.name, 'value': group_view.variation.name}
