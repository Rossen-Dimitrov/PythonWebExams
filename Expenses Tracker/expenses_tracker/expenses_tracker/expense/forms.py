from django import forms

from expenses_tracker.expense.models import Expense


class ExpensesBaseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'expense_image', 'price']

        labels = {
            'expense_image': 'Link To Image',
        }


class ExpensesAddForm(ExpensesBaseForm):
    pass


class ExpensesEditForm(ExpensesBaseForm):
    pass


class ExpensesDeleteForm(ExpensesBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
