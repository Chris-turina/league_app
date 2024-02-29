from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('leagues/', views.getLeagues, name="leagues"),
    path('leagues/<str:pk>', views.getLeague, name="league")
]