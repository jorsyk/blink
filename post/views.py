from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .services import get_post_by_id, toggle_like


class PostListCreateView(ListCreateAPIView):
    """Список всех постов"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikePostView(APIView):
    """Добаление лайка на пост"""

    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_post_by_id(post_id)
        message = toggle_like(request.user, post)
        return Response({'message': message})
