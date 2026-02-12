from typing import Dict

from django.contrib.auth.models import User
from project.models import Project

from KrakemBackend.utils import RequestSchema


class CreateProjectSchema(RequestSchema):
    required_fields: set[str] = {"name", "description"}

    @classmethod
    def create(cls, request) -> str:
        data: Dict = request.data
        user: User = request.user
        project = Project.objects.create(name=data["name"], owner=user,
                                         description=data["description"])
        return str(project.project_id)
