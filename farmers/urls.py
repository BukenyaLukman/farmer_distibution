from django.urls import path
from . views import (home_view,farmers_view)

app_name = "farmer"



urlpatterns = [
	path('api/',home_view, name="home"),
	path('',farmers_view, name="farmer-view"),
]