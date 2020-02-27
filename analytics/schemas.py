from marshmallow import post_load
from marshmallow.fields import String

from analytics.base import ViewSchema
from analytics.types import Idfa


class IdfaSchema(ViewSchema):
    idfa = String(required=True)

    @post_load
    def deserialize(self, data: dict, **kwargs) -> Idfa:
        return Idfa(data['idfa'])
