from django.urls import path

from users.api import views

urlpatterns = [
    path('<int:user_id>/', views.user_get, name='get'),
    path('create/', views.user_create, name='create'),
    path('me/', views.me, name='me'),
]

app_name = 'users'
