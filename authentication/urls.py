from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from authentication import views
from authentication.views import LoginUser, RegisterUser, ResetPasswordView

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),

]
