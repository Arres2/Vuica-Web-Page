from django.urls import path
from . import views



app_name= "Homepage"
urlpatterns = [
    path("", views.index, name= 'Home'),
    path("google13754e890efe3188.html", views.google)
  
]

