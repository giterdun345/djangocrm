from django import forms
# from leads.models import User 
from django.contrib.auth import get_user_model
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class AgentModelForm(forms.ModelForm):
  class Meta:
    model = User
    fields = (
      'username',
      'email',
      'first_name',
      'last_name',
    )
