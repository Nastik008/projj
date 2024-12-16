from django.urls import path
from .views import RegisterUser, LoginView, ProfileUser, MainPage

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='register'),
    path("login/", LoginView, name='login'),
    path("profile/", ProfileUser, name='user_profile'),
    path("", MainPage.as_view(), name='main'),
    

]