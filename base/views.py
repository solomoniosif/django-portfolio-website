from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        return context


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'
    # redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('base:homepage')
