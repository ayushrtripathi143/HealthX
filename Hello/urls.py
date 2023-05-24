"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='home'),
    path("new",views.new,name="new"),
    path("teamsignup",views.teamsignup,name="teamsignup"),
    path("appointment",views.appointment,name="appointment"),
    path("temp_nav",views.temp_nav,name="team_nav"),
    path("button",views.button,name="button"),
    path("maps",views.maps,name="maps"),
    path("signup",views.signup,name="signup"),
    path("second_main",views.second_main,name="second_main"),
    path("staff_login",views.staff_login,name="staff_login"),
    path("admin_login",views.admin_login,name="admin_login"),
    path("confirm_appoint",views.confirm_appoint,name="confirm_appoint"),
    path("consulting_landing",views.consulting_landing,name="consulting_landing"),
    path("Thankyou",views.ThankYou,name="Thankyou"),
    path("second_page",views.second_page,name="second_page"),
    path("admin_dashboard",views.admin_dashboard,name="admin_dashboard"),
    path("doctors_dashboard",views.doctors_dashboard,name="doctors_dashboard"),
    path("chatbot",views.chatbot,name="chatbot"),
    path("Add_hospital",views.add_hospital,name="Add_hospital"),
    path("medicine_remainder",views.medicine_remainder,name="medicine_remainder"),
    path("view_appoitments",views.view_appointment,name="view_appoitments"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("date",views.date,name='date'),
    path("about",views.about,name='about'),
    path("launch_project2/",views.launch_project2,name="launch_project2"),
]
