
from django.shortcuts import render
from api_basic.models import Employeemodel
from api_basic.serialize import Employeeserialize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render
import requests



# Create your views here.

@api_view(["POST"])
def saveemp(request):
    if request.method=="POST":
        saveserialize = Employeeserialize(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data,status = status.HTTP_201_CREATED)
            



def insertemp(request):
    if request.method=="POST":
        empname = request.POST.get("empname") 
        email = request.POST.get("email") 
        salary = request.POST.get("salary")
        data = {'empname':empname,'email':email,'salary':salary}
        headers = {'Content-Type': 'application/json'}
        read = requests.post('http://127.0.0.1:8000/insertempapi',json=data,headers=headers)
        return render(request,'insert.html')
    
    else:
        return render(request,'insert.html')

       