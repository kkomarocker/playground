from django.urls import path, include

urlpatterns = [
    path('', include('playground_backend.urls')),
    path('', include('accounts.urls')),
]
