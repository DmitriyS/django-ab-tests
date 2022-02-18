from abc import ABC, abstractmethod
from typing import Any, Type

from marshmallow import Schema, ValidationError as SchemaValidationError
from rest_framework.exceptions import ValidationError as ApiValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView


class BaseViewSerializer(ABC):
    def __init__(self, request: Request) -> None:
        self.request = request

    @abstractmethod
    def serialize(self, *args: Any, **kwargs: Any) -> dict:
        raise NotImplementedError()


class ApiView(GenericAPIView):
    request: Request
    serializer_class: Type[BaseViewSerializer]

    def get_serializer(self, *args: Any, **kwargs: Any) -> BaseViewSerializer:
        serializer_class = self.get_serializer_class()
        return serializer_class(self.request, *args, **kwargs)

    def serialize_response(self, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer()
        return Response(serializer.serialize(*args, **kwargs))


class ViewSchema(Schema):
    def handle_error(self, error: SchemaValidationError, data: dict, *, many: bool, **kwargs: Any) -> None:
        raise ApiValidationError(str(error))
