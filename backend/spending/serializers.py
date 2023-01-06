from rest_framework.serializers import ModelSerializer
from .models import Spending


class SpendingGetSerializer(ModelSerializer):
    class Meta:
        model = Spending
        fields = ['spending_id', 'date', 'cost', 'purpose', 'memo']

class SpendingPostSerializer(ModelSerializer):
    class Meta:
        model = Spending
        fields = '__all__'
class SpendingGettoalcostSerializer(ModelSerializer):
    class Meta:
        model = Spending
        fields =['cost']