from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/', login, {'template_name': 'membership/login.html'}),
    path('logout/', logout, {'template_name': 'membership/logout.html'}),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile')
]
