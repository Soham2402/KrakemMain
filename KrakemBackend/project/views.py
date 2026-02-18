from typing import Dict

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from project.utils import AddProjectResourcesSchema, CreateProjectSchema


class ProjectView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request) -> Response:
        try:
            data: Dict = request.data
            CreateProjectSchema.validate(payload=data)
            project_id: str = CreateProjectSchema.create(request=request)
            response_data: dict = {"project_id": project_id}
            return Response(data=response_data, status=status.HTTP_200_OK)

        except ValueError as v:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": str(v)})
        except Exception as e:
            # Add logger
            print(str(e))
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"error": "There was an error please try again later"},
            )

    def get(self, request, id=None) -> Response:
        try:
            projects = CreateProjectSchema.get(request=request, project_id=id)
            return Response(data={"data": projects}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"error": "There was an error please try again later"},
            )


class ProjectResources(APIView):
    def post(self, request) -> Response:
        try:
            data: Dict = request.data
            AddProjectResourcesSchema.validate(payload=data)
            AddProjectResourcesSchema.create(request=request)
            return Response(
                status=status.HTTP_201_CREATED, 
                data={"message": "Resources uploaded successfully"})
        
        except ValueError as v:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": str(v)})

        except Exception as e:
            # TODO add logger
            # In production, use: logger.error(f"Upload error: {e}")
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={"error": "Internal server error"},)
