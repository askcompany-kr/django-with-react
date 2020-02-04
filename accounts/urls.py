from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
]
