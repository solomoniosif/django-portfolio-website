from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:homepage'), name='logout'),
]
