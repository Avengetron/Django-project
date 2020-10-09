from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cal(request):
    return render(request, 'indexxx.html')

def add(request):

    res = int(request.POST['num1']) + int(request.POST["num2"])

    return render(request, 'result.html',{'result':res})
