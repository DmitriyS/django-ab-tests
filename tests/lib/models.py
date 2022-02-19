from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from ab_tests.utils import apply


class TestModel(ABC):
    @classmethod
    @abstractmethod
    def deserialize(cls, data: dict) -> TestModel:
        raise NotImplementedError()


@dataclass
class TestExperimentVariation(TestModel):
    name: str
    probability: int

    @classmethod
    def deserialize(cls, data: dict) -> TestExperimentVariation:
        return TestExperimentVariation(
            name=data['name'],
            probability=data['probability'],
        )


@dataclass
class TestExperiment(TestModel):
    name: str
    variations: list[TestExperimentVariation]

    @classmethod
    def deserialize(cls, data: dict) -> TestExperiment:
        return TestExperiment(
            name=data['name'],
            variations=apply(TestExperimentVariation.deserialize, data['groups']),
        )


@dataclass
class TestGroup(TestModel):
    name: str
    value: str

    @classmethod
    def deserialize(cls, data: dict) -> TestGroup:
        return TestGroup(
            name=data['name'],
            value=data['value'],
        )
