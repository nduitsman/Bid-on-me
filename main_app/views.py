
from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

from .models import Auto, Profile, Bid
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count


class Home(TemplateView):
    template_name = 'home.html'

class UserProfile(TemplateView):
    template_name = 'user_profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["auto_posts"] = Auto.objects.all().filter(username = self.request.user.username)
        context["bids"] = Bid.objects.all()
        return context
    
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
  
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
        
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

        
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
        # for post in context['auto_posts']:
        #     context['test'] = Bid.objects.all().filter(auto_post_id = post['id'])
        context["bids"] = Bid.objects.all()

        return context
    
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['account_type','company','email','first_name','last_name','phone_number','profile_image']
    template_name = 'profile_update.html'
    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.pk})
    
class UpdateAutoPost(UpdateView):
    model = Auto
    fields = ['make','vehicle_model','year' ,'condition','mileage','accidents','tickets','premium','provider','liability','uninsured','medical','roadside','rental','safe_driver','zip' ,'annual_miles','credit_score','age','coverage_preference','username']
    template_name = 'auto_post_update.html'
    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.pk})
    
class AutoPostDetail(DetailView):
    model = Auto
    template_name= 'auto_post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["auto_posts"] = Auto.objects.all()
        context["bids"] = Bid.objects.all()
        return context

class BidCreate(View):
    def post(self, request, pk):
        more_info = request.POST.get('more_info')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        phone_number = '(' + phone_number[0:3] + ') ' + phone_number[3:6] + '-' + phone_number[6:10]
        company = request.POST.get('company')
        auto_post_id = request.POST.get('auto_post_id')
        Bid.objects.create(username=username, company=company, phone_number=phone_number, more_info=more_info, auto_post_id=auto_post_id)
        return redirect('auto_posts')

class AutoPostDelete(DeleteView):
    model = Auto
    template_name = 'auto_post_delete.html'
    def get_success_url(self):
        return reverse('user_profile', kwargs={'pk': self.object.pk})