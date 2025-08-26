from django.urls import path

from api_v2.views import (
    get_token_view, ArticleView, CommentListCreateView, CommentDetailView)

app_name = 'v2'

urlpatterns = [
    path('get-csrf/', get_token_view, name='get-csrf'),

    path('articles/', ArticleView.as_view(), name='articles'),
    path('articles/<int:pk>/', ArticleView.as_view(), name='article'),

    path('articles/<int:article_id>/comments/', CommentListCreateView.as_view(), name='article-comments'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment'),
]
