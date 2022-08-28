from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomerUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomerUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'email', 'age',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',)

