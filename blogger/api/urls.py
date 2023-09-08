from django.urls import include, path

urlpatterns = [
    path('auth/', include('auth.urls')),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
]

app_name = 'api'
