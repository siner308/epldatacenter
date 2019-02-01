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
    list_display = ['match_date', 'teams', 'score', 'formation']

    class Meta:
        model = Match

    def match_date(self, obj):
        return '%s %s %s %s' % (obj.match_date_weekday, obj.match_date_day, obj.match_date_month, obj.match_date_year)

    def teams(self, obj):
        return '%s vs %s' % (obj.home_team_name, obj.away_team_name)

    def score(self, obj):
        return '%s : %s' % (obj.home_team_goal, obj.away_team_goal)

    def formation(self, obj):
        home_team_formation = '%s-%s-%s' % (obj.home_team_line_1_count, obj.home_team_line_2_count, obj.home_team_line_3_count)
        if obj.home_team_line_4_count != '0':
            home_team_formation = '%s-%s' % (home_team_formation, obj.home_team_line_4_count)
        if obj.home_team_line_5_count != '0':
            home_team_formation = '%s-%s' % (home_team_formation, obj.home_team_line_5_count)
        if obj.home_team_line_6_count != '0':
            home_team_formation = '%s-%s' % (home_team_formation, obj.home_team_line_6_count)
        away_team_formation = '%s-%s-%s' % (obj.away_team_line_1_count, obj.away_team_line_2_count, obj.away_team_line_3_count)
        if obj.away_team_line_4_count != '0':
            away_team_formation = '%s-%s' % (away_team_formation, obj.away_team_line_4_count)
        if obj.away_team_line_5_count != '0':
            away_team_formation = '%s-%s' % (away_team_formation, obj.away_team_line_5_count)
        if obj.away_team_line_6_count != '0':
            away_team_formation = '%s-%s' % (away_team_formation, obj.away_team_line_5_count)
        return '%s : %s' % (home_team_formation, away_team_formation)


admin.site.register(Season, SeasonAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)
