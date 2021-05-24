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
    



# class HomeView(generic.TemplateView):
#     template_name = 'instagram/home_page.html'

class HomeView(generic.ListView):
    template_name = 'instagram/home_page.html'
    queryset = Post.objects.all()
    context_object_name = "posts"

# class UploadPictureView(generic.CreateView):
#     template_name = 'instagram/upload_picture.html'
#     form_class = UploadImageModelForm

#     def get_success_url(self):
#         return reverse("instagram:home")
def upload_picture(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadImageModelForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
            return redirect('/',username=request.user)
    else:
        form = UploadImageModelForm()
    return render(request,'instagram/upload_picture.html',{'form':form})
    
    