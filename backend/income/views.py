import json
from math import trunc
import datetime
from dateutil.relativedelta import relativedelta
from multiprocessing import connection

from django.core import serializers
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta

from .models import Income
from user.models import User

from .serializers import get_income_serializer, post_income_serializer, put_income_serializer


@api_view(['GET'])  # C-1 해당 유저 수입 내역 조회
def get_income_list(request, user_id):
    try:
        bool(User.objects.get(user_id=user_id))
    except:
        return JsonResponse({'message': "존재하지 않는 user"}, safe=False, status=status.HTTP_404_NOT_FOUND)

    datas = Income.objects.filter(user_id=user_id, is_deleted=False)

    if len(datas) == 0:
        return JsonResponse({'message': "수입 내역이 없습니다."}, safe=False, status=status.HTTP_404_NOT_FOUND)

    serializer = get_income_serializer(datas, many=True)
    total_cost = 0
    for i in datas:
        total_cost += i.cost
    return JsonResponse({'user_id,': user_id, 'income_list': serializer.data, 'total_price': total_cost})


@api_view(['POST'])  # C-2 해당 유저 수입 등록
def post_new_income(request):
    if request.data['cost'] > 9999999:
        return JsonResponse({'memssage': "금액은 최대 9,999,999원입니다."}
                            , safe=False, status=status.HTTP_400_BAD_REQUEST)
    serializer = post_income_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])  # C-3,4 해당 유저 수입 수정, 삭제
def put_new_Income(request, id):

    data = Income.objects.get(id=id)  # 앞의 id는 Spending 테이블의 칼럼, 뒤의 id는 요청 값으로 전달하는 id 의미
    if data.is_deleted:
        return JsonResponse({'memssage': "삭제된 수입 내역입니다."}
                            , safe=False, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        reqData = request.data  # reqData는 내가 수정을 원해서 서버에 전달하는 json데이터를 의미
        serializer = put_income_serializer(instance=data, data=reqData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        delete_data = Income.objects.filter(id=id, is_deleted=False)
        delete_data.update(is_deleted=True)
        return Response(status=status.HTTP_202_ACCEPTED)

    # if request.method == 'PUT':
    #     data = request.data
    #     update_data = Income.objects.get(id=id)
    #     serializer = PutIncomeSerializer(instance=update_data, data=data)
    #     if serializer.is_valid():
    #         serializer.save
    #         return Response(serializer.data, status=200)
    #     return Response(serializer.errors, status=400)
    # elif request.method == 'DELETE':
    #     delete_data = Income.objects.filter(id=id, is_deleted=False)
    #     delete_data.update(is_deleted=True)
    #     return Response(status=204)

    # input_data = Income.objects.get(id=id)
    # if input_data.is_deleted:
    #     return JsonResponse({'memssage': "삭제된 수입 내역입니다."}
    #                         , safe=False, status=status.HTTP_400_BAD_REQUEST)
    #
    # if request.method == 'PUT':
    #     data = request.data
    #     update_data = Income.objects.get(id=id)
    #     serializer = PutIncomeSerializer(instance=update_data, data=data)
    #
    #     if serializer.is_valid():
    #         serializer.save
    #         return Response(serializer.data, status=200)
    #     return Response(serializer.errors, status=400)
    #
    # elif request.method == 'DELETE':
    #     delete_data = Income.objects.filter(id=id, is_deleted=False)
    #     delete_data.update(is_deleted=True)
    #     return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])  # D-4 3개월 전 수입 총합
def get_three_month_ago_income(request, user_id):
    three_month_ago = datetime.datetime.now() - relativedelta(months=3)

    three_month_ago_income = Income.objects.filter(when__month=three_month_ago.month)
    total_three_month_ago_income = 0
    for i in three_month_ago_income:
        total_three_month_ago_income += i.cost

    return JsonResponse({'total_three_month_ago_income': int(total_three_month_ago_income)}, safe=False,
                        status=status.HTTP_200_OK)
