from flask import Response


class CustomResponse(Response):
    default_mimetype = 'application/json'
