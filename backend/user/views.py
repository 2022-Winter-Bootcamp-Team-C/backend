from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import User
from .serializers import UserSerializer
from .serializers import UserSignupResponse
from .service import create_user


@api_view(['POST'])
def join(request):
    email = request.data['email']
    password = request.data['password']
    new_user = create_user(email, password)
    data = UserSignupResponse(new_user, many=False).data
    return JsonResponse(data, status=201)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        email = data['email']
        obj = User.objects.get(name=email)

        if data['password'] == obj.password:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
