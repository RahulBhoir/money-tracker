from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tag)
admin.site.register(CategoryType)
admin.site.register(Category)
admin.site.register(SpendType)
admin.site.register(Income)
admin.site.register(DailySpend)