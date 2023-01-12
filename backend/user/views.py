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



# @api_view(['POST'])
# def join(request):  # 회원가입
#     email = request.data['email']
#     password = request.data['password']
#     new_user = create_user(email, password)
#     data = UserSignupResponse(new_user, many=False).data
#     return JsonResponse(data, status=201)
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

# @api_view(['POST'])
# def login_user(request):
#     user_email=request.data.get('email', "")
#     user_pw=request.data.get('password', "")
#     user = User.objects.filter(email=user_email).first()
#     if user is None:
#         return Response({'msg': "해당 ID의 사용자가 없습니다."})
#     if check_password(user_pw, user.password):
#         return Response({'msg': "로그인 성공", 'user_id': user.user_id})
#     else:
#         return Response({'msg': "로그인 실패. 패스워드 불일치"})
#
#
#
#
# @api_view(['POST'])
# def regis_user(request):
#     user_email = request.data.get('email', "")
#     user_pw = request.data.get('password', "")
#     user_pw_crypted = make_password(user_pw)  # 암호화
#     if User.objects.filter(email=user_email).exists():
#         user=User.objects.filter(email=user_email).first()
#         data = dict(
#             msg="이미 존재하는 아이디입니다.",
#             email=user.email,
#             password=user.password
#         )
#         return Response(data)
#
#     User.objects.create(email=user_email, password=user_pw_crypted)
#     data=dict(
#         email=user_email,
#         password=user_pw_crypted
#     )
#
#     return Response(data=data)
