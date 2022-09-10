from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from .utils import get_total_remaining_amount

from datetime import date, datetime

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


class SpendViewset:
    pass


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
