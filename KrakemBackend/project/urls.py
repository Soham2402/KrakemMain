from django.urls import path
from project.views import ProjectView, ProjectResources

urlpatterns = [
    path("api/v1/create-project/", ProjectView.as_view(), name="create-project"),
    path("api/v1/get-projects/", ProjectView.as_view(), name="get-projects"),
    path("api/v1/get-project/<str:id>", ProjectView.as_view(), name="get-project"),
    path("api/v1/add-resource/", ProjectResources.as_view(), name="add-resource"),
]
