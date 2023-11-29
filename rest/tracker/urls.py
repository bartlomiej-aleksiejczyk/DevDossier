from django.urls import path

from tracker.views.user_views import UserLoginView, UserRegistrationView, UserLogoutView, UserRoleView

urlpatterns = [
    path('api/v1/', include([
        path('register/', UserRegistrationView.as_view(), name='register'),
        path('login/', UserLoginView.as_view(), name='login'),
        path('logout/', UserLogoutView.as_view(), name='logout'),
    ])),
]