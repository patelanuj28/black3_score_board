from django.contrib import admin
from game.models import Game, Players, Score
from django.contrib.auth.models import User
from django.conf.urls import patterns, url
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core import serializers
from django.utils.html import strip_tags


class Game_Admin(admin.ModelAdmin):
	fieldsets = [
            (None, {'fields': ['total_players']}),
			]
	list_display = ('id', 'total_players', 'created_on', 'updated_on')
	search_fields = ['total_players', 'id']

admin.site.register(Game, Game_Admin)


class Players_Admin(admin.ModelAdmin):
	fieldsets = [
            (None, {'fields': [ 'game', 'name']}),
			]
	list_display = ('id', 'name', 'created_on', 'updated_on')
	search_fields = ['name', 'id']

admin.site.register(Players, Players_Admin)


class Score_Admin(admin.ModelAdmin):
	fieldsets = [
            (None, {'fields': [ 'game', 'name', 'score']}),
			]
	list_display = ('id', 'score', 'created_on', 'updated_on', 'game', 'name')
	search_fields = ['score', 'id']
	

admin.site.register(Score, Score_Admin)
