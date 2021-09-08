from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/', views.download_video, name='download'),
    path('fdownload',views.facebook,name='fdownload'),
    path('facebook/',views.facebook,name='facebook'),
]