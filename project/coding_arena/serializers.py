from rest_framework_json_api import serializers
from coding_arena.models import Gamer, Invite, Challenge

class GamerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gamer
        fields =(
            "user_id",
            "name",
            "prog_lang",
            "username",
            "email",
        )

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Challenge
        fields =(
            "title",
            "description",
            "createdBy", 
            "dateTimeCreated",
        )

class InviteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Invite
       fields = (
           "challengeID",
           "recipient",
           "dateTimeCreated",
           "status", 
       )

