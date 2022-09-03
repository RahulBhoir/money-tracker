from django.http import HttpResponse


from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
def home(request):
    return HttpResponse("Home page")


class SalaryViewset(ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.get("amount")
        print("this is data", data)

        return Response(serializers.data, status=HTTP_201_CREATED)


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
