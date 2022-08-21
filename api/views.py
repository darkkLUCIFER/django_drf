# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUserOrStaffOrReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly

from rest_framework.viewsets import ModelViewSet


# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffOrReadOnly,)


# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffOrReadOnly,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def delete(self, request):
#         request.user.auth_token.delete()
#         return Response(status=204)

class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filterset_fields = ['status', 'author__username']
    search_fields = ['title', 'content', 'author__first_name', 'author__last_name']
    ordering_fields = ['publish', 'status']

    # def get_queryset(self):
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #
    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author__username=author)
    #
    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsSuperUserOrStaffOrReadOnly']
