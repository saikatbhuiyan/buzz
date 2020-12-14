from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('post/', views.create_post, name='create_post'),
    path('<int:pk>', views.update_post, name='update_post'),
    path('upload/<int:pk>', views.upload_file, name='upload'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
