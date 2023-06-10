from . import views
from django.urls import path
urlpatterns=[
       path('emission_home_index/',views.emission_home_index),
       path('login/',views.e_login),
       path('registration_emission_check/', views.registration_emission_check),
       path('emission_check_homepage/', views.emission_check_homepage),
       path('total_emission/<int:id>/', views.total_emission),
       path('home/',views.home),
       path('view_emission_calculate/',views.view_emission_calculate),
       path('emission_logout/',views.emission_logout),
       path('userindex/',views.userindex),
       path('usersave/',views.usersave),
       path('user_update/',views.user_update),
       path('delete/<int:id>/',views.delete),
       path('update/<int:id>/', views.update),
       path('updatetemp/',views.updatetemp)

]