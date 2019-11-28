from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('addstudent/', views.addstudent, name="addstudent"),
    path('allstudents/', views.allstudents, name="allstudents"),
]
