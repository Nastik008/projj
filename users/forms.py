from django import forms
# from .models import UserProfile
# from django.contrib.auth.models import Group
# from django.contrib.auth.forms import UserCreationForm

# class UserProfileForm(forms.ModelForm):
#     group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
#     class Meta:
#         model = UserProfile
#         fields = [
#             'role',
#             'tg',
#             'email',
#             'phone',
#             # 'stud_group',
#             # 'team',
#             # 'team_role'
#         ]
#         widgets = {
#             'tg': forms.TextInput(attrs={'placeholder': 'Введите ваш Telegram'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Введите вашу почту'}),
#             'phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         #self.fields['role'].queryset = Group.objects.all()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)