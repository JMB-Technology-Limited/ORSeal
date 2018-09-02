from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<slug>/', views.project, name='project'),
    path('project/<slug>/organization', views.organization_list, name='organization_list'),
    path('project/<slug>/organization/<id>', views.organization_show, name='organization_show'),
]
