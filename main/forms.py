from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Customer


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Customer
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = ('email',)
