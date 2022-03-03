from django.utils.functional import cached_property
from rest_framework.test import APITestCase

from .api import Api
from .generator import Generator


class BaseApiTestCase(APITestCase):
    @cached_property
    def api(self) -> Api:
        return Api(client=self.client)  # noqa

    @cached_property
    def generator(self) -> Generator:
        return Generator()
