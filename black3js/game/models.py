from django.db import models
# Create your models here.
from django.template.defaultfilters import slugify

class Game(models.Model):
    total_players = models.IntegerField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.id
    class Meta:
    	verbose_name= "Game"
    	verbose_name_plural = 'Games'
    	db_table = "game"

class Players(models.Model):
	game = models.ForeignKey(Game, related_name='players')
	name = models.CharField(max_length=10, verbose_name="Player Name")
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name= "Player"
		verbose_name_plural = 'Players'
		db_table = "players"

class Score(models.Model):
	game = models.ForeignKey(Game)
	name = models.ForeignKey(Players, related_name='scores')
	score = models.IntegerField(max_length=10)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.score
	class Meta:
		verbose_name= "score"
		verbose_name_plural = 'Scores'
		db_table="score"
