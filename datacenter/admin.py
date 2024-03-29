from django.contrib import admin

# Register your models here.

from datacenter.models import TeamName
from datacenter.models import Player, PlayerName, PlayerNation, PlayerPosition 
from datacenter.models import Season
from datacenter.models import DateMonth, DateWeekday
from datacenter.models import Match


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['season', 'description']
    ordering = ['-season']

    class Meta:
        model = Season


class PlayerNationAdmin(admin.ModelAdmin):
    list_display = ['nation']
    search_fields = ['nation']

    class Meta:
        model = PlayerNation


class PlayerNameAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    class Meta:
        model = PlayerName


class PlayerPositionAdmin(admin.ModelAdmin):
    list_display = ['position']
    search_fields = ['position']

    class Meta:
        model = PlayerPosition


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'player_back_number', 'player_nation']
    search_fields = ['player_name__name', 'player_nation__nation']
    autocomplete_fields = ['player_name', 'player_nation']
    ordering = ['player_name']

    class Meta:
        model = Player


class TeamNameAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    class Meta:
        model = TeamName


class DateMonthAdmin(admin.ModelAdmin):
    list_display = ['month']

    class Meta:
        model = DateMonth


class DateWeekdayAdmin(admin.ModelAdmin):
    list_display = ['weekday']

    class Meta:
        model = DateWeekday


class MatchAdmin(admin.ModelAdmin):
    list_display = ['season', 'match_date', 'teams', 'position', 'win_rate', 'season_goal_conceded', 'clean_sheet', 'change_created', 'score', 'result']
    autocomplete_fields = ['home_team_player_1', 'home_team_player_2', 'home_team_player_3', 'home_team_player_4',
                           'home_team_player_5', 'home_team_player_6', 'home_team_player_7', 'home_team_player_8',
                           'home_team_player_9', 'home_team_player_10', 'home_team_player_11', 'home_team_player_sub_1',
                           'home_team_player_sub_2', 'home_team_player_sub_3', 'home_team_player_sub_4', 'home_team_player_sub_5',
                           'home_team_player_sub_6', 'home_team_player_sub_7',
                           'away_team_player_1', 'away_team_player_2', 'away_team_player_3', 'away_team_player_4',
                           'away_team_player_5', 'away_team_player_6', 'away_team_player_7', 'away_team_player_8',
                           'away_team_player_9', 'away_team_player_10', 'away_team_player_11', 'away_team_player_sub_1',
                           'away_team_player_sub_2', 'away_team_player_sub_3', 'away_team_player_sub_4', 'away_team_player_sub_5',
                           'away_team_player_sub_6', 'away_team_player_sub_7',
                           'home_team_name', 'away_team_name']
    search_fields = ['season', 'home_team_name', 'away_team_name']
    list_per_page = 15


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
            away_team_formation = '%s-%s' % (away_team_formation, obj.away_team_line_6_count)
        return '%s : %s' % (home_team_formation, away_team_formation)

    def position(self, obj):
        try:
            return '%s' % (- int(obj.home_position) + int(obj.away_position))
        except:
            return ''

    def win_rate(self, obj):
        try:
            return '%.2f' % ((float(obj.home_won) / (float(obj.home_won) + float(obj.home_drawn) + float(obj.home_lost))) - (float(obj.away_won) / (float(obj.away_won) + float(obj.away_drawn) + float(obj.away_lost))))
        except:
            return ''

    def season_goal_conceded(self, obj):
        try:
            return '%.2f' % (((float(obj.home_avg_goal) - float(obj.home_avg_conceded))) - ((float(obj.away_avg_goal) - float(obj.away_avg_conceded))))
        except:
            return ''

    def clean_sheet(self, obj):
        try:
            return '%s' % (int(obj.home_clean_sheet) - int(obj.away_clean_sheet))
        except:
            return ''

    def change_created(self, obj):
        try:
            return '%.2f' % (float(obj.home_change_created) - float(obj.away_change_created))
        except:
            return ''

    def result(self, obj):
        try:
            if int(obj.home_team_goal) > int(obj.away_team_goal):
                return 'H'
            elif int(obj.home_team_goal) == int(obj.away_team_goal):
                return 'D'
            elif int(obj.home_team_goal) < int(obj.away_team_goal):
                return 'A'
        except:
            return ''

    position.short_description = '순위차이 (-)'
    win_rate.short_description = '승률차이 (+)'
    season_goal_conceded.short_description = '골득실차이 (+)'
    clean_sheet.short_description = '무실점경기차이 (+)'
    change_created.short_description = '찬스차이 (+)'



admin.site.register(Match, MatchAdmin)
admin.site.register(TeamName, TeamNameAdmin)

admin.site.register(DateMonth, DateMonthAdmin)
admin.site.register(DateWeekday, DateWeekdayAdmin)

admin.site.register(Season, SeasonAdmin)
admin.site.register(PlayerName, PlayerNameAdmin)
admin.site.register(PlayerNation, PlayerNationAdmin)
admin.site.register(PlayerPosition, PlayerPositionAdmin)
admin.site.register(Player, PlayerAdmin)
