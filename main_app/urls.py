from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(), name = 'home'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('auto/new/', views.AutoPost.as_view(), name = 'newAutoPost'),
]