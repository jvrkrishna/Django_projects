from django.urls import path
from . import views

urlpatterns = [
    path('tech_news/', views.Tech_view),
]