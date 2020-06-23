from django.shortcuts import render
from coding_arena.models import Gamer, Invite, Challenge
from coding_arena.serializers import GamerSerializer, InviteSerializer, ChallengeSerializer
from rest_framework import viewsets

# Create your views here.

class GamerViewSet(viewsets.ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer


class InviteViewSet(viewsets.ModelViewSet):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

