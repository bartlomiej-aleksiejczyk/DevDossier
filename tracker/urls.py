from django.urls import path

from .views import (
    app_list, app_create, app_detail, app_edit, app_delete,
    entry_list, entry_detail, entry_create, entry_edit, entry_delete,
)

urlpatterns = [

    path('app/', app_list, name='app_list'),
    path('app/create/', app_create, name='app_create'),
    path('app/<int:pk>/', app_detail, name='app_detail'),
    path('app/<int:pk>/edit/', app_edit, name='app_edit'),
    path('app/<int:pk>/delete/', app_delete, name='app_delete'),

    # Entry endpoints
    path('app/<int:app_pk>/entry/', entry_list, name='entry_list_for_app'),
    path('app/<int:app_pk>/entry/create/', entry_create, name='entry_create_for_app'),
    path('app/<int:app_pk>/entry/<int:pk>/', entry_detail, name='entry_detail'),
    path('app/<int:app_pk>/entry/<int:pk>/edit/', entry_edit, name='entry_edit'),
    path('app/<int:app_pk>/entry/<int:pk>/delete/', entry_delete, name='entry_delete'),

]
