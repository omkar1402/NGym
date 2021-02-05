from . import views
from django.contrib import admin 
from django.urls import path, include 


urlpatterns = [
    path('',views.home,name='home'),
    path('bulky/',views.bulky,name="bulky"),
    path('lean/',views.lean,name="lean"),
    path('maintain/',views.maintain,name="maintain"),    
    path('gain/',views.gain,name="gain"),
    path('loss/',views.loss,name="loss"),
    path('diet_maintain/',views.diet_maintain,name="diet_maintain"),

    path('register/',views.register_page,name="register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),

    path('chest/', views.chest, name="chest"),
    path('back/', views.back, name="back"),
    path('shoulder/', views.shoulder, name="shoulder"),
    path('bicep/', views.bicep, name="bicep"),
    path('tricep/', views.tricep, name="tricep"),
    path('legs/', views.legs, name="legs"),
    path('chest_back/', views.chest_back, name="chest_back"),
    path('shoulder_legs/', views.shoulder_legs, name="shoulder_legs"),
    path('bicep_tricep/', views.bicep_tricep, name="bicep_tricep"),
    path('push/', views.push, name="push"),
    path('pull/', views.pull, name="pull"),

    path('fruits/',views.fruits,name='fruits'),
    path('heavy/', views.heavy, name='heavy'),
    path('light/', views.light, name='light'),

    # path('meal/',views.meal,name='meal'),

    path('list/',views.employee_list,name='list'),
    path('employee_form/<int:id>/',views.employee_form, name='update'),        #get and post for update
    path('employee_form/',views.employee_form, name ='insert'),     #get and post for insert
    path('employee_delete/<int:id>',views.employee_delete, name ='delete'),
]
