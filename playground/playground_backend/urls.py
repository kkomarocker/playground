from rest_framework import routers
from .api import ArticleViewSet, CommentViewSet
from django.urls import path, include
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('api/article', ArticleViewSet, 'articles')
router.register('api/comment', CommentViewSet, 'comments')


urlpatterns = router.urls
