from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# Create your models here.
class SpendType(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class CategoryType(models.Model):
    # value = debit, credit
    name = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    category_type = models.ForeignKey(CategoryType, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class DailySpend(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    amount = models.FloatField(default=0.0,
                               max_length=10, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False, verbose_name="spend_date")
    time = models.TimeField(blank=False, null=False, verbose_name="spend_time")
    spend_type = models.ForeignKey(SpendType, on_delete=models.RESTRICT)
    tag = models.ForeignKey(Tag, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        display_name = str(self.user.id) + self.name
        return display_name

    def save(self):
        if not self.date:
            self.date = datetime.now().date()
        if not self.time:
            self.time = datetime.now().time()
        if not self.tag:
            self.tag = Tag.objects.get(id=1)
        if not self.spend_type:
            self.spend_type = SpendType.objects.get(id=1)
        if not self.category:
            self.category = Category.objects.get(id=1)


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0, blank=False, null=False)
    total_remaining_amt = models.IntegerField(default=0,
                                              blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    date = models.DateField(default=datetime.now().date(),
                            blank=False, null=False, verbose_name="income_date",)
    time = models.TimeField(default=datetime.now().time(),
                            blank=False, null=False, verbose_name="income_time",)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} {self.created.date()}"

    def salary_split(self):
        split_dic = dict()
        if self.amount > 0:
            split_dic = {
                "need": self.amount * 0.5,
                "want": self.amount * 0.3,
                "saving": self.amount * 0.2,
            }
        else:
            split_dic = {"error": "Salary is zero"}
        return split_dic
