from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/home.html']
        return ['common/landing_page.html']

