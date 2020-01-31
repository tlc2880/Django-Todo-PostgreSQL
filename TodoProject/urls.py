#  Name: Tommy Cao
#  Date: 10/22/17
#  Description: Django Todo with PostgreSQL.

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/',include('todos.urls'))
]