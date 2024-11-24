from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматично входить користувач після реєстрації
            return redirect('cabinet')  # Перенаправлення до кабінету після успішної реєстрації
        else:
            # Додаємо виведення помилок форми для налагодження
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cabinet')  # Змінити на вашу домашню сторінку
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'


@login_required
def cabinet_view(request):
    return render(request, 'users/cabinet.html', {'user': request.user})

