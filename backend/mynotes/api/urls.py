from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('note/<str:pk>/', views.getNote),
    path('create-note/', views.createNote),
    path('delete-note/<str:pk>/', views.deleteNote),
    path('update-note/<str:pk>/', views.updateNote),
]