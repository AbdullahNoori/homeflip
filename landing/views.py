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

class SearchPageView(TemplateView):
    template_name = 'landing/search.html'
    form_class = SearchForm()

    def get_context_data(self, **kwargs):
        context = {}

        # get search from the form
        # pass the query to autocomplete and get the full address
        fullAddress = autoComplete("glenolden")
        
        # get the results
        
        data = listForSale(fullAddress['city'], fullAddress['state_code'])
        
        
        # print(data['properties'])
        # pass the data['properties'] to context
        
        return context
        
    def get_form(self, form_class=None):
        form = super(SearchPageView, self).get_form(form_class)
        # override the queryset
        form.fields['keywords'].queryset = self.petitioner.players 
        return form

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
    context = {}
    query = request.POST.get('location')
    
    fullAddress = autoComplete("glenolden")
    data = listForSale(fullAddress['city'], fullAddress['state_code'])
    context['properties'] = data['properties']
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