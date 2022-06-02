import logging

from rest_framework import response
from rest_framework import request
from rest_framework import decorators
from rest_framework import permissions

logging.basicConfig(level=logging.DEBUG)


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def ping(req: request.Request) -> response.Response:
    logging.debug(req.data.__str__())
    return response.Response()
