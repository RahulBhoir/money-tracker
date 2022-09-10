from .models import *
from rest_framework import serializers


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = [
            "user", "amount", "category", "date", "time", "total_remaining_amt"
        ]


class DailySpendSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailySpend
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class SpendTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpendType
        fields = "__all__"
