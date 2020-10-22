from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login, name = 'login'),
    path('logout/',views.logout,name = 'logout'),
    path('signup/',views.signup, name = 'signup'),
    path('show/',views.show),
    path('get/ajax/validate/nickname', views.teamname_check, name = "teamname_check"),
]
