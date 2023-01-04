
import uuid

from django.db import models


class Member(models.Model):
    member_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)  # PK
    name = models.CharField(max_length=50, default='')
    password = models.BinaryField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, blank=True)
    is_deleted = models.BinaryField(default=b'\x08')

    class Meta:
        db_table = 'user'
