from typing import Any

from marshmallow import post_load
from marshmallow.fields import String

from .base import ViewSchema
from .types import Idfa


class IdfaSchema(ViewSchema):
    idfa = String(required=True)

    @post_load
    def deserialize(self, data: dict, **kwargs: Any) -> Idfa:
        return Idfa(data['idfa'])
