from math import trunc
import datetime
from dateutil.relativedelta import relativedelta
from multiprocessing import connection
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from dateutil.relativedelta import relativedelta

from .models import Income
from .serializers import GetIncomeSerializer, PostIncomeSerializer


@api_view(['GET'])
def get_income_list(request, user_id):
    datas = Income.objects.filter(user_id=user_id, is_deleted='0')
    serializer = GetIncomeSerializer(datas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_new_income(request):
    serializer = PostIncomeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])  # D-4 3개월 전 수입 총합
def get_three_month_ago_income(request, user_id):
    three_month_ago = datetime.datetime.now() - relativedelta(months=3)

    three_month_ago_income = Income.objects.filter(when__month=three_month_ago.month)
    total_three_month_ago_income = 0
    for i in three_month_ago_income:
        total_three_month_ago_income += i.cost

    return JsonResponse({'total_three_month_ago_income': int(total_three_month_ago_income)}, safe=False,
                        status=status.HTTP_200_OK)


@api_view(['GET'])  # D-2 금월 수입 조회
def get_income_this_month(request, user_id):
    this_month = datetime.datetime.now().month
    this_month_income = Income.objects.filter(user_id=user_id, when__month=this_month)

    total_income = 0

    for i in this_month_income:
        total_income += i.cost

    return JsonResponse({'total_income': int(total_income)}, safe=False, status=status.HTTP_200_OK)
