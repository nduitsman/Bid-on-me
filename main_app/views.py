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
        
class AutoPost(CreateView):
    model = Auto
    fields = ['make','model','year','condition','mileage','accidents','tickets','premium','provider','liability','uninsured','medical','roadside','safe_driver','zip','annual_miles','credit_score','age','coverage_preference']
    template_name = 'autopost.html'
    success_url='/'
    # def post(self, request, pk):
    #     user = User.objects.get(id=request.user.id)
    
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(AutoPost, self).form_valid(form)
    # def get_success_url(self):
    #     print(self.kwargs)
    #     return reverse('home', kwargs={'pk':self.object.pk})
