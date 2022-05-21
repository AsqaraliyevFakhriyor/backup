from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second_page(request):
    """
        second page function in playground.views it will render html template and return response to client side
    """
    x = 1
    y = 2

    return render(request, "hello.html", {"name": "Felix"})