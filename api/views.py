from django.shortcuts import render
from .models import Userdetail, Activity
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def get(request):
    us = Userdetail.objects.all()
    us_s = []

    act_s = []

    for i in us:
        lst = []
        if i.userid in Activity.objects.all().values_list("userid", flat=True):
            act = Activity.objects.filter(userid=i.userid)
            for j in act:
                lst.append(
                    {
                    'start_time': j.start_time,
                    'end_time': j.end_time,
                    })
            us_s.append({
                'userid': i.userid,
                'real_name' : i.real_name,
                'tz' : str(i.tz),
                'activity' : lst
                })


    data = {
        'Member' : us_s
    }
    return  JsonResponse(data)

