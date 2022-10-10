from distutils.sysconfig import get_config_h_filename
from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Auto
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


class Home(TemplateView):
    template_name = 'home.html'

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
@method_decorator(login_required, name='dispatch')
class AutoPost(CreateView):
    model = Auto
    fields = ['make','vehicle_model','year' ,'condition','mileage','accidents','tickets','premium','provider','liability','uninsured','medical','roadside','rental','safe_driver','zip' ,'annual_miles','credit_score','age','coverage_preference','username']
    template_name = 'autopost.html'
    success_url='/'
    
@method_decorator(login_required, name='dispatch')
class AutoList(TemplateView):
    template_name = 'auto_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["auto_posts"] = Auto.objects.all()
        return context
    
    