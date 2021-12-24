from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('<str:tk>/<int:per>/<str:interval>', views.index, name='ticker-data'),
    path('about-us', views.about),
    path('refresh', views.refresh, name='refresh'),
]