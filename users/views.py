from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from users.forms import SignInForm


class MainPageView(TemplateView):
    template_name = 'main/index.html'


class SignInView(FormView):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        ...

    def form_invalid(self, form):
        ...
