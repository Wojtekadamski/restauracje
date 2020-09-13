"""restauracje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from restauracja_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_restaurant/', views.add_restaurant),
    path("", views.show_all),
    path("restauracja_info/<int:id>/", views.show_info),
    path('add_type/', views.add_types),
    path('types/', views.show_types)

]
