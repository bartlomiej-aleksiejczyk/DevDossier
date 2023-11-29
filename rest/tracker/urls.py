from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tracker.views.app_views import AppViewSet
from tracker.views.entry_views import EntryViewSet, AppEntriesView
from tracker.views.user_views import UserLoginView, UserRegistrationView, UserLogoutView, UserRoleView, UserCRUDViewSet

router = DefaultRouter()
router.register(r'users', UserCRUDViewSet)
router.register(r'apps', AppViewSet)
router.register(r'entries', EntryViewSet)


urlpatterns = [
    path('api/v1/', include([
        # User endpoints
        path('register/', UserRegistrationView.as_view(), name='register'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('logout/', UserLogoutView.as_view(), name='logout'),
        path('', include(router.urls)),
        # Entries of given App
        path('apps/<int:app_id>/entries/', AppEntriesView.as_view(), name='app-entries')
    ])),
]