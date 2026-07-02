from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'common/home.html'


class LandingPageView(TemplateView):
    template_name = 'common/landing_page.html'