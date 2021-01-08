# from django.shortcuts import render
from django.shortcuts import render
import json
from django.views.generic.base import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'landing/index.html'

class PricingPageView(TemplateView):
    template_name = 'landing/pricing.html'

class SearchPageView(TemplateView):
    template_name = 'landing/search.html'


class SearchResultsPageView(TemplateView):
    template_name = 'landing/search-results.html'

class SoonPageView(TemplateView): 
    template_name = 'landing/soon.html'

class PropertyPageView(TemplateView):
    template_name = 'landing/property.html'


class ProjectsPageView(TemplateView):
    template_name = 'landing/projects.html'