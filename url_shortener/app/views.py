from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Link

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "http://localhost:8000/linklist/"

class LinkListView(ListView):
    model = Link

class LinkCreateView(CreateView):
    model = Link
    success_url = "http://localhost:8000/linklist/"
    fields = ('url', 'title', 'description')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class LinkView(View):
    model = Link
    
