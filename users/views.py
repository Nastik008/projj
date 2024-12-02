from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from .forms import UserProfileForm
from django.contrib.auth import login, authenticate

class RegisterUser(View):
    def get(self, request):
        form = UserProfileForm()
        return render(request, 'users/register.html', {'form': form})
    
    def post(self, request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #user.set_password(form.cleaned_data['password'])
            user.save()
            group = form.cleaned_data.get('role')
            if group:
                user.role = group
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('login')  
        return render(request, 'users/register.html', {'form': form})
    

