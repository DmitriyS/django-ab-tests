from rest_framework.request import Request
from rest_framework.response import Response
from webargs.djangoparser import use_args

from ab_tests.base import ApiView
from ab_tests.schemas import IdfaSchema
from ab_tests.serializers import ExperimentListSerializer, GroupListSerializer
from ab_tests.service import AnalyticsService
from ab_tests.types import Idfa


class BaseAnalyticsView(ApiView):
    @property
    def service(self) -> AnalyticsService:
        return AnalyticsService()


class ExperimentListView(BaseAnalyticsView):
    serializer_class = ExperimentListSerializer

    def get(self, request: Request) -> Response:
        experiments = self.service.list_experiments()
        return self.serialize_response(experiments)


class GroupListView(BaseAnalyticsView):
    serializer_class = GroupListSerializer

    @use_args(IdfaSchema)
    def get(self, request: Request, idfa: Idfa) -> Response:
        groups = self.service.populate_and_list_groups(idfa)
        return self.serialize_response(groups)
