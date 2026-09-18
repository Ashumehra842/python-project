from django.urls import path
from . import views
urlpatterns = [
    path('', views.tours, name="tours"),
    path('requests', views.requests, name="requests"),
    path('create', views.create, name="create"),
    path('detail/<int:id>', views.details, name="detail")
]