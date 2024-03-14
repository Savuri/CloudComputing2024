from django.urls import path, re_path
from . import views

app_name = 'url'


urlpatterns = [
    path('', views.home, name='home'),
    path('error', views.error, name='error'),
    path('<str:short_url>', views.redirect_by_shortening),
]
