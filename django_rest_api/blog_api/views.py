from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


# view qui permet de créer
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


# view qui permet de get et delete des items
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer