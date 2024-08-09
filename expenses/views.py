import uuid

from django.db import connection
from django.shortcuts import redirect, render

from .models import Expense


def home(request):
    return render(request, 'home.html')

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        added_person = request.POST['added_person']
        added_amount = request.POST['added_amount']
        added_date = request.POST['added_date']
        description = request.POST['description']

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO expenses_expense (added_person, added_amount, added_date, description)
                VALUES (%s, %s, %s, %s)
            """, [added_person, added_amount, added_date, description])

        return redirect('expense_list')  # Assuming 'expense_list' is the name of your URL pattern for the expense list

    return render(request, 'add_expense.html')

def view_reports(request):
    return render(request, 'home.html')
