from django.urls import path
from .views import App1_view
urlpatterns = [
    path('',App1_view,name='App1_home'),
]