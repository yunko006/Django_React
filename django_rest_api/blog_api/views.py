from rest_framework import generics
from rest_framework import permissions
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, DjangoModelPermissions


class PostUserWritePermission(BasePermission):
    message = "Editing posts is rstricted to the author only."

    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

# view qui permet de créer
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


# view qui permet de get et delete des items
class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    # add the new permission to allow only author to edit object
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer