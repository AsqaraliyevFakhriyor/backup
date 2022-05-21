from django.urls import path
from .views import home, products, Main, About, Base, Todo

urlpatterns = [
    path('', home, name='home'),
    path('products', products, name='products'),
    path('main', Main.as_view(), name='main'),
    path('about', About.as_view(), name="about"),
    path('base', Base.as_view(), name="base"),
    path('todo', Todo.as_view(), name='todo')
]
