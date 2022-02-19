from rest_framework.response import Response


class ApiError(Exception):
    def __init__(self, response: Response) -> None:
        self.response = response

    @property
    def status_code(self) -> int:
        return self.response.status_code
