from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('u/registration', views.registration, name='registration'),
    path('u/login', views.login_view, name='login'),
    path('u/logout', views.logout_view, name='logout')
]