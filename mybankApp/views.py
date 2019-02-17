from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .MyForm import myForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import bankSerializer
from .models import Bank
from django.urls import reverse

# Create your views here.

def bankView(request):
    model = Bank
    return render(request, 'home.html')


class MyBankGetByIFSC (APIView):


    def get(self, request):
        flag = 0
        if request.method == 'GET':
            c = request.GET['ifsc']
            a = Bank.objects.all()
            if c != '' :
                print("Hello : ",c)
                for i in range(len(a)):
                    if a[i].ifsc.lower() == c.lower() :
                        flag = 1
                        print("Run1")
                        serializer = bankSerializer(a[i])
                        return Response(serializer.data)
                if flag == 0:
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')


class MyBGetByCityName (APIView):

    def get(self, request):
        flag = 0
        bList=[]
        if request.method == 'GET':
            # c = request.GET['ifsc']
            bName = request.GET['bName']
            bCity = request.GET['bCity']
            print(bName)
            print(bCity)
            a = Bank.objects.all()
            if bName != '' and bCity != '':
                for i in range(len(a)):
                    if a[i].bank_name.lower() == bName.lower() and a[i].city.lower() == bCity.lower():
                        flag=1
                        bList.append(a[i])
                
                if flag == 0:
                    return HttpResponseRedirect('/')
                else:
                    serializer = bankSerializer(bList, many =True)
                    return Response(serializer.data)
            else:
                return HttpResponseRedirect('/')       
                  
