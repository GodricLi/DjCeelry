from django.shortcuts import render
from django.http import JsonResponse
from celeryapp.tasks import Course


def course(request, *args, **kwargs):
    # 执行异步任务
    print("start course...")
    Course.delay()
    print("end course...")
    return JsonResponse({'result': 'ok'})
