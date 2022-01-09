from django.urls import path
from . import views

app_name = 'sign_app'

urlpatterns = [
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('validate', views.Validate, name='validate'),
    path('confirm', views.Confirm, name='confirm'),
]