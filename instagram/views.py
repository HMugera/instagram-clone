from django.shortcuts import render
from django.views import generic 


class HomeView(generic.TemplateView):
    template_name = 'instagram/home_page.html'

# class HomeView(generic.ListView):
#     template_name = 'leads/lead_list.html'
#     queryset = Lead.objects.all()
#     context_object_name = "leads"
