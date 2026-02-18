from typing import Dict, Tuple, List

from django.contrib.auth.models import User
from project.models import Project, Resource

from KrakemBackend.utils import RequestSchema
from project.constants import ResourceTypeConstants


class CreateProjectSchema(RequestSchema):
    required_fields: set[str] = {"name", "description"}

    @classmethod
    def create(cls, request) -> str:
        data: Dict = request.data
        user: User = request.user
        project = Project.objects.create(
            name=data["name"], owner=user, description=data["description"]
        )
        return str(project.project_id)

    @classmethod
    def get(cls, request, project_id: str = "") -> Dict:
        user = request.user
        if project_id is None:
            pass
        project_ids = (
            Project.objects.filter(owner=user)
            .order_by("created_on")
            .values("project_id", "name", "description")
        )
        return project_ids


class AddProjectResourcesSchema(RequestSchema):
    required_fields: set[str] = {"project_id", "pdf", "doc", "text"}

    TYPE_MAPPING = {
        "pdf": ResourceTypeConstants.PDF,
        "doc": ResourceTypeConstants.DOC,
        "text": ResourceTypeConstants.TEXT,
    }

    def _get_project(project_id: str, user: User) -> Tuple[str, Project]:
        try:
            project = Project.objects.get(
                owner=user, project_id=project_id, is_active=True
            )
            return "", project
        except Project.DoesNotExist:
            return (
                f"Project with ID {project_id} does not exist or is deactivated",
                None,
            )

    @classmethod
    def create(cls, request) -> str:
        data = request.data
        user = request.user

        # 1. Validate Project
        project_id = data.get("project_id")
        err, project = cls._get_project(project_id=project_id, user=user)
        if err:
            raise ValueError(err)

        # 2. Iterate through expected resource keys
        for key, resource_type_int in cls.TYPE_MAPPING.items():
            # Use getlist to handle multiple files for the same key
            # data.getlist() is available on QueryDict objects (request.data)
            files = data.getlist(key) if hasattr(data, 'getlist') else []

            for file_item in files:
                # Check if the item is actually a file object and not an empty string
                if not file_item or isinstance(file_item, str):
                    continue

                # 3. Create the Resource entry
                Resource.objects.create(
                    project=project,
                    owner=user,
                    resource_type=resource_type_int,
                    data=file_item,
                    title=getattr(file_item, 'name', f"{key}_resource")[:36]
                )

        return str(project.project_id)