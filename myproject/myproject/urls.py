from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('users/', include('users.urls')),  # Маршрути додатку users
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]
