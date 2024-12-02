from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('CalculationPower/',views.CalculationPower,name="CalculationPower"),
    path('',views.CalculationPower,name="CalculationPower")
]
