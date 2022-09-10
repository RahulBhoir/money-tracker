from .models import DailySpend, Income


def get_total_remaining_amount(user_id, month):

    total_spend = DailySpend.objects.filter(
        user_id=user_id, date__month=month).values_list("amount", flat=True)
    total_income = Income.objects.filter(
        user_id=user_id, date__month=month).values_list("amount", flat=True)

    if len(total_income) == 0:
        total_income = 0
    else:
        total_income = sum(total_income)

    if len(total_spend) == 0:
        total_spend = 0
    else:
        total_spend = sum(total_spend)

    return total_income - total_spend
