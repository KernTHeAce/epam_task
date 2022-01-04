from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about),
    path('department/', views.department),
    path('employee/', views.employee),
]