from .models import Article, Comment
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import ArticleSerializer, CommentSerializer

# pylint: disable=maybe-no-member


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return self.request.user.articles.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer
