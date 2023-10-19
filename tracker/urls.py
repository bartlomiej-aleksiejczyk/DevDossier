from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.app_list, name='app_list'),
    path('app/create/', views.app_create, name='app_create'),
    path('app/<int:pk>/', views.app_detail, name='app_detail'),
    path('app/<int:pk>/edit/', views.app_edit, name='app_edit'),
    path('app/<int:pk>/delete/', views.app_delete, name='app_delete'),
]