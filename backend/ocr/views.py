import requests
import uuid
import time
import base64
import json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.settings import OCR_SECRET_KEY, OCR_API_URL


@api_view(['POST'])
def ocr_receipt(request):
    api_url = OCR_API_URL
    secret_key = OCR_SECRET_KEY
    image_file = request.data['url']

    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo'
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = {'message': json.dumps(request_json).encode('UTF-8')}
    files = [
        ('file', open(image_file, 'rb'))
    ]
    headers = {
        'X-OCR-SECRET': secret_key
    }

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
    a = json.loads(response.text)
    print(a['images']['receipt']['result']['paymentInfo']['date']['text'])
    print(a['images']['receipt']['result']['totalPrice']['price']['text'])

    # print(json.loads(response.text))
    return Response(json.loads(response.text))

    # print(response.text.encode('utf8'))

    # spec = json.loads(response.text)
    # print(spec['images'])
    # print(payload)
    # print(response.text.encode('utf8'))

    # return Response(spec["addresses"])

    # with open(request.data['url'], "rb") as f:
    #     img = base64.b64encode(f.read())
    #
    # URL = "https://hudfkr1v5p.apigw.ntruss.com/custom/v1/19970/5306aa9f52013ed8693a9db38f37b929f578eb212f4c63f670641facc747471e/general"
    # KEY = "aEhuQlZ4WFhuUFNFZkpXY2NYUUhqb2lQcHhQWW1EWkI="
    #
    # headers = {
    #     "Content-Type": "application/json",
    #     "X-OCR-SECRET": KEY
    # }
    #
    # data = {
    #     "version": "V2",
    #     "requestId": "testId",  # 요청을 구분하기 위한 ID, 사용자가 정의
    #     "timestamp": int(round(time.time() * 1000)),
    #     "images": [
    #         {
    #             "name": "result",
    #             "format": "png",
    #             "data": img.decode('utf-8'),
    #             # 'templateIds': [22321]
    #         }
    #     ]
    # }
    # data = json.dumps(data)
    # response = requests.post(URL, data=data, headers=headers)
    # return Response(json.loads(response.text))
