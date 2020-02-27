from rest_framework.request import Request
from rest_framework.response import Response
from webargs.djangoparser import use_args

from analytics.base import ApiView
from analytics.schemas import IdfaSchema
from analytics.serializers import ExperimentListSerializer
from analytics.serializers import GroupListSerializer
from analytics.service import AnalyticsService
from analytics.types import Idfa


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
