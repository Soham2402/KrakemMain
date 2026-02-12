from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from project.utils import CreateProjectSchema
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from typing import Dict


class Project(APIView):
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
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": str(v)})
        except Exception as e:
            # Add logger
            print(str(e))
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data={"error": "There was an error please try again later"})
