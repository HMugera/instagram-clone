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
from cloudinary.forms import cl_init_js_callbacks
from django.views.decorators.csrf import csrf_exempt



class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse("login")
    


# @login_required(login_url='/accounts/login/')
def home_page(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}
    
    return render(request,'instagram/home_page.html',ctx)

# @login_required(login_url='/accounts/login/')
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

def view_post(request,pk):
    post = Post.objects.get(id=pk)
    ctx = {'post':post}
    
    return render(request,'instagram/view_post.html',ctx)
    
    
    