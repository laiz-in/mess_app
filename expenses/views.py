from django.shortcuts import render

from .models import Expense


def home(request):
    return render(request, 'home.html')

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    return render(request, 'home.html')

def view_reports(request):
    return render(request, 'home.html')
