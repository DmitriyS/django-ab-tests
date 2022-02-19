from urllib.parse import urljoin

from rest_framework.response import Response
from rest_framework.test import APIClient

from ab_tests.utils import apply
from .errors import ApiError
from .models import TestExperiment, TestGroup


class BaseApi:
    BASE_PATH: str

    def __init__(self, client: APIClient) -> None:
        self.client = client

    def make_url(self, url: str) -> str:
        return urljoin(self.BASE_PATH, url)

    def assert_response_code(self, response: Response, expected_code: int) -> None:
        if response.status_code != expected_code:
            raise ApiError(response)


class Api(BaseApi):
    BASE_PATH: str = '/'

    def get_experiments(self) -> list[TestExperiment]:
        r = self.client.get(self.make_url('experiments/'))
        self.assert_response_code(r, 200)
        return apply(TestExperiment.deserialize, r.json()['tests'])

    def get_groups(self, idfa: str) -> list[TestGroup]:
        r = self.client.get(self.make_url('groups/'), data={'idfa': idfa})
        self.assert_response_code(r, 200)
        return apply(TestGroup.deserialize, r.json()['groups'])
