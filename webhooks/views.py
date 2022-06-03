import logging
import os.path

from django.conf import settings
from rest_framework import response
from rest_framework import request
from rest_framework import decorators
from rest_framework import permissions
from rest_framework import status

import subprocess

logging.basicConfig(level=logging.DEBUG)


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def handle(req: request.Request, project_name: str) -> response.Response:

    logging.debug(project_name)
    logging.debug(settings.PROJECTS)

    for project in settings.PROJECTS:
        if project_name == project['name']:

            if os.path.exists(project['path']):
                cwd = os.getcwd()

                os.chdir(project['path'])

                url = f'https://{settings.GITHUB_USER}:{settings.GITHUB_TOKEN}@{settings.GITHUB_HOST}/{project["owner"]}/{project["name"]}.git'

                out = subprocess.run(['git', 'pull', url], capture_output=True)

                logging.debug(out.__str__())

                os.chdir(cwd)

                return response.Response()

    return response.Response(status=status.HTTP_404_NOT_FOUND)
