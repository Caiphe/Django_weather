from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import  Group, User
from django.contrib import  messages
from .forms import UserRegistrationForm, CustomAuthenticationForm
from django.conf import settings
from django.urls import reverse_lazy


def user_registration_view(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
                user = form.save()
                login(request, user)
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                password2 = form.cleaned_data.get('password2')

                user = authenticate(username=username, password=password)
                return redirect('/')

                if user is not None:
                    login(request, user)
                    return redirect('/core/')
                messages.success(request, 'Account Created')
        else:
            messages.warning(request, "Try Again")
    form = UserRegistrationForm
    context = { 'form': form}
    return render(request, 'accounts/register.html', context)


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, f"Logged Out")
    return redirect('/')


# Login View
def login_request_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/core/')
            else:
                messages.info(request, "Username or password not valid")
                return redirect('/')
        else:
            messages.warning(request, "Something Went Wrong")

    form = CustomAuthenticationForm
    return render(request, 'accounts/login.html', {'form' : form})


# Check if username exists already
def check_username_exists(request):
    username = request.GET.get('username', None)
    check_data = User.objects.filter(username__iexact=username).exists()
    if not check_data:
        data = { 'exists': True }
    else:
        data = { 'exists': False }
    return JsonResponse(data)


# Check if Email exists already
def check_email_exists(request):
    email = request.GET.get('email', None)
    data = { 'is_taken': User.objects.filter(email__iexact=email).exists() }
    return JsonResponse(data)

