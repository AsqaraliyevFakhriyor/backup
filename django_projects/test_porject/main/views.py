from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Todo

# Create your views here.

def home(request):
    return HttpResponse("<h1> hello world </h1>")


def products(request):
    return HttpResponse("<h1>you are in products menu chose what you want!</h1>")

class Main(TemplateView):
    template_name = "main.html"

class About(TemplateView):
    template_name = "about.html"

class Base(TemplateView):
    template_name = "base.html"


class Todo(ListView):
    model = Todo
    template_name = "todo.html"

