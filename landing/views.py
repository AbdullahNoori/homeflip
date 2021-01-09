# from django.shortcuts import render
from django.shortcuts import render
import json
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .forms import *
from .api import *

class HomePageView(TemplateView):
    template_name = 'landing/index.html'

class PricingPageView(TemplateView):
    template_name = 'landing/pricing.html'
    

class FilterPage(ListView):
    def get(self, request):
        return render(request, 'landing/search.html')

    def post(self, request):
        city = request.POST.get('city')
        address = request.POST.get('address')
        fullAddress = autoComplete(str(address)+" "+str(city))

        data = listForSale(fullAddress['city'], fullAddress['state_code'])

        # runAI(data['properties'])

        context = {'address': fullAddress}
        
        return render(request, 'landing/search.html', context)

def search(request):
    if request.method == "GET":
        return render(request, 'landing/search.html')
    
    else:
        
        query = request.POST.get('location')
        fullAddress = autoComplete(query)
        data = listForSale(fullAddress['city'], fullAddress['state_code'])
        context = {'properties':  data['properties'] }

        return render(request, 'landing/search.html', context)


class SearchResultsPageView(TemplateView):
    template_name = 'landing/search-results.html'


class PropertyPageView(ListView):
    
    def get(self, request, property_id):
        
        data = propertyDetail(property_id)
        
        context = {"property": data['properties'][0]}
        
        return render(request, 'landing/property.html', context)

    
    

class ProjectsPageView(TemplateView):
    template_name = 'landing/projects.html'
    
class ProjectSinglePageView(TemplateView):
    template_name = 'landing/project-single.html'
    
class MaintenancePageView(TemplateView):
    template_name = 'landing/404/maintenance.html'
    
class SoonPageView(TemplateView): 
    template_name = 'landing/404/soon.html'