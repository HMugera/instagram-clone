from django.http.response import Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from .forms import *
from django.contrib import messages
from .models import Post, Comment, Profile, Follow
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views import generic 



class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse("login")
    



class HomeView(generic.TemplateView):
    template_name = 'instagram/home_page.html'

# class HomeView(generic.ListView):
#     template_name = 'leads/lead_list.html'
#     queryset = Lead.objects.all()
#     context_object_name = "leads"
