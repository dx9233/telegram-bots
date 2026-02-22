from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm


class HomeView(View):
    template_name = 'base.html'
    
   