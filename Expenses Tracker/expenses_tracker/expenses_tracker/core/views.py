from django.shortcuts import render

from expenses_tracker.expense.models import Expense
from expenses_tracker.user_profile.models import UserProfile
from expenses_tracker.user_profile.views import add_profile
from expenses_tracker.utils import get_user_profile


def home_page(request):
    if not get_user_profile():
        return add_profile(request)
    profile = get_user_profile()
    all_expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in all_expenses)

    context = {
        'profile': profile,
        'all_expenses': all_expenses,
        'budget_left': budget_left
    }

    return render(request, 'core/home-with-profile.html', context=context)


