from django.db.models import fields
from rest_framework import serializers
from ..models import Qso

class QsoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qso
        fleids = "__all__"
