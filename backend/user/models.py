import uuid

from django.db import models


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)  # PK
    email = models.EmailField(max_length=200, default='')
    password = models.BinaryField(max_length=60, default=b'')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)
    is_deleted = models.BinaryField(default=False)

    class Meta:
        db_table = 'user'
