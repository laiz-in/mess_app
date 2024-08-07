from django.contrib import admin
from django.urls import include, path

from .views import (add_expense, expense_list, home,  # Import the home view
                    view_reports)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('expenses/',expense_list, name="expense_list" ),

    path('add_expense/',add_expense, name="add_expense" ),

    path('view_reports/',view_reports, name="view_reports" ),

]
