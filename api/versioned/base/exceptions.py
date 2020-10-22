from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.exceptions import APIException
from rest_framework.response import Response


class CustomAPIError(APIException):
    status_code = 406
    default_detail = "Not Acceptable."
    default_code = 406

    def __init__(self, detail=None, code=None, status_code=None):
        if detail:
            self.default_detail = detail
        if code:
            self.default_code = code

        if status_code:
            self.status_code = status_code

        self.detail = self.default_detail


def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException) or isinstance(exc, CustomAPIError):
        if isinstance(exc.default_code, int):
            status_code = exc.default_code
        else:
            status_code = exc.status_code
        data = {
            "status_code": status_code,
            "errors": {},
        }  # status_code used in renderers
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait
        if isinstance(exc.detail, list):
            data["errors"]["non_field_errors"] = exc.detail
        elif isinstance(exc.detail, dict):
            data["errors"] = exc.detail
        else:
            data["errors"]["non_field_errors"] = [exc.detail]
        return Response(data, status=exc.status_code, headers=headers)
        # else:
        #     data = {'status_code': 500, 'errors': {}}  # status_code used in renderers
        #     data['errors']['non_field_errors'] = [f'{exc.__class__.__name__}: {exc}']
        # return Response(data, status=500)
