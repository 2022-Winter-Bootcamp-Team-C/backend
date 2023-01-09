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
from .serializers import GetIncomeSerializer, PostIncomeSerializer, PutIncomeSerializer



@api_view(['GET'])  # C-1 해당 유저 수입 내역 조회
def getincomeList(request, user_id):
    datas = Income.objects.filter(user_id=user_id, is_deleted=False)
    serializer = GetIncomeSerializer(datas, many=True)
    total_cost = 0
    for i in datas:
        total_cost += i.cost
    return JsonResponse({'user_id,': user_id, 'income_list': serializer.data, 'total_price': total_cost})

@api_view(['POST']) # C-2 해당 유저 수입 등록
def postnewIncome(request):
        serializer = PostIncomeSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['PUT', 'DELETE']) # C-3,4 해당 유저 수입 수정, 삭제
def putnewIncome(request, income_id):
    if request.method == 'PUT':
        data = request.data
        update_data = Income.objects.get(income_id=income_id)
        serializer = PutIncomeSerializer(instance=update_data, data=data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        delete_data = Income.objects.filter(income_id=income_id, is_deleted=False)
        delete_data.update(is_deleted=True)
        return Response(status=204)

@api_view(['GET'])  # D-4 3개월 전 수입 총합
def get_three_month_ago_income(request, user_id):

    three_month_ago = datetime.datetime.now() - relativedelta(months=3)

    three_month_ago_income = Income.objects.filter(when__month=three_month_ago.month)
    total_three_month_ago_income = 0
    for i in three_month_ago_income:
        total_three_month_ago_income += i.cost

    return JsonResponse({'total_three_month_ago_income': int(total_three_month_ago_income)}, safe=False,
                        status=status.HTTP_200_OK)
