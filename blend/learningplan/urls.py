from django.urls import path
from . import views

urlpatterns = [
    path('', views.getLearningPlanData, name='getLearningPlanData'),
]