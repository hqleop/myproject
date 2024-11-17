from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm  # Переконайтеся, що ім'я збігається


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматично входить користувач після реєстрації
            return redirect('cabinet')  # Перенаправлення до кабінету після успішної реєстрації
        else:
            # Додаємо виведення помилок форми для налагодження
            print(form.errors)
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'

@login_required
def cabinet_view(request):
    return render(request, 'users/cabinet.html', {'user': request.user})

