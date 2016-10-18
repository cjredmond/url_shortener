from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Link, Hit
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
import random

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class LinkUpdateView(UpdateView):
    model = Link
    success_url = "/"
    fields = ("url", "title", "description")

class LinkListView(ListView):
    model = Link

class LinkCreateView(CreateView):
    model = Link
    success_url = "/"
    fields = ('url', 'title', 'description')

    def new_link(self):
        letter = ["a", "b", "c", "d", "e", "f", "g"]
        randomindex = random.randint(0,len(letter)-1)
        rand_letter = letter[randomindex]
        random_num = random.randint(1,7)
        stuff = str(rand_letter * random_num)
        return stuff

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.short_url = self.new_link()
        return super().form_valid(form)

class LinkView(View):
    model = Link

    def get(self, request, short_url):
        target = self.kwargs['short_url']
        x = Link.objects.get(short_url = target)
        print("0"* 20)
        Hit.objects.create(link = x,  clicked=True)
        return HttpResponseRedirect("{}".format(x.url))
