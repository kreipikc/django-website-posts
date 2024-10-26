from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('u/registration', views.registration, name='registration'),
    path('u/login', views.login_view, name='login'),
    path('u/logout', views.logout_view, name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post'),
]