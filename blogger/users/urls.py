from django.urls import path

from users.api import views

urlpatterns = [
    path('<int:pk>/', views.user_get, name='get'),
    path('create/', views.user_create, name='create'),
    path('me/', views.me, name='me'),
    path('me/update/', views.user_update, name='update'),
    path('', views.user_list, name='list'),
]

app_name = 'users'
