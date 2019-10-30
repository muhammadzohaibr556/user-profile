from django.urls import path
from .views import SignUpView, userUpdateView
from django.contrib.auth.decorators import login_required
urlpatterns = [ 
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update/', login_required(userUpdateView), name='update')
    ]
