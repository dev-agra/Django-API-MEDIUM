from django.db import models
import uuid

# Create your models here.
# abstract model which will hold model fields common to all the other applications in the project

class TimeStampedModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # this model's db not created but a base class for other models
        abstract = True
        ordering = ["-created_at", "-updated_at"]