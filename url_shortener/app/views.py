from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app.models import Link
from django.http import HttpResponse, HttpResponsePermanentRedirect
import random

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

    def new_link(self):
        letter = ["a", "b", "c"]
        randomindex = random.randint(0,len(letter)-1)
        rand_letter = letter[randomindex]
        random_num = random.randint(1,5)
        stuff = str(rand_letter * random_num)
        #new_url = str("http://localhost:8000/pass/" + stuff)
        return stuff

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.short_url = self.new_link()
        return super().form_valid(form)

class LinkView(View):
    model = Link
    #template_name = "app/link_list.html"
    #response = HttpResponse("Here's the text of the Web page.")
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data()
        #context["letters"] = self.kwargs['short_url']
        #return context
    def get(self, request, short_url):
        target = self.kwargs['short_url']
        print(target)
        print("-" * 40)
        x = Link.objects.get(short_url = target)
        print(x.url)
        return HttpResponsePermanentRedirect("{}".format(x.url))
