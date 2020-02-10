from django.urls import path
from . import views
urlpatterns = [
    path('ooii/',views.index),
    path('login',views.login),
    path('show/',views.show),
    path('register',views.register),
    path('re',views.v),
    path('index',views.movie_01),

]