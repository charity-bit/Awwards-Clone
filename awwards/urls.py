from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    #  authentication
    path('',views.CustomLoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),


    
    path('home/',views.home,name='home'),
    path('profiel/<str:username>/',views.profile,name='profile')

]
