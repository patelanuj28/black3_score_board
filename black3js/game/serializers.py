from rest_framework import serializers
from game.models import Game, Players, Score

class GameSerializer(serializers.ModelSerializer):
    api_url = serializers.SerializerMethodField('get_api_url')
    

    class Meta:
        model = Game
        fields = ('id', 'total_players', 'created_on', 'updated_on')
        read_only_fields = ('id', 'created_on')

    def get_api_url(self, obj):
        return "#/game/%s" % obj.id


class ScoreSerializer(serializers.ModelSerializer):
    api_url = serializers.SerializerMethodField('get_api_url')
    #game = GameSerializer
    #name = PlayersSerializer
    
    class Meta:
        model = Score
        fields = ('id', 'game','name', 'score', 'created_on', 'updated_on')
        read_only_fields = ('id','created_on')

    def get_api_url(self, obj):
        return "#/score/%s" % obj.id


class PlayersSerializer(serializers.ModelSerializer):
    api_url = serializers.SerializerMethodField('get_api_url')
    

    class Meta:
        model = Players
        fields = ('id', 'game','name', 'created_on', 'updated_on')
        read_only_fields = ('id', 'created_on')

    def get_api_url(self, obj):
        return "#/players/%s" % obj.id


class PlayersScoreSerializer(serializers.ModelSerializer):
    api_url = serializers.SerializerMethodField('get_api_url')
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Players
        fields = ('id', 'game','name', 'created_on', 'updated_on', 'scores')
        read_only_fields = ('id', 'created_on')

    def get_api_url(self, obj):
        return "#/players/%s" % obj.id


class GamePlayerSerializer(serializers.ModelSerializer):
    api_url = serializers.SerializerMethodField('get_api_url')
    players = PlayersSerializer(many=True, read_only=True)
    

    class Meta:
        model = Game
        fields = ('id', 'total_players', 'created_on', 'updated_on', 'players')
        read_only_fields = ('id', 'created_on')

    def get_api_url(self, obj):
        return "#/game/%s" % obj.id



class GamePlayerScoreSerializer(serializers.ModelSerializer):
    api_url = serializers.SerializerMethodField('get_api_url')
    players = PlayersScoreSerializer(many=True, read_only=True)
    

    class Meta:
        model = Game
        fields = ('id', 'total_players', 'created_on', 'updated_on', 'players')
        read_only_fields = ('id', 'created_on')

    def get_api_url(self, obj):
        return "#/game/%s" % obj.id

