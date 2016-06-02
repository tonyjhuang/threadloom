from django.contrib.auth.models import User
from forum.models import *
from forum.permissions import *
from forum.serializers import *
from rest_framework import filters, generics, mixins, permissions, viewsets
from rest_framework.decorators import detail_route

class TopicViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    'list', 'create', 'retrieve', 'update', 'destroy'.

    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ThreadViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    'list', 'create', 'retrieve', 'update', 'destroy'.

    """
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('topic',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ReplyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    'list', 'create', 'retrieve', 'update', 'destroy'.

    """
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('thread',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (NotAuthenticatedCreateOrReadOnly,
                          IsSameUserOrReadOnly,)
