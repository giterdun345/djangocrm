from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm


def landing_page (request):  
  return render(request, "landing.html")

def lead_list (request):
  leads = Lead.objects.all()
  
  context={
    "leads": leads
  }  
  return render(request, "leads/leads_list.html", context)

def lead_detail(request, pk):
  lead = Lead.objects.get(id=pk)
  context={
    "lead": lead
  }
  return render(request, "leads/leads_detail.html", context)


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