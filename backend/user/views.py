from rest_framework import viewsets

from .serializers import userSerializer

from .models import User


class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = userSerializer
