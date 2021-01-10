from django.urls import path

from .views import * 
  
urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('search', search, name='search'),
  path('property/<str:property_id>', PropertyPageView.as_view(), name='property'),
  path('search-results/', SearchResultsPageView.as_view(), name='search-results'),
  path('soon/', SoonPageView.as_view(), name='soon'),
  path('pricing/', PricingPageView.as_view(), name='pricing'),
  path('projects/', ProjectsPageView.as_view(), name='projects'),
  path('contact/', ContactPageView.as_view(), name='contact'),
  path('project-single/', ProjectSinglePageView.as_view(), name='project-single'),
  path('maintenance/', MaintenancePageView.as_view(), name='maintenance'),
]
  
