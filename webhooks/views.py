from rest_framework import response
from rest_framework import request
from rest_framework import decorators
from rest_framework import permissions


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.AllowAny])
def index(req: request.Request) -> response.Response:
    return response.Response("index")


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def ping(req: request.Request) -> response.Response:
    print(req.data)
    return response.Response()
