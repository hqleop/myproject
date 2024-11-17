from django.urls import path
from .views import register_view, CustomLoginView, cabinet_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),  # Перенаправлення на головну після виходу
    path('cabinet/', cabinet_view, name='cabinet'),
]