from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signap/', SignUpView.as_view(), name='signup')
]
