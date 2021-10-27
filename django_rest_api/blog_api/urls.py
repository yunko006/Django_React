from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    # show a detail view of a post
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    # show all the post
    path('', PostList.as_view(), name='listcreate'),
]