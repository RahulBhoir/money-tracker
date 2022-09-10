from django.http import HttpResponse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from .utils import get_total_remaining_amount

from datetime import date, datetime

User = get_user_model()

# Create your views here.


def home(request):
    return HttpResponse("Home page")


class IncomeViewset(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        income_amount = data.get("income_amount", 0)
        income_type = data.get("income_type", 1)
        income_date = data.get("income_date", date.today())
        income_time = data.get("income_time", datetime.now().time())

        income_data = {
            "user": user.id,
            "amount": income_amount,
            "category": income_type,
            "date": income_date,
            "time": income_time,
            "total_remaining_amt": get_total_remaining_amount(user_id=user.id, month=income_date.month)
        }

        serializer = IncomeSerializer(data=income_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpendViewset(APIView):
    queryset = DailySpend.objects.all()
    serializer_class = DailySpendSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        data = request.query_params
        month = data.get('month', datetime.now().month)
        self.queryset = self.queryset.filter(user=user, date__month=month)
        serializers = DailySpendSerializer(self.queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        spend_data = {
            'user': user.id,
            'name': data.get('name', ''),
            'amount': data.get('amount', 0),
            'category': data.get('category', 1),
            'tag': data.get('tag', 1),
            'spend_type': data.get('spend_type', 1),
            'date': data.get('date', date.today()),
            'time': data.get('time', datetime.now().time())
        }

        serializer = DailySpendSerializer(data=spend_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagsViewset(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class CategoryViewset(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SpendTypeViewset(ListAPIView):
    queryset = SpendType.objects.all()
    serializer_class = SpendTypeSerializer
