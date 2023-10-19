from django.urls import path
from .views import app_list, app_detail, app_create, app_edit, app_delete


urlpatterns = [
    path('app/', app_list, name='app_list'),
    path('app/create/', app_create, name='app_create'),
    path('app/<int:pk>/', app_detail, name='app_detail'),
    path('app/<int:pk>/edit/', app_edit, name='app_edit'),
    path('app/<int:pk>/delete/', app_delete, name='app_delete'),
]