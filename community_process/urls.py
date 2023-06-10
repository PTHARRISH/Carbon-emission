from . import views
from django.urls import path
urlpatterns=[
    path('community_home_index/',views.community_home_index),
    path('c_login/', views.c_login),
    path('registration_community_process/', views.registration_community_process),

]