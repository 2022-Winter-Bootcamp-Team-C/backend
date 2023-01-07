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


@api_view(['GET'])  # D-4 3개월 전 수입 총합
def get_three_month_ago_income(request, user_id):

    three_month_ago = datetime.datetime.now() - relativedelta(months=3)

    three_month_ago_income = Income.objects.filter(when__month=three_month_ago.month)
    total_three_month_ago_income = 0
    for i in three_month_ago_income:
        total_three_month_ago_income += i.cost

    return JsonResponse({'total_three_month_ago_income': int(total_three_month_ago_income)}, safe=False,
                        status=status.HTTP_200_OK)
