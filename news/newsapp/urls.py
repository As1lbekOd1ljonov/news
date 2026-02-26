from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import NewsListView, NewsDetailView, CategoryNewsListView, RegisterView, Login, ToggleLikeView, ProfileView, \
    SavedNewsListView, ToggleSaveView, NewsDeleteView, NewsCreateView, NewsUpdateView, ProfileUpdateView, \
    NewsSearchView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('', NewsListView.as_view(), name='home' ),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('like/<int:pk>/', ToggleLikeView.as_view(), name='like_news'),
    path('save/<int:pk>/', ToggleSaveView.as_view(), name='save_news'),
    path("saved/", SavedNewsListView.as_view(), name="saved_news"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('category/<int:pk>/', CategoryNewsListView.as_view(), name='category_news'),
    path('news/detail/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('create/category', CategoryCreateView.as_view(), name='category_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('search/', NewsSearchView.as_view(), name='news-search'),
]

