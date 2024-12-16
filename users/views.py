from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def main_view(request):
    return render(request, 'main.html')

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
                return redirect('user_profile')
        messages.error(request, "Invalid credentials provided")
        return redirect('login')
    return render(request, 'users/login.html')


def ProfileUser(request):
    # template_name = "users/user_profile.html"
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # user = authenticate(request, name=form.cleaned_data.get('name'), surname=form.cleaned_data.get('surname'), group=form.cleaned_data.get('group'), contacts=form.cleaned_data.get('contacts'))
            return redirect('main')
        else:
            messages.error(request, "Invalid credentials provided")
            return redirect('user_profile')
    return render(request, 'users/user_profile.html')




class MainPage(LoginRequiredMixin, TemplateView):
    template_name = "users/main.html"
    login_url = '/login/'
    redirect_field_name = 'next'  # Параметр запроса для перенаправления

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})



        




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
    

