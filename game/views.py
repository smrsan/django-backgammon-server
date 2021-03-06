from django.contrib.auth.models import User

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Game, Board, Turn
from .serializers import UserSerializer, GameSerializer, BoardSerializer, TurnSerializer
from .permissions import HasAccessToGame, HasAccessToGameRelatedModels


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GameViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, HasAccessToGame]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated, HasAccessToGameRelatedModels]

    def get_queryset(self):
        return Board.objects.get(game=self.kwargs['game_pk'])


class TurnViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer
    permission_classes = [IsAuthenticated, HasAccessToGameRelatedModels]

    def get_queryset(self):
        return Turn.objects.filter(game=self.kwargs['game_pk'])


@api_view(['GET'])
def GameWsResponseTypes(request, format=None):
    return Response({})


@api_view(['GET'])
def ChatWsResponseTypes(request, format=None):
    return Response({})
