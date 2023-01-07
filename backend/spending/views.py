from math import trunc
import datetime
from multiprocessing import connection

from dateutil.relativedelta import relativedelta
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Spending
from .serializers import SpendingGetSerializer, SpendingPostSerializer, SpendingGettoalcostSerializer


# Create your views here.

@api_view(['GET'])  # B-1 해당 유저 지출 내역 조회
def getSpendingdatas(request, user_id):
    datas = Spending.objects.filter(user_id=user_id)  # 앞의 user_id Spending 테이블의 user_id 칼럼 의미, 뒤 user_id는 요청 값으로 전달하는 user_id 의미
    serializer = SpendingGetSerializer(datas, many=True)
    return Response(serializer.data)



@api_view(['POST'])  # B-2 지출 등록폼 입력 후 DB에 저장
def postSendingdata(request):
    reqData = request.data
    serializer = SpendingPostSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT']) # B-3 지출 내역 수정
def putSendingdata(request, spending_id):
    reqData = request.data          #reqData는 내가 수정을 원해서 서버에 전달하는 json데이터를 의미
    data = Spending.objects.get(spending_id=spending_id)            #앞의 spending_id는 Spending 테이블의 칼럼, 뒤의 spending_id는 요청 값으로 전달하는 spending_id 의미
    serializer= SpendingPostSerializer(instance=data, data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])  # D-1 용도별 지출 비율
def get_spending_rate_by_purpose(request, user_id):
    all_querySet = Spending.objects.filter(user_id=user_id)
    all_count = all_querySet.count()  # 전체 개수 구하기

    food_querySet = Spending.objects.filter(purpose="식사")
    food_count = food_querySet.count()  # 식비 개수

    transportation_querySet = Spending.objects.filter(purpose="교통/차량")
    transportation_count = transportation_querySet.count()  # 교통비 개수

    alcohol_querySet = Spending.objects.filter(purpose="술/유흥")
    alcohol_count = alcohol_querySet.count()  # 쇼핑 개수

    mobile_querySet = Spending.objects.filter(purpose="주거/통신")
    mobile_count = mobile_querySet.count()  # 쇼핑 개수

    beauty_querySet = Spending.objects.filter(purpose="뷰티/미용")
    beauty_count = beauty_querySet.count()  # 쇼핑 개수

    food_rate = trunc((food_count / all_count) * 100)
    transportation_rate = trunc((transportation_count / all_count) * 100)
    alcohol_rate = trunc((alcohol_count / all_count) * 100)
    mobile_rate = trunc((mobile_count / all_count) * 100)
    beauty_rate = trunc((beauty_count / all_count) * 100)

    return JsonResponse({'food_rate': food_rate, 'transportation_rate': transportation_rate,
                         'alcohol_rate': alcohol_rate, 'mobile_rate': mobile_rate,
                         'beauty_rate': beauty_rate}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])  # D-2 금월 지출 조회
def get_spending_this_month(request, user_id):
    this_month = datetime.datetime.now().month
    this_month_spending = Spending.objects.filter(when__month=this_month)

    total_spending = 0

    for i in this_month_spending:
        total_spending += i.cost

    return JsonResponse({'total_spending': int(total_spending)}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])  # D-3 한 달 전 지출 비교
def get_comparison_last_month(request, user_id):
    this_month = datetime.datetime.now()
    last_month = this_month - relativedelta(months=1)

    this_month_spending = Spending.objects.filter(when__month=this_month.month)
    total_this_month_spending = 0
    for i in this_month_spending:
        total_this_month_spending += i.cost

    last_month_spending = Spending.objects.filter(when__month=last_month.month)
    total_last_month_spending = 0
    for i in last_month_spending:
        total_last_month_spending += i.cost

    comparison_total_spending = total_this_month_spending - total_last_month_spending

    return JsonResponse({'comparison_total_spending': int(comparison_total_spending)}, safe=False,
                        status=status.HTTP_200_OK)


@api_view(['GET'])  # D-5 3개월 전 지출 총합
def get_three_month_ago_spending(request, user_id):

    three_month_ago = datetime.datetime.now() - relativedelta(months=3)

    three_month_ago_spending = Spending.objects.filter(when__month=three_month_ago.month)
    total_three_month_ago_spending = 0
    for i in three_month_ago_spending:
        total_three_month_ago_spending += i.cost

    return JsonResponse({'total_three_month_ago_spending': int(total_three_month_ago_spending)}, safe=False,
                        status=status.HTTP_200_OK)
