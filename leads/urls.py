from django.urls import path
from .views import (
   lead_list, lead_detail, lead_create,
   lead_update, lead_delete, LeadListView,
   LeadDetailView, LeadCreateView, LeadUpdateView,
   LeadDeleteView
)
app_name = "leads"

urlpatterns = [
   # path('', lead_list, name='lead-list'),
   path('', LeadListView.as_view(), name= 'lead-list'),
   # path('<int:pk>/', lead_detail, name='lead-detail'),
   path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
   # path('<int:pk>/update/', lead_update, name='lead-update'),
   path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
   # path('<int:pk>/delete/', lead_delete, name='lead-delete'),
   path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
   # put last in order due to linear fashion like express in finding path 
   # path('create/', lead_create, name='lead-create'),
   path('create/', LeadCreateView.as_view(), name='lead-create')
   # name allows us to reference the partivular path a lot easier  
   # use "{% url '<namespace>:<name>' <any arguments from url lead.pk %}" in html to dynamically use the path

]