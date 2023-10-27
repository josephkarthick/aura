"""aio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from asset import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path ('itaasetlist/', views.itassetlist, name='itassetlist'),
    path('add_asset/', views.add_asset, name='add_asset'),
    path('editasset/', views.editasset, name='editasset'),
    path('edit_asset/', views.editasset, name='edit_asset'),
    path('edit_asset/<sno>', views.edit_asset, name='edit_asset'),
    path('delete_asset/<sno>', views.delasset, name='delete_asset'),
    
    path('search/<id>', views.search, name='search'),
    path ('addvoip', views.addvoip, name='addvoip'),
    path ('voiplist', views.voiplist, name='voiplist'),
    path ('editvoip', views.editvoip, name='editvoip'),
    path ('edit_voip/<sno>', views.edit_voip, name='edit_voip'),
    path('delete_voip/<sno>', views.delvoip, name='delete_voip'),
    path ('', views.login, name="login"),
    path('logout', views.logout_view, name='logout'),
    
    path('download-excel/', views.download_excel, name='download-excel'),
    path('voip_ex/', views.voip_ex, name='voip_ex'),
    path('pdf/<sno>', views.pdf, name='pdf'),
    
]