from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm 
from .models import CustomUser

class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm 
    form = CustomUserChangeForm 
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', ] # new
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Personal Info',{'fields': ('username', 'first_name', 'last_name','birth_date','gender','date_joined')}),
    ) 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username','birth_date','gender', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    readonly_fields=('date_joined',)
    
admin.site.register(CustomUser, CustomUserAdmin)