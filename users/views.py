from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login



def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request,user)
                messages.success(request, 'Login successfully done')
                return redirect('user_profile')
            else:
                messages.error(request, "Invalid credentials provided")
                return redirect('login')
    return render(request, 'users/login.html')


class ProfileUser(TemplateView):
    template_name = "user_profile.html"
        




class RegisterUser(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            print(user)
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('login')
        else:

            print(form.errors)

        return render(request, 'users/register.html', {'form': form})
    

