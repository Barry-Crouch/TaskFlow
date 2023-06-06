from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('project_view/', views.ProjectView.as_view(), name='project_view'),
]
