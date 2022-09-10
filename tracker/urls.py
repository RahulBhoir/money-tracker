from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"income", IncomeViewset, basename="income")

urlpatterns = [
    path("api/", include(router.urls)),
    path("home", home, name="home"),
    path("tag_list", TagsViewset.as_view(), name="tag_list"),
    path("category_list", CategoryViewset.as_view(), name="category_list"),
    path("spendtype_list", SpendTypeViewset.as_view(), name="spend_type_list"),
    path("api/spend", SpendViewset.as_view(), name="daily_spend"),
    path("api/spend/<int:pk>/", SpendViewset.as_view(), name="daily_spend"),
]
