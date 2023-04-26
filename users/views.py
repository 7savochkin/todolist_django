from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from users.forms import SignInForm, SignUpForm


class MainPageView(TemplateView):
    template_name = 'main/index.html'


class SignInView(FormView):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm
    success_url = reverse_lazy('index')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(request=self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        return super().form_valid(form)


class SignUpView(FormView):
    template_name = 'auth/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)
