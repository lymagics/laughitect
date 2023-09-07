from django.urls import path

from posts.api import views

urlpatterns = [
    path('<int:pk>/', views.post_get, name='get'),
]

app_name = 'posts'
