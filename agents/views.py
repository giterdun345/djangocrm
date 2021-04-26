from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from django.shortcuts import reverse
from .mixins import OrganizerAndLoginRequiredMixin
from django.core.mail import send_mail
import random 

class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
  template_name = 'agents/agent_list.html'

  def get_queryset(self):
    # filters to get access only to the organizations associated with the current user 
    organization = self.request.user.userprofile
    return Agent.objects.filter(organization = organization)

class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
  template_name = "agents/agent_create.html"
  form_class = AgentModelForm


  def get_success_url(self):
    return reverse("agents:agent-list")

  def form_valid(self, form):
    user = form.save(commit=False)
    user.is_agent =True
    user.is_organizer = False
    user.set_password(f"{random.randint(0, 1000000)}")
    user.save()
    Agent.objects.create(
      user=user,
      organization=self.request.user.userprofile
    )
    send_mail(
      subject='Youre invited to be an agent',
      message= 'You were added as an agent on DJCRM. Please come login to start working.',
      from_email= 'admin@test.com',
      recipient_list=[user.email]
      )

    # agent.organization = self.request.user.userprofile
    # agent.save()
    # always call super at the end 
    return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"

    def get_queryset(self):
      # filters to get access only to the organizations associated with the current user 
      organization = self.request.user.userprofile
      return Agent.objects.filter(organization = organization)


class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
  template_name = "agents/agent_update.html"
  queryset = Agent.objects.all()
  form_class = AgentModelForm

  def get_success_url(self):
    return reverse("agents:agent-list")

class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
  template_name = 'agents/agent_delete.html'
  context_object_name = "agent"

  def get_success_url(self):
    return reverse("agents:agent-list")

  def get_queryset(self):
    # filters to get access only to the organizations associated with the current user 
    organization = self.request.user.userprofile
    return Agent.objects.filter(organization = organization)
