from rest_framework.serializers import ModelSerializer
from api.models import Unit, Visit


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        exclude = ["worker"]


class VisitSerializer(ModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"
