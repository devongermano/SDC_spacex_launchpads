from flask import Response


class ApiError(Exception):
    """Base class for all api-related errors."""
    error_response = Response()
    pass

class ClientError(ApiError):
