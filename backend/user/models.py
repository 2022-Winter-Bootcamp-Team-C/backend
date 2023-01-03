import uuid

from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)  # PK
    email = models.CharField(max_length=50)
    # email = models.EmailField(_('email address'), unique=False)
    password = models.BinaryField(max_length=60)
    # password = models.CharField(max_length=200, null=False)
    # salt = models.BinaryField(max_length=29)

    # BaseEntity
    created_at = models.DateTimeField(auto_now_add=True, null=False)
