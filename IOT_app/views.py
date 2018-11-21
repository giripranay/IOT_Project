from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import DataForm
import requests
from .models import Bin1
from django.utils.dateparse import parse_datetime


def index(request):
    values=Bin1.objects.all()
    latest=Bin1.objects.all().order_by('-id')[0]
    count = len(values)
    URL="https://io.adafruit.com/api/v2/giripranay/feeds/bin1/data?X-AIO-Key=a68f2ef379d4470780176f536af0f462"
    r = requests.get(url=URL)
    new=r.json()
    count2=len(new)
    if(count!=count2):
        for i in new[0:count2-count]:
            temp_date = parse_datetime(i['created_at'])
            obj=Bin1(value=i['value'],date=temp_date)
            obj.save()

    data={'lis':new,'count':count,'count2':count2,'values':values,'latest':latest}

    return render(request,'IOT_app/index.html',data)

def data(request):
    if request.method =='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            newitem=form.save(commit=False)
            newitem.save()
            return redirect('index')
    else:
        form=DataForm()
    return render(request,'IOT_app/data.html',{'form':form})


def database(request):
    bills_list=Bin1.objects.all()
    data={'lis':bills_list,}
    return render(request,'IOT_app/database.html',data)
