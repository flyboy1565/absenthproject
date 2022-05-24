from os import stat
from django.shortcuts import get_object_or_404, render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from .models import Qso
from .api.serializers import QsoSerializer

# api documentation for users
@api_view(["GET"])
def ApiOverview(request):
    api_urls = {
        "all_qso": "/",
        "Add": "/create",
        "Update": "/update/pk",
        "Delete": "/qso/pk/delete"
    }
    return Response(api_urls)


# create
@api_view(['POST'])
def add_qso(request):
    qso = QsoSerializer(data=request.data)
    if Qso.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This entry already exists")
    if qso.is_valid():
        qso.save()
        return Response(qso.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


# list
@api_view(['GET'])
def list_qso(request):
    if request.query_params:
        qsos = Qso.objects.filter(**request.query_params.dict())
    else:
        qsos = Qso.objects.all()
    if qsos:
        data = QsoSerializer(qsos)
        return Response(data)
    return Response(status=status.HTTP_404_NOT_FOUND)


# update 
@api_view(['POST'])
def update_qso(request, pk):
    qso = Qso.objects.get(pk=pk)
    data = QsoSerializer(instance=qso,data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_qso(request, pk):
    qso = get_object_or_404(Qso, pk=pk)
    qso.delete()
    return Response(status.HTTP_202_ACCEPTED)