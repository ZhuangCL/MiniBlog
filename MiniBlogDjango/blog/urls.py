from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('articles/', views.ArticleListView.as_view(), name = 'articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name = 'article-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name = 'bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name = 'blogger-detail'),
    path('myarticle/', views.MyArticleUserListView.as_view(), name = 'my-articles'),
    path('allarticle/', views.MyArticleAllUserListView.as_view(), name = 'all-articles'),
    path('register/', views.sign_up, name = 'register'),
    path('article/<int:pk>/update/', views.ArticleUpdate.as_view(), name = 'article_update'),
    path('article/<int:pk>/delete/', views.ArticleDelete.as_view(), name = 'article_delete'),
    path('blogger/<int:pk>/create/', views.ArticleCreate.as_view(), name = 'article_create'),
    path('article/<int:pk>/comment/create/', views.ArticleInstanceCreate.as_view(), name = 'comment_create'),
    path('article/<int:pk>/comment/delete/', views.ArticleInstanceDelete.as_view(), name = 'comment_delete'),
]