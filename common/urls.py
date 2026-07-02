from django.urls import path
from common.views import HomeView, LandingPageView

app_name = 'common'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page' ),
    path('home/', HomeView.as_view(), name='home'),

]

