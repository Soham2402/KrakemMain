from django.contrib.auth.models import User
from django.db import models
from project.constants import ProcessingConstants, ResourceTypeConstants
from project.constants import ResourceProcessingConstants as ResProCons
from uuid import uuid4


# Create your models here.
class Project(models.Model):
    project_id = models.UUIDField(
        primary_key=True, unique=True, default=uuid4, editable=False
    )
    name = models.CharField(max_length=36, null=False)
    description = models.TextField(null=False)
    owner = models.ForeignKey(to=User, null=False, on_delete=models.PROTECT)
    processing_state = models.IntegerField(
        choices=ProcessingConstants.model_choices, default=ProcessingConstants.PENDING
    )

    is_active = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now=True)
    deleted_on = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.project_id}_{self.owner.id}"

    class Meta:
        db_table = "project"


class Resource(models.Model):
    resource_type = models.IntegerField(
        default=ResourceTypeConstants.OTHER, choices=ResourceTypeConstants.model_choices
    )
    title = models.CharField(max_length=36, null=True)

    owner = models.ForeignKey(to=User, null=False, on_delete=models.PROTECT)
    project = models.ForeignKey(to=Project, null=False, on_delete=models.CASCADE)

    data = models.FileField(null=False, upload_to="resources/")
    processing_state = models.IntegerField(
        choices=ResProCons.model_choices, default=ResProCons.PENDING
    )

    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project.project_id}_{self.pk}"

    class Meta:
        db_table = "resource"


class ResourceChunks(models.Model):
    vector_id = models.CharField(null=False, max_length=255)
    data = models.FileField(null=False, upload_to="chunks/")
    resource = models.ForeignKey(to=Resource, null=False, on_delete=models.CASCADE)
    vectorising_state = models.IntegerField(
        choices=ProcessingConstants.model_choices, default=ProcessingConstants.PENDING
    )

    created_on = models.DateField(auto_now=True)
    completed_on = models.DateField()

    class Meta:
        db_table = "resource_chunk"
