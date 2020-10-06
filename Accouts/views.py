from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request, user_)
        return redirect("/")
    return render(request, 'accounts/login.html', {"form": form})


def logout_view(request, *args, **kwargs):
    if request.method == 'POST':
        logout(request)
        return redirect("/")

    return render(request, 'accounts/logout.html')


def registration_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password"))
        return render(request, "accounts/success.html")
    return render(request, 'accounts/register.html', {"form": form})

