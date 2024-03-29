from django.shortcuts import render, redirect

from expenses_tracker.expense.forms import ExpensesAddForm, ExpensesEditForm, ExpensesDeleteForm
from expenses_tracker.expense.models import Expense


def create_expense(request):
    form = ExpensesAddForm(request.GET)
    if request.method == 'POST':
        form = ExpensesAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }
    return render(request, 'expense/expense-create.html', context=context)


def edit_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()
    form = ExpensesEditForm(instance=expense)
    if request.method == 'POST':
        form = ExpensesAddForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }
    return render(request, 'expense/expense-edit.html', context=context)


def delete_expense(request, pk):
    expense = Expense.objects.filter(pk=pk).get()
    form = ExpensesDeleteForm(instance=expense)
    if request.method == 'POST':
        expense.delete()
        return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'expense/expense-delete.html', context=context)

