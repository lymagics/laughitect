from django.urls import path

from users.api import views

urlpatterns = [
    path('<int:pk>/', views.user_get, name='get'),
    path('<int:pk>/follow/', views.user_follow, name='follow'),
    path('<int:pk>/unfollow/', views.user_unfollow, name='unfollow'),
    path('<int:pk>/following/', views.user_following, name='following'),
    path('<int:pk>/followers/', views.user_followers, name='followers'),
    path('create/', views.user_create, name='create'),
    path('me/', views.me, name='me'),
    path('me/update/', views.user_update, name='update'),
    path('', views.user_list, name='list'),
]

app_name = 'users'
