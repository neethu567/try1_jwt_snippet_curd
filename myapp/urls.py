from django.urls import path
from .views import *

app_name = "myapp"
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("login-token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("snippet/", SnippetListCreateAPIView.as_view(), name="snippet-list"),
    path("snippet/<int:pk>/", SnippetDetailAPIView.as_view(), name="snippet-detail"),
    path("tag/", TagListView.as_view(), name="tag-list"),
]
