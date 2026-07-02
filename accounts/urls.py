from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy

from accounts.views import UserRegisterView, CustomLogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html', ), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view(
        email_template_name='accounts/password-reset.html',
success_url = reverse_lazy('accounts:password_reset_done')
    ), name='password-reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
            template_name='accounts/password-reset-done.html'),
             name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='accounts/password-reset-confirm.html'),
            name='password-reset-confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='accounts/password-reset-complete.html'),
         name='password-reset-complete'),
    path('password-change/',PasswordChangeView.as_view(
             template_name='accounts/password-change.html',
             success_url=reverse_lazy('accounts:password-change-done')
         ),
         name='password-change'),

    # 2. Confirmation page
    path('password-change/done/',PasswordChangeDoneView.as_view(template_name='accounts/password-change-done.html'),
         name='password-change-done'),

]