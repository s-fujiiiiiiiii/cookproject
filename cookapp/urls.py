from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView
from .views import PostListView, SearchResultsView


app_name = 'cookapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog-detail/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('post/create/', views.BlogPostCreateView.as_view(), name='post_create'),
    path('post/success/', views.BlogPostSuccessView.as_view(), name='post_success'),
 path('posts/', PostListView.as_view(), name='post_list'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('user-list/<int:user>/', views.UserView.as_view(), name='user_list'),
    path('mypage/', views.MyPageView.as_view(), name='mypage'),
    path('post/delete/<int:pk>/', views.BlogPostDeleteView.as_view(), name='post_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)