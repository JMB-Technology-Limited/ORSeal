from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug>/', views.project, name='project'),
    path('project/<slug>/organisation', views.organisation_list, name='organisation-list'),
]
