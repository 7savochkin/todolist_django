from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from base.mixins.view_mixin import RequestFormViewMixin
from users.forms import SignInForm, SignUpForm


class MainPageView(TemplateView):
    template_name = 'main/index.html'


class SignInView(RequestFormViewMixin):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm
    success_url = reverse_lazy('menu')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('menu'))
        return super().get(request, *args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(request=self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class SignUpView(RequestFormViewMixin):
    template_name = 'auth/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('menu')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('menu'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
