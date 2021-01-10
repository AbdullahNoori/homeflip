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
    
class ContactPageView(ListView):
    def get(self, request):
        return render(request, 'landing/contacts.html')

    def post(self, request):
            
        
        city = request.POST.get('city', city)
        address = request.POST.get('address')
        fullAddress = autoComplete(str(address)+" "+str(city))

        data = listForSale(fullAddress['city'], fullAddress['state_code'])

        # runAI(data['properties'])

        context = {'address': fullAddress}
        
        return render(request, 'landing/search.html', context)

def search(request, *args, **kwargs):
    
    
    if request.method == "GET":
        query = request.GET.get('city', None)
        context = {}
        if not query is None:
            fullAddress = autoComplete(query)
            search_query = {
                'fullAddress': fullAddress,
            }
            
            data = listForSale(search_query)
            context = {'properties':  data['properties'], 'fullAddress': fullAddress,}
        
        
        return render(request, 'landing/search.html', context)
    
    else:
        fullAddress = autoComplete(request.POST.get('location'))
        search_query = {
            'fullAddress': fullAddress,
            'sort' : request.POST.get('sort', ""),
            'prop_type' : request.POST.get('prop_type', ""),
            'price_min' : request.POST.get('min_price', ""),
            'price_max' : request.POST.get('max_price', ""),
            'beds_min' : request.POST.get('beds_min', ""),
            'baths_min' : request.POST.get('baths_min', ""),
            'radius' : request.POST.get('radius', ""),
            'limit' : request.POST.get('limit', ""),
        }
        
        data = listForSale(search_query)
        context = {'properties':  data['properties'], 'fullAddress': fullAddress, }

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