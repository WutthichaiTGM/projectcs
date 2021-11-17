# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('details', views.index, name='details'),
    # path('', views.dashboardView, name="dashboardView"),
    path('dashboard/', views.dashboardView, name="dashboardView"),
    # path('dashboard/details', views.dashboardView, name='details'),
    path('register/', views.register, name="register_url"),
    path('<int:id>/', views.student_form, name='form_update'),
    path('delete/<int:id>/',views.student_delete,name='form_delete'),
    path('show/',views.student_show,name='form_list'),
    
    # school
    path('school/',views.school,name='school'),
    path('admissions/',views.admissions, name='admissions'),
    path('Student/', views.viewdatastudent,name="ShowDataStudent"),


    # Form
    path('addDataStudent/',views.student_form,name='form_insert'),
    # Upload
    path('upload/',views.uploadcsv, name='uploadcsv'),
    # JSON
    path('json/',views.json,name='json'),
    # Predictions
    path('Predict/',views.Predict, name='Predict'),






    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
