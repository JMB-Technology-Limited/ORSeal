from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug>/', views.project, name='project'),
]
