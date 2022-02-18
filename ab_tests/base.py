from typing import Type

from marshmallow import Schema, ValidationError as SchemaValidationError
from rest_framework.exceptions import ValidationError as ApiValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class BaseViewSerializer:
    def __init__(self, request: Request):
        self.request = request

    def serialize(self, *args, **kwargs) -> dict:
        raise NotImplementedError()


class ApiView(GenericAPIView):
    request: Request
    serializer_class: Type[BaseViewSerializer]

    def get_serializer(self, *args, **kwargs) -> BaseViewSerializer:
        serializer_class = self.get_serializer_class()
        return serializer_class(self.request, *args, **kwargs)

    def serialize_response(self, *args, **kwargs) -> Response:
        serializer = self.get_serializer()
        return Response(serializer.serialize(*args, **kwargs))


class ViewSchema(Schema):
    def handle_error(self, error: SchemaValidationError, data: dict, *, many: bool, **kwargs):
        raise ApiValidationError(error)
