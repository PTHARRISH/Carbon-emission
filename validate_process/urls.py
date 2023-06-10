from . import views
from django.urls import path
urlpatterns=[
       path('data_home_index/',views.validate_home_index),
       path('v_login/', views.v_login),
      path('registration_validate_process/', views.registration_validate_process),
      path('uuu/', views.uuu)

]