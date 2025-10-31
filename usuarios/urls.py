from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.vista_registro, name='registro'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('check-username/', views.check_username, name='check-username'),
]