from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser 
        fields = ("first_name","last_name","username","email","birth_date","gender")
        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.extra_field = self.cleaned_data["first_name","last_name","username","birth_date","gender"]
            if commit:
                user.save()
                return user


class CustomUserChangeForm(UserChangeForm):
    
    class Meta: 
        model = CustomUser 
        fields = UserChangeForm.Meta.fields

class EditProfile(CustomUserChangeForm):

    class Meta: 
        model = CustomUser 
        fields = (
            'first_name',
            'last_name',
            'username',
            'birth_date',
            'gender',
            'password'
        )
