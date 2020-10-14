from django.urls import path
from accounts import views
from django.conf import settings


urlpatterns = [
    path('register/', views.user_registration_view, name="register"),
    path('logout/', views.logout_view, name="log-out"),
    path('', views.login_request_view, name="login" ),
    path('validate-user/', views.check_username_exists, name="validate-username"),
    path('validate-username/', views.check_username_exists, name="check-username"),
]
