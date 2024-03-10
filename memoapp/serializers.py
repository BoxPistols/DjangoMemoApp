from rest_framework import serializers
from .models import MemoModel


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoModel
        fields = ("id", "title", "memo")
