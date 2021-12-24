"""FinmatProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import json
# with open('price.json') as data_file:
#     data_loaded = json.load(data_file)
#     # data_loaded = list(data_loaded)
#     print(data_loaded)
# from FinmatProject import
from django.contrib import admin
from django.urls import  path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # path('price', include(data_loaded)),
]
