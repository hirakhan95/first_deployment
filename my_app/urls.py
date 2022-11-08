from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all_users),
    path('contacts', views.show_all_contacts),
]
