from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import taskserializers 
from .models import *
# Create your views here.


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'list':'/task-list/',
        'detail view':'/task_detail/<str:pk>/',
        'create':'/task-create/',
        'update ':'/task_update/<str:pk>/',
        'delete':'/task_delete/<str:pk>/',
        }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = task.objects.all()
    serializer = taskserializers(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    tasks = task.objects.get(id=pk)
    serializer = taskserializers(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskpost(request):
    serializer = taskserializers(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(['GET','POST'])
def taskupdate(request,pk):
    tasks = task.objects.get(id=pk)
    serializer = taskserializers(instance=tasks,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    tasks = task.objects.get(id=pk)
    tasks.delete()

    return Response('item sucessfully deleted')

