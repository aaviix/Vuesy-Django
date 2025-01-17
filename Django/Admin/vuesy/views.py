from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class DashboardView(LoginRequiredMixin,TemplateView):
    pass

dashboard_view = DashboardView.as_view(template_name ="index.html") 

class MyPasswordChangeView( PasswordChangeView):
    success_url = reverse_lazy("dashboard")


class MyPasswordSetView( PasswordSetView):
    success_url = reverse_lazy("dashboard")
