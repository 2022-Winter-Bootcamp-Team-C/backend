from rest_framework.serializers import ModelSerializer
from .models import Spending
from .models import User




class SpendingGetSerializer(ModelSerializer):
    class Meta:
        model = Spending
        fields = ['spending_id', 'when', 'cost', 'purpose', 'memo']


class SpendingPostSerializer(ModelSerializer):
    class Meta:
        model = Spending
        fields = '__all__'


class SpendingGettoalcostSerializer(ModelSerializer):
    class Meta:
        model = Spending
        fields = ['cost']

class spending_delete_serializer(ModelSerializer):
    class Meta:
        model = Spending
        fields = ['is_deleted']
