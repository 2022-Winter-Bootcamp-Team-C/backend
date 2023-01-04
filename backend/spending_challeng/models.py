import uuid

from django.db import models

from member.models import Member


class Spending_challenge(models.Model):
    challenge_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)  # PK
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    budget = models.DecimalField(decimal_places=0, max_digits=8, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BinaryField(default=b'\x08')

    class Meta:
        db_table = 'spending_challenge'

