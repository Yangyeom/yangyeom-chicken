from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse
from decouple import config
from .models import Payment
from django.contrib.auth import get_user_model


KEY = config('KAKAO_API_KEY')
API_HOST = 'https://kapi.kakao.com'
headers = {'Authorization': f'KakaoAK {KEY}'}
tid = 0
user = -1

def req(path, query, data={}):
    url = API_HOST + path

    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    return requests.post(url, headers=headers, data=data).json()


# Create your views here.
# 주문 정보 확인
def index(request):
    return render(request, 'payments/index.html')


# 결제 요청
def pay(request, user_id):
    # order example
    global tid
    global user
    user = user_id

    params = {
        'cid': 'TC0ONETIME',
        'partner_order_id': '19283432',
        'partner_user_id': user,
        'item_name': 'Coke 영화추천서비스이용 결제',
        'item_code': 'a123',
        'quantity': 1,
        'total_amount': 4900,
        'vat_amount': 490,
        'tax_free_amount': 0,
        'approval_url': 'http://127.0.0.1:8000/payments/success/',
        'fail_url': 'http://127.0.0.1:8000/payments/fail/',
        'cancel_url': 'http://127.0.0.1:8000/payments/cancel/',
    }
    data = req('/v1/payment/ready', '', params)
    tid = data['tid']

    # return redirect(data['next_redirect_pc_url'])
    data = json.dumps(data)
    return HttpResponse(data, status=201)


# 결제 성공(승인)
def success(request):
    global tid
    global user

    params = {
        'cid': 'TC0ONETIME',
        'tid': tid,
        'partner_order_id': '19283432',
        'partner_user_id': user,
        'pg_token': request.GET.get('pg_token'),
    }

    data = req('/v1/payment/approve', '', params)

    User = get_user_model().objects.get(id=user)
    User.paid = True
    User.save()
    payment = Payment(aid=data['aid'], tid=data['tid'], payment_method_type=data['payment_method_type'],
                item_name=data['item_name'], item_code=['item_code'], amount=data['amount']['total'],
                created_at=data['created_at'], approved_at=data['approved_at'], user=User)
    payment.save()

    return render(request, 'payments/success.html')