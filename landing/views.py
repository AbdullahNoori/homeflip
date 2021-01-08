# from django.shortcuts import render
from django.shortcuts import render
import json
from django.views.generic.base import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'landing/index.html'

