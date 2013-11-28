# Create your views here.
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from game.models import Game, Players, Score
from game.serializers import GameSerializer, PlayersSerializer, ScoreSerializer, GamePlayerSerializer, PlayersScoreSerializer, GamePlayerScoreSerializer
from chartit import DataPool, Chart
from django.shortcuts import render_to_response
from django.template import RequestContext




class GameList(generics.ListCreateAPIView):
    """
    List all games, or create a new game.
    """
    model = Game
    serializer_class = GameSerializer



class PlayersList(generics.ListCreateAPIView):
    """
    List all players, or create a new players.
    """
    model = Players
    serializer_class = PlayersScoreSerializer

class ScoreList(generics.ListCreateAPIView):
    """
    List all score, or create a new score.
    """
    model = Score
    serializer_class = ScoreSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a game instance.
    """
    model = Game
    serializer_class = GamePlayerScoreSerializer

class GamePlayerList(generics.ListCreateAPIView):
    """
    Retrieve, update or delete a game instance.
    """
    
    #queryset = Players.objects.all(game_id=data.game_id)
    model = Players
    #serializer_class = PlayersSerializer(queryset, data=data, many=True, allow_add_remove=True)
    #serializer.is_valid()
    #serializer.save() 

    def get_queryset(self):
        game = self.kwargs['game_id']
        return Players.objects.filter(game_id=game)

class GamePlayerScoreList(generics.ListCreateAPIView):
    """
    Retrieve, update or delete a game instance.
    """
    model = Score
    serializer_class = ScoreSerializer

    def get_queryset(self):
        game = self.kwargs['game_id']
        return Score.objects.filter(game_id=game)

class PlayerScoreList(generics.ListCreateAPIView):
    """
    Retrieve, update or delete a game instance.
    """
    model = Score
    serializer_class = ScoreSerializer

    def get_queryset(self):
        game = self.kwargs['game_id']
        player=self.kwargs['player_id']
        return Score.objects.filter(game_id=game, name_id=player)
    

    
class PlayersDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a players instance.
    """
    model = Players
    serializer_class = PlayersSerializer
    

class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a score instance.
    """
    model = Score
    serializer_class = ScoreSerializer
    

def chart(request, template_name="chart.html"):

    #total_score = Game.objects.filter(score__game_id__exact='17').get('')
    total_score = Game.objects.all()
    
    #select p.name, sum(s.score) as total_score from game g, players p, score s where g.id=17 and  g.id = p.game_id and p.id = s.name_id group by p.name 
#order by sum(s.score)


    return render_to_response(template_name, {'games':total_score}, context_instance=RequestContext(request))
    
