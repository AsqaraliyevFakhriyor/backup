from django.urls import path
from .views import second_page

app_name = "playground"

urlpatterns = [
    path("", second_page, name = "second_page"),
]
