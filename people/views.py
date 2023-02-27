from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Регистрация прошла успешно!')
    else:
        form = UserRegisterForm()
    return render(request, 'people/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'people/profile.html')


