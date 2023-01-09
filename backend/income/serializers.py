import uuid

from django.db.models import Sum
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Income
from user.models import User

class GetIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['income_id', 'cost', 'when', 'purpose', 'memo']

class PostIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['user', 'cost', 'when', 'purpose', 'memo']

class PutIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class DeleteSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ['is_deleted']


