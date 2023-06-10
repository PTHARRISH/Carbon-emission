from . import views
from django.urls import path
urlpatterns=[
    path('C',views.data_home_index),
    path('registration_data_analyst/', views.registration_data_analyst),
    path('data_index/',views.data_index),
    # path('data_hp/', views.data_hp),
    path('datapage/',views.datapage),
    path('data_analyst_data_save/',views.data_analyst_data_save),
    path('dataset_view_industry/', views.dataset_view_industry),
    path('total_emission_datamatch/<int:id>/',views.total_emission_datamatch),
    path('analysing_data_home/',views.analysing_data_home),
    path('Hemission/',views.Hemission),
    path('analysing_data_industry/',views.analysing_data_industry),
    path('dummy/', views.dummy),
    path('data_logout/',views.data_logout),
    path('view_home_analyse/',views.view_home_analyse),
    path('start_process/',views.start_process),
    path('analyse_process/',views.analyse_process),
    path('analyst_calculate/<int:id>/',views.analyst_calculate),
]

