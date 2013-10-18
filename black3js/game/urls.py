from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from game import views

urlpatterns = patterns('',
	#url(r'^/$', views.GameList.as_view(), name='game-list'),
    url(r'^game/$', views.GameList.as_view(), name='game-list'),
    url(r'^game/(?P<pk>[0-9]+)/$', views.GameDetail.as_view(), name='game-detail'),
   	#url(r'^game/(?P<pk>[0-9]+)/players/$', views.GamePlayerDetail.as_view(), name='game-player-detail'),
   	url('^gameplayer/(?P<game_id>[0-9]+)/$', views.GamePlayerList.as_view()),

    url(r'^players/$', views.PlayersList.as_view(), name='player-list'),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayersDetail.as_view(), name='players-detail'),
    
    url(r'^score/$', views.ScoreList.as_view(), name='score-list'),
	url(r'^score/(?P<pk>[0-9]+)/$', views.ScoreDetail.as_view(), name='score-detail'),
	url('^gameplayerscore/(?P<game_id>[0-9]+)/$', views.GamePlayerScoreList.as_view()),
	url('^playerscore/(?P<game_id>[0-9]+)/(?P<player_id>[0-9]+)/$', views.PlayerScoreList.as_view()),

  
)


urlpatterns = format_suffix_patterns(urlpatterns)