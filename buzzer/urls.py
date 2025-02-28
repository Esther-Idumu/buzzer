from django.urls import path
from . import views
from . views import signup, login, logout, home

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:pk>/', views.profile_view, name='profile'),
    path('profile_list/', views.profile_list, name='profile_list'),

]
 
 
