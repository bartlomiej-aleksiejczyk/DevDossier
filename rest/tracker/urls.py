from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tracker.views.app_views import AppViewSet
from tracker.views.attachment_views import AttachmentViewSet
from tracker.views.comment_views import CommentViewSet, EntryCommentsView
from tracker.views.entry_views import EntryViewSet, AppEntriesView, UserEntriesView
from tracker.views.user_views import UserLoginView, UserRegistrationView, UserLogoutView, UserRoleView, UserCRUDViewSet, UserRankingView

router = DefaultRouter()
router.register(r'users', UserCRUDViewSet)
router.register(r'apps', AppViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'attachments', AttachmentViewSet)

urlpatterns = [
    path('api/v1/', include([
        # Entry ranking of given user
        path('users/ranking/', UserRankingView.as_view(), name='user-ranking'),
        # User endpoints
        path('register/', UserRegistrationView.as_view(), name='register'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('logout/', UserLogoutView.as_view(), name='logout'),
        path('role/', UserRoleView.as_view(), name='role'),
        path('', include(router.urls)),
        # Entries of given App
        path('apps/<int:app_id>/entries/', AppEntriesView.as_view(), name='app-entries'),
        # Comment of given Entry
        path('entries/<int:entry_id>/comments/', EntryCommentsView.as_view(), name='entry-comments'),
        # Entries of given User
        path('users/<int:user_id>/entries/', UserEntriesView.as_view(), name='user-entries'),
    ])),
]