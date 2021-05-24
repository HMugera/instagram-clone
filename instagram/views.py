from django.http.response import Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from .forms import *
from django.contrib import messages
from .models import Post, Comments, Profile, Follow
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
    try:
        comments = Comments.filter_comments_by_post_id(pk)
        print(comments)
        
    except Comments.DoesNotExist:  
        comments = None
    
    ctx = {
        'post':post,
        "comments":comments
        }
    
    return render(request,'instagram/view_post.html',ctx)

def add_comment(request,post_id):
    current_user = request.user
    if request.method == 'POST':
        comment= request.POST.get('comment')
    post = Post.objects.get(id=post_id)
    user_profile = User.objects.get(username=current_user.username)
    Comments.objects.create(
         comment=comment,
         post = post,
         user=user_profile   
        )
    return redirect('instagram:view_post' ,pk=post_id)


def like_post(request,post_id):
    post = Post.objects.get(pk=post_id)
    is_liked=False
    user=request.user.profile
    try:
        profile=Profile.objects.get(user=user.user)
        print(profile)

    except Profile.DoesNotExist:
        raise Http404()
    if post.likes.filter(id=user.user.id).exists():
        post.likes.remove(user.user)
        is_liked=False
    else:
        post.likes.add(user.user)
        is_liked=True
    return HttpResponseRedirect(reverse('home'))



def profile(request,username):
    user = User.objects.get(username=username)
    profile = Profile.filter_profile_by_id(user.id)

    ctx = {
        "profile":profile,
        'user':user
        }
   
    return render(request, 'profile/profile.html',ctx)

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateUserProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateUserProfileForm(request.POST,instance=profile)
            if form.is_valid():  
                form.save()
                return redirect('/') 
            
    ctx= {"form":form}
    return render(request, 'profile/update_profile.html',ctx)
    
    
    