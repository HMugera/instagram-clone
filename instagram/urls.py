from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView,SignupView
import django.contrib.auth.urls 
# from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views  as auth_views


urlpatterns=[
 
path('',HomeView.as_view(),name='home'),
path('signup/', SignupView.as_view(success_url='/'), name='signup'),
path('accounts/', include('django.contrib.auth.urls')),
path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page = '/')),
   
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
