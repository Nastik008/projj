from django.urls import path
from .views import RegisterUser, LoginView, ProfileUser

urlpatterns = [
    path('registration/', RegisterUser.as_view(), name='register'),
    path("login/", LoginView, name='login'),
    path("profile/", ProfileUser.as_view(), name='user_profile'),

]