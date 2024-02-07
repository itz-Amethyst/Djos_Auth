from django.urls import path

from core.api.views.login import LoginUserView
from core.api.views.user_info import MyUserInfoView

urlpatterns = [
    path("login/", LoginUserView.as_view(), name='login'),
    path('users/me/custom', MyUserInfoView.as_view(), name='my_user_info'),
]