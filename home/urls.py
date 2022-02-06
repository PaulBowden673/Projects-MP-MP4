from django.urls import path
from home.views import AboutView, ContactView, LivehealthyView, GainweightView, LoseweightView, EnduranceView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('lose-weight/', LoseweightView.as_view(), name='lose-weight'),
    path('gain-weight/', GainweightView.as_view(), name='gain-weight'),
    path('endurance/', EnduranceView.as_view(), name='endurance'),
    path('live-healthy/', LivehealthyView.as_view(), name='live-healthy'),
    path('contact/', ContactView.as_view(), name='contact'),
]
