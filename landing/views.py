# from django.shortcuts import render
from django.shortcuts import render
import json
from django.views.generic.base import TemplateView

from .api import *

class HomePageView(TemplateView):
    template_name = 'landing/index.html'

class PricingPageView(TemplateView):
    template_name = 'landing/pricing.html'

class SearchPageView(TemplateView):
    template_name = 'landing/search.html'

    def get_context_data(self, **kwargs):
        context = {}
        # get serarch from the from
        # passs the query to autocomplete and get the full address
        fullAddress = autoComplete("glenolden")
        
        # get the results
        
        data = listForSale(fullAddress['city'], fullAddress['state_code'])
        
        
        # print(data['properties'])
        # pass the data['properties'] to context
        
        return context
        
        

    
    

class SearchResultsPageView(TemplateView):
    template_name = 'landing/search-results.html'

class PropertyPageView(TemplateView):
    template_name = 'landing/property.html'

class ProjectsPageView(TemplateView):
    template_name = 'landing/projects.html'
    
class ProjectSinglePageView(TemplateView):
    template_name = 'landing/project-single.html'
    
class MaintenancePageView(TemplateView):
    template_name = 'landing/404/maintenance.html'
    
class SoonPageView(TemplateView): 
    template_name = 'landing/404/soon.html'