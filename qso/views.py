from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from .models import Qso
from .api.serializers import QsoSerializer

@api_view(["GET"])
def ApiOverview(request):
    api_urls = {
        "all_qso": "/",
        "Add": "/create",
        "Update": "/update/pk",
        "Delete": "/qso/pk/delete"
    }
    return Response(api_urls)


@api_view(['POST'])
def add_qso(request):
    qso = QsoSerializer(data=request.data)
    if Qso.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This entry already exists")
    if qso.is_valid():
        qso.save()
        return Response(qso.data)
    return Response(status=status.HTTP_404_NOT_FOUND)