from django.urls import path
from FinalProject.accounts.views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register user"),
    path('login/', LoginUserView.as_view(), name="login user"),
    path('logout/', LogoutUserView.as_view(), name="logout user"),
    path('profile_page/', ProfilePageUserView.as_view(), name="profile page user"),
]
