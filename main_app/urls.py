from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user/<username>', views.profile, name='profile'),
    path('user/<int:user_id>/add_skill/', views.add_skill, name='add_skill'),
    
    
]