from django.utils.functional import cached_property
from rest_framework.test import APITestCase

from .api import Api


class BaseApiTestCase(APITestCase):
    @cached_property
    def api(self) -> Api:
        return Api(client=self.client)  # noqa
