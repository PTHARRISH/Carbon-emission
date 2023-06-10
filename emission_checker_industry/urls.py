from . import views
from django.urls import path
urlpatterns=[
       path('emission_home_index/',views.emission_home_index),
       path('e1_login/',views.e1_login),
       path('registration_emission_checker_industry/', views.registration_emission_checker_industry),
       path('home_industry/',views.home_industry),
       path('emission_check_industry/',views.emission_check_industry),
       path('view_emission_calculate_industry/',views.view_emission_calculate_industry),
       path('total_emission_industry/<int:id>/',views.total_emission_industry),
       path('emission_logout/',views.emission_logout),
       path('industryindex/',views.industryindex),
       path('industrysave/',views.industrysave),
       path('industry_update/', views.industry_update),
       path('deletein/<int:id>/', views.deletein),
       path('updatein/<int:id>/', views.updatein),
       path('industrytemp/',views.industrytemp),

]


