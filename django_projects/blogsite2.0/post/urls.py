from django.urls import path

from .views import (
    PostDetailView,
    PostListView,
    PostEditView,
    PostDeleteView,
    PostCreateView,
)

app_name = "post"

# Post app urls

urlpatterns = [
    path('', PostListView.as_view(), name = "post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', PostDetailView.as_view(), name = "post_detail"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/edit", PostEditView.as_view(), name = "post_edit"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/'delete", PostDeleteView.as_view(), name = "post_delete"),
    path("craete/article", PostCreateView.as_view(), name = "post_create"),
 ]