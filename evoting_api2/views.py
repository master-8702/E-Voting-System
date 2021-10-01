from django.shortcuts import render
from django.http import JsonResponse
from election.models import Regions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegionSerializer


@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Regions':'/regions_list/',
        'Detail View':'task-detail/<int:id>/',
        'Create':'region-create/',
        'Update':'region-update/<int:id>',
        'Delete':'region-delete/<int:id>',
    }

    return Response(api_urls)


@api_view(['GET'])
def regionList(request):
    regions =Regions.objects.all()
    serializer = RegionSerializer(regions, many =True)
    return Response(serializer.data)



@api_view(['GET'])
def regionDetail(request, id):
    regions =Regions.objects.get(pk=id)
    serializer = RegionSerializer(regions, many =False)
    return Response(serializer.data)


@api_view(['POST'])
def regionCreate(request):
    serializer = RegionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def regionUpdate(request, id):
    region =Regions.objects.get(pk=id)
    serializer = RegionSerializer(instance = region, data= request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def regionDelete(request, id):
    regions =Regions.objects.get(pk=id)
    regions.delete()
    return Response("Entity Successfully Deleted!")

