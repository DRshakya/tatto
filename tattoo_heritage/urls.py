from django.urls import path
from . import views

app_name = 'heritage'

urlpatterns = [
    path('artists/', views.disp_artist, name='disp_artist'),
    path('addartist/', views.add_artist, name='add_artist'),
    path('', views.user_login, name='user_login'),
    path('viewwork/', views.view_work, name='view_work'),
    path('gal1', views.add_gal1, name='gal1'),
    path('addwork', views.add_work, name='addwork'),
    path('delgal', views.del_gal, name='del_gal'),
    path('delwork', views.del_work, name='del_wrk'),
    path('updateartist', views.update_artist, name='update_artist'),

]