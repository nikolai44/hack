"""hack URL Configuration

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
from suppliers.views import home_view, add_facture, get_id, add_geodata

urlpatterns = [
    path('get_info/<int:uid>', get_id, name='get_info'),
    path('admin/', admin.site.urls),
    path('add_facture', add_facture, name='add_facture'),
    path('', home_view, name='home'),
    path('geo/add', add_geodata, name='home')
]
