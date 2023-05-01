from django.urls import path

from users.views import MainPageView, SignInView, SignUpView

urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('main/', MainPageView.as_view(), name='index'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_up/', SignUpView.as_view(), name='sign_up')
]
