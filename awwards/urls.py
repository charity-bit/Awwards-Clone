from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    #  authentication
    path('',views.CustomLoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),


    
    path('home/',views.home,name='home'),
    # path('home/',views.cProjectListView.as_view(),name='home'),
    path('profile/<str:username>/',views.profile,name='profile'),
    path('submit/',views.AddProjectView.as_view(),name='submit'),
    

    # rate
    path('sites/rate/',views.rate,name='rate'),
    path('details/sites/<int:pk>/',views.ProjectDetailsView.as_view(),name='details'),


]

