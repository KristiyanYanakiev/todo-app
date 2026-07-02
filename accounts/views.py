from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

UserModel = get_user_model()

class UserRegisterView(UserPassesTestMixin, CreateView):

    model = UserModel
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('common:home')

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.warning(self.request, "You are already logged in.")
        return redirect('common:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)

        return response
class CustomLogoutView(LoginRequiredMixin, LogoutView):

    template_name = 'accounts/logout.html'
    http_method_names = ["get", "post", "options"]
    next_page = reverse_lazy('accounts:login')


