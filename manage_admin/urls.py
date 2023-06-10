from . import views
from django.urls import path

urlpatterns = [

    path('', views.admin_home_index),
    path('m_login/', views.m_login),
    path('admin_homepage/', views.admin_homepage),
    path('admin_login/', views.admin_login),
    path('admin_logout/', views.admin_logout),
    path('basic_calc/', views.basic_calc),
    path('process_admin/', views.process_admin),
    path('admincalcu_save/', views.admincalcu_save),
    path('calc_emission/<int:id>/', views.calc_emission),
    path('admin_view/', views.admin_view),
    path('data_table _admin/', views.data_table_admin),
    path('data_table_home/', views.data_table_home),
    path('data_table_industry/', views.data_table_industry),
    path('send_analyse/<int:id>/', views.send_analyse),
    path('send_analyse_industry/<int:id>/', views.send_analyse_industry),
    path('graph_10/', views.graph_1),
    path('graph_2/', views.graph_2),
    path('graph_3/', views.graph_3),
    path('report/', views.report),

]
