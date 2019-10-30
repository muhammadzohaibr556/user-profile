from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm, EditProfile
from .models import CustomUser
from django.shortcuts import render, redirect
class SignUpView(CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'signup.html'


def userUpdateView(request):
    if request.method=="POST":
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form = EditProfile(instance=request.user)
        args = {'form':form}
        return render (request,'update.html',args)
