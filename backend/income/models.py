import uuid
from user.models import User
from django.db import models



class Income(models.Model):
    income_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)  # PK
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(decimal_places=0, max_digits=7, null=False)
    date = models.DateTimeField(auto_now=True, blank=True)
    memo = models.CharField(max_length=20)
    purpose = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BinaryField(default=b'\x08')

    class Meta:
        db_table = 'income'
