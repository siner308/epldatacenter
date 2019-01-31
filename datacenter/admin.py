from django.contrib import admin

# Register your models here.

from datacenter.models import Player, Match, Season


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['season', 'description']
    ordering = ['-season']
    class Meta:
        model = Season


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'player_back_number', 'player_nation']
    ordering = ['player_name']

    class Meta:
        model = Player


class MatchAdmin(admin.ModelAdmin):
    list_display = ['match_date', 'home_team_name', 'away_team_name']
    ordering = ['-match_date']

    class Meta:
        model = Match

    def teams(self, obj):
        return '%s vs %s' % (obj.home_team_name, obj.away_team_name)

    def score(self, obj):
        return '%s : %s' % (obj.home_team_goal, obj.away_team_goal)


admin.site.register(Season, SeasonAdmin)
admin.site.register(Player)
admin.site.register(Match)
