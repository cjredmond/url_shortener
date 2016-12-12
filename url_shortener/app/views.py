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
    fields = ('url', 'title', 'description', 'public')

class LinkListView(ListView):
    model = Link
    def get_context_data(self):
        context = super().get_context_data()
        if not self.request.user.is_authenticated:
            public = Link.objects.filter(public = True)
            context["public"] = public
        else:
            user_link = Link.objects.filter(user= self.request.user)
            public = Link.objects.filter(public = True)
            public_ex = public.exclude(user = self.request.user)
            context["user_link"] = user_link
            context["public_ex"] = public_ex
        return context


class LinkCreateView(CreateView):
    model = Link
    success_url = "/"
    fields = ('url', 'title', 'description', 'public')

    def new_link(self):
        letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
        randomindex = random.randint(0,len(letter)-1)
        rand_letter = letter[randomindex]
        random_num = random.randint(1,4)
        stuff = str(rand_letter * random_num)
        return stuff

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.short_url = str(self.new_link() + self.new_link() + self.new_link())
        return super().form_valid(form)

class LinkView(View):
    model = Link

    def get(self, request, short_url):
        x = Link.objects.get(short_url = short_url)
        Hit.objects.create(link = x,  clicked=True)
        return HttpResponseRedirect("{}".format(x.url))
