from django.shortcuts import render, redirect, reverse 
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views.generic import (TemplateView, 
ListView, UpdateView, DetailView, DeleteView, 
CreateView
)
class LandingPageView(TemplateView):
  template_name = "landing.html"

def landing_page (request):  
  return render(request, "landing.html")

class LeadListView(ListView):
  template_name = "leads/leads_list.html"
  queryset = Lead.objects.all()
  # automatically assigns context variables to be called object_list

def lead_list (request):
  leads = Lead.objects.all()  
  context={
    "leads": leads
  }  
  return render(request, "leads/leads_list.html", context)

class LeadDetailView(DetailView):
  template_name = "leads/leads_detail.html"
  queryset = Lead.objects.all()
  context_object_name = 'lead'

def lead_detail(request, pk):
  lead = Lead.objects.get(id=pk)
  context={
    "lead": lead
  }
  return render(request, "leads/leads_detail.html", context)

class LeadCreateView(CreateView):
  template_name = "leads/lead_create.html"
  form_class = LeadModelForm

  def get_success_url(self):
    # on success redirects you back to list 
    return reverse('leads:lead-list')


def lead_create(request):
  # 2:48 bookmark 
  form = LeadModelForm()
  if request.method =='POST':
    print('receiving a post request')
    form = LeadModelForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("/leads")
  context = {

    "form": form
  }
  return render(request, "leads/lead_create.html", context)

class LeadUpdateView(UpdateView):
  template_name = "leads/lead_update.html"
  queryset = Lead.objects.all()
  form_class = LeadModelForm

  def get_success_url(self):
    # on success redirects you back to list 
    return reverse('leads:lead-list')

def lead_update(request, pk):
  lead = Lead.objects.get(id = pk)
  # instance is the single object you want to update 
  form = LeadModelForm(instance=lead)
  if request.method =='POST':
    form = LeadModelForm(request.POST, instance = lead)
    if form.is_valid():
      form.save()
      return redirect("/leads/")

  context = {
    "form": form, 
    "lead": lead
  }

  return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(DeleteView):
  template_name = 'leads/lead_delete.html'
  queryset = Lead.objects.all()

  def get_success_url(self):
  # on success redirects you back to list 
    return reverse('leads:lead-list')

def lead_delete(request, pk):
  lead = Lead.objects.get(id = pk)
  lead.delete()
  return redirect('/leads')


# def lead_create(request):
#   # 2:48 bookmark 
  # form = LeadForm()
  # if request.method =='POST':
  #   print('receiving a post request')
  #   form = LeadForm(request.POST)
  #   if form.is_valid():
  #     print('Valid Form')
  #     print(form.cleaned_data)
  #     first_name = form.cleaned_data['first_name']
  #     last_name = form.cleaned_data['last_name']
  #     age = form.cleaned_data['age']
  #     agent = Agent.objects.first()
  #     Lead.objects.create(first_name = first_name, last_name = last_name, age = age, agent =  agent)
  #     print('Lead Created')
  #     return redirect("/leads")
  # context = {

  #   "form": form
  # }
#   return render(request, "leads/lead_create.html", context)

# def lead_update(request, pk):
#   lead = Lead.objects.get(id = pk)
#   form = LeadForm()
#   if request.method =='POST':
#     print('receiving a post request')
#     form = LeadForm(request.POST)
#     if form.is_valid():
#       first_name = form.cleaned_data['first_name']
#       last_name = form.cleaned_data['last_name']
#       age = form.cleaned_data['age']
#       # after grabbing all of the data from the form 
#       # you place it into model and save 
#       lead.first_name = first_name
#       lead.last_name= last_name
#       lead.age = age
#       lead.save()
#       return redirect("/leads")

#   context = {
#     "lead": lead,
#     "form": form
#   }
#   return render(request, 'leads/lead_update.html', context)