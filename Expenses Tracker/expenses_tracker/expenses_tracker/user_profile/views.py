from django.shortcuts import render, redirect

from expenses_tracker.expense.models import Expense
from expenses_tracker.user_profile.forms import UserProfileAddForm, UserProfileEditForm, UserProfileDeleteForm
from expenses_tracker.utils import get_user_profile


def details_profile(request):
    profile = get_user_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'bought_count': len(expenses),
        'budget_left': budget_left
    }
    return render(request, 'profile/profile.html', context=context)


def add_profile(request):
    form = UserProfileAddForm
    if request.method == 'POST':
        form = UserProfileAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form
    }

    return render(request, 'core/home-no-profile.html', context=context)


def edit_profile(request):
    user = get_user_profile()
    form = UserProfileEditForm(instance=user)
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context=context)


def delete_profile(request):
    user = get_user_profile()
    if request.method == 'POST':
        user.delete()
        Expense.objects.all().delete()
        return redirect('home page')

    return render(request, 'profile/profile-delete.html')
