"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import profile
from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('awwards.urls')),

    # api paths
    path('api/projects/',views.get_projects_data,name='projects'),
    path('api/profiles/',views.get_profiles_data,name='profiles'),


    # singe items
    path('api/project/<int:pk>/',views.ProjectDetailAPIView.as_view(),name='single_project'),
    path('api/profile/<int:pk>/',views.ProfileDetailAPIView.as_view(),name='single_profile'),
    
]
