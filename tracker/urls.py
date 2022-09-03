from xml.etree.ElementInclude import include
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r"salary", SalaryViewset, basename="income")

urlpatterns = [
    # path("api/", include(router.urls)),
    path("home", home, name="home"),
    path("tag_list", TagsViewset.as_view(), name="tag_list"),
    path("category_list", CategoryViewset.as_view(), name="category_list"),
    path("spendtype_list", SpendTypeViewset.as_view(), name="spend_type_list"),
    path("income", SalaryViewset, name="income"),
]
