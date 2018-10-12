from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('skills/', skill_list, name='skill_list'),
    path('skills/<int:pk>/', skill_detail, name='skill_detail'),
    path('skills/create/', SkillCreate.as_view(), name='skill_create'),

    # path('', HomeView.as_view(), name='home'),
    # path('skills/', SkillListView.as_view(), name='skill_list'),
    # path('skills/<int:pk>/', SkillDetailView.as_view(), name='skill_detail'),
    # path('skills/create/', SkillCreate.as_view(), name='skill_create'),

]