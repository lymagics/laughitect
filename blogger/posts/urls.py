from django.urls import path

from posts.api import views

urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('<int:pk>/', views.post_get, name='get'),
    path('<int:pk>/update/', views.post_update, name='update'),
    path('', views.post_list, name='list'),
]

app_name = 'posts'
