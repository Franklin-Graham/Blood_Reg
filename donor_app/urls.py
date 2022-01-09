from django.urls import path
from . import views

app_name = 'donor_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('donate', views.donate, name='donate'),
]