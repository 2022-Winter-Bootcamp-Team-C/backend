from multiprocessing import connection

from django.db.models import Sum
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Spending
from .serializers import SpendingGetSerializer, SpendingPostSerializer, SpendingGettoalcostSerializer


# Create your views here.

@api_view(['GET']) #B-1 해당 유저 지출 내역 조회
def getSpendingdatas(request, user_id):
    datas=Spending.objects.filter(user_id=user_id) #앞의 user_id Spending 테이블의 user_id 칼럼 의미, 뒤 user_id는 요청 값으로 전달하는 user_id 의미
    serializer = SpendingGetSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['POST']) #B-2 지출 등록폼 입력 후 DB에 저장
def postSendingdata(request):
    reqData = request.data
    serializer = SpendingPostSerializer(data=reqData)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def totalSpendingcost(request, user_id):
    try:
        cursor = connection.cursor()

        strSql = "SELECT cost FROM spending"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        books = []
        for data in datas:
            row = {'code': data[0],
                   'name': data[1],
                   'author': data[2]}

            books.append(row)

    except:
        connection.rollback()
        print("Failed selecting in BookListView")

    return render(request, 'book_list.html', {'books': books})