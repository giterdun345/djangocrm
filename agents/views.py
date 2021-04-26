from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from django.shortcuts import reverse

class AgentListView(LoginRequiredMixin, generic.ListView):
  template_name = 'agents/agent_list.html'

  def get_queryset(self):
    # filters to get access only to the organizations associated with the current user 
    organization = self.request.user.userprofile
    return Agent.objects.filter(organization = organization)

class AgentCreate(LoginRequiredMixin, generic.CreateView):
  template_name = "agents/agent_create.html"
  form_class = AgentModelForm


  def get_success_url(self):
    return reverse("agents:agent-list")

  def form_valid(self, form):
    agent = form.save(commit=False)
    agent.organization = self.request.user.userprofile
    agent.save()
    # always call super at the end 
    return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"

    def get_queryset(self):
      # filters to get access only to the organizations associated with the current user 
      organization = self.request.user.userprofile
      return Agent.objects.filter(organization = organization)


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
  template_name = "agents/agent_update.html"
  queryset = Agent.objects.all()
  form_class = AgentModelForm

  def get_success_url(self):
    return reverse("agents:agent-list")

class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
  template_name = 'agents/agent_delete.html'
  context_object_name = "agent"

  def get_success_url(self):
    return reverse("agents:agent-list")

  def get_queryset(self):
    # filters to get access only to the organizations associated with the current user 
    organization = self.request.user.userprofile
    return Agent.objects.filter(organization = organization)
