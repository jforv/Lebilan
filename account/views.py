from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from account.models import Account
from account.serializers import AccountSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def account_list(request):
    if request.method =='GET':
        account = Account.objects.all()
        account_serializer = AccountSerializer(account, many=True)
        return JSONResponse(account_serializer.data)
    elif request.method == 'POST':
        account_data = JSONParser().parse(request)
        account_serializer = AccountSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JSONResponse(account_serializer.data,status=status.HTTP_201_CREATED)
        return JSONResponse(account_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def account_detail(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        account_serializer = AccountSerializer(account)
        return JSONResponse(account_serializer.data)

    elif request.method == 'PUT':
        account_data = JSONParser().parse(request)
        account_serializer = AccountSerializer(account, data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JSONResponse(account_serializer.data)
        return JSONResponse(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)



    
        
