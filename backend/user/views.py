import bcrypt as bcrypt
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.status import HTTP_200_OK

from .models import User
from .serializers import UserSerializer
from .serializers import UserSignupResponse
from .service import create_user


@api_view(['POST'])
def join(request):  # 회원가입
    email = request.data['email']
    password = request.data['password']
    new_user = create_user(email, password)
    data = UserSignupResponse(new_user, many=False).data
    return JsonResponse(data, status=201)
#
#
# @api_view(['POST'])
# def login(request):
#     input_email = request.data['email']
#     input_password = request.data['password']
#
#     user_data = User.objects.get(email=input_email)
#
#     if user_data:
#         if user_data.password == input_password:
#             return JsonResponse({'email': input_email, 'password': input_password}, status=status.HTTP_200_OK,
#                                 safe=False)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     else:
#         return Response(status==status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    try:
        user_data = User.objects.get(email=request.data['email'])
        if user_data.password == request.data['password']:
            return JsonResponse({'user_id': user_data.user_id}, safe=False, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
