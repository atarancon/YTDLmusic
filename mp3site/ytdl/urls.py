from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name="list"),
    path('download/<pk>', views.download , name="download"),
    #path('download', views.download , name="download"),
]
