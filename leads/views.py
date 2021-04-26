from django.contrib.auth.mixins import LoginRequiredMixin
# must make sure it is first so it is called first 
from agents.mixins import OrganizerAndLoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse 
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views.generic import (TemplateView, 
ListView, UpdateView, DetailView, DeleteView, 
CreateView
)

class SignupView(CreateView):
  template_name = "registration/signup.html"
  form_class = CustomUserCreationForm

  def get_success_url(self):
    # on success redirects you back to list 
    return reverse('login')

class LandingPageView(TemplateView):
  template_name = "landing.html"

def landing_page (request):  
  return render(request, "landing.html")

class LeadListView(LoginRequiredMixin,ListView):
  template_name = "leads/leads_list.html"

  def queryset(self):
    user = self.request.user
    # initial queryset of the leads for the entire organization
    if user.is_organizer: 
      queryset = Lead.objects.filter(organization=user.userprofile )
    else:
      queryset = Lead.objects.filter(organization=user.agent.organization )
      # filter for the agent that is logged in 
      queryset = queryset.filter(agent__user= user)

    # # this does not query multiple times. it takes the original query and filters that 
    # if self.request.user.is_agent:
    #   # filter the query using double underscore indicates a filter where the agent has a user the same as request user 
    #   queryset = queryset.filter(agent__user= user)

    return queryset
  # queryset = Lead.objects.all()
  # automatically assigns context variables to be called object_list

def lead_list (request):
  leads = Lead.objects.all()  
  context={
    "leads": leads
  }  
  return render(request, "leads/leads_list.html", context)

class LeadDetailView(LoginRequiredMixin, DetailView):
  template_name = "leads/leads_detail.html"
  # queryset = Lead.objects.all()
  context_object_name = 'lead'

  def queryset(self):
    user = self.request.user
    # initial queryset of the leads for the entire organization
    if user.is_organizer: 
      queryset = Lead.objects.filter(organization=user.userprofile)
    else:
      queryset = Lead.objects.filter(organization=user.agent.organization )
      # filter for the agent that is logged in 
      queryset = queryset.filter(agent__user= user)
    return queryset

def lead_detail(request, pk):
  lead = Lead.objects.get(id=pk)
  context={
    "lead": lead
  }
  return render(request, "leads/leads_detail.html", context)

class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
  template_name = "leads/lead_create.html"
  form_class = LeadModelForm

  def get_success_url(self):
    # on success redirects you back to list 
    return reverse('leads:lead-list')
  
  def form_valid(self, form):
    # if connection refused error 
    send_mail(
      subject="A lead has been created",
      message="Go to the site to see the new lead",
      from_email= "test@test.com",
      recipient_list=["test2@test.com"]
    )
    return super(LeadCreateView, self).form_valid(form)

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

class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
  template_name = "leads/lead_update.html"
  # queryset = Lead.objects.all()
  form_class = LeadModelForm

  def queryset(self):
    user = self.request.user
    # initial queryset of the leads for the entire organization
    queryset = Lead.objects.filter(organization=user.userprofile )
    return queryset

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


class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
  template_name = 'leads/lead_delete.html'
  queryset = Lead.objects.all()
  
  def queryset(self):
    user = self.request.user
    # initial queryset of the leads for the entire organization
    queryset = Lead.objects.filter(organization=user.userprofile )
    return queryset

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