from django.db import models
# Create your models here.


class Season(models.Model):
    season = models.CharField(max_length=100, blank=True)
    html = models.TextField(blank=True)
    description = models.TextField(blank=True)


class PlayerNation(models.Model):
    nation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nation


class PlayerName(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class PlayerPosition(models.Model):
    position = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.position


class Player(models.Model):
    player_name = models.ForeignKey(PlayerName, on_delete=models.CASCADE, null=True)
    player_nation = models.ForeignKey(PlayerNation, on_delete=models.CASCADE, null=True)
    player_back_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s (%s, %s)' % (self.player_name, self.player_nation, self.player_back_number)


class TeamName(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class DateMonth(models.Model):
    month = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.month


class DateWeekday(models.Model):
    weekday = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.weekday


class Match(models.Model):
    season = models.CharField(max_length=100, blank=True)
    # match date
    match_date_day = models.CharField(max_length=100, blank=True)
    match_date_month = models.ForeignKey(DateMonth, on_delete=models.CASCADE, null=True)
    match_date_weekday = models.ForeignKey(DateWeekday, on_delete=models.CASCADE, null=True)
    match_date_year = models.CharField(max_length=100, blank=True)
    # home team name
    home_team_name = models.ForeignKey(TeamName, on_delete=models.CASCADE, null=True, related_name='home_team_name')
    # home team goal
    home_team_goal = models.CharField(max_length=100, blank=True)
    # home team players
    home_team_player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_1')
    home_team_player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_2')
    home_team_player_3 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_3')
    home_team_player_4 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_4')
    home_team_player_5 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_5')
    home_team_player_6 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_6')
    home_team_player_7 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_7')
    home_team_player_8 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_8')
    home_team_player_9 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_9')
    home_team_player_10 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_10')
    home_team_player_11 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_11')
    # home team substitutes
    home_team_player_sub_1 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_1')
    home_team_player_sub_2 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_2')
    home_team_player_sub_3 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_3')
    home_team_player_sub_4 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_4')
    home_team_player_sub_5 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_5')
    home_team_player_sub_6 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_6')
    home_team_player_sub_7 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_7')
    # goalkeeper, defender, midfielder, forward
    home_team_player_1_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_1_position')
    home_team_player_2_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_2_position')
    home_team_player_3_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_3_position')
    home_team_player_4_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_4_position')
    home_team_player_5_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_5_position')
    home_team_player_6_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_6_position')
    home_team_player_7_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_7_position')
    home_team_player_8_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_8_position')
    home_team_player_9_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_9_position')
    home_team_player_10_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_10_position')
    home_team_player_11_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_11_position')
    # home team substitutes' position
    home_team_player_sub_1_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_1_position')
    home_team_player_sub_2_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_2_position')
    home_team_player_sub_3_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_3_position')
    home_team_player_sub_4_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_4_position')
    home_team_player_sub_5_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_5_position')
    home_team_player_sub_6_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_6_position')
    home_team_player_sub_7_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='home_team_player_sub_7_position')
    # count of position
    home_team_line_1_count = models.CharField(max_length=100, blank=True)
    home_team_line_2_count = models.CharField(max_length=100, blank=True)
    home_team_line_3_count = models.CharField(max_length=100, blank=True)
    home_team_line_4_count = models.CharField(max_length=100, blank=True)
    home_team_line_5_count = models.CharField(max_length=100, blank=True)
    home_team_line_6_count = models.CharField(max_length=100, blank=True)
    # season data
    home_position = models.CharField(max_length=100, blank=True)
    home_won = models.CharField(max_length=100, blank=True)
    home_drawn = models.CharField(max_length=100, blank=True)
    home_lost = models.CharField(max_length=100, blank=True)
    home_avg_goal = models.CharField(max_length=100, blank=True)
    home_avg_conceded = models.CharField(max_length=100, blank=True)
    home_clean_sheet = models.CharField(max_length=100, blank=True)
    home_change_created = models.CharField(max_length=100, blank=True)
    # away team name
    away_team_name = models.ForeignKey(TeamName, on_delete=models.CASCADE, null=True, related_name='away_team_name')
    # away team goal
    away_team_goal = models.CharField(max_length=100, blank=True)
    # away team players
    away_team_player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_1')
    away_team_player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_2')
    away_team_player_3 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_3')
    away_team_player_4 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_4')
    away_team_player_5 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_5')
    away_team_player_6 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_6')
    away_team_player_7 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_7')
    away_team_player_8 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_8')
    away_team_player_9 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_9')
    away_team_player_10 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_10')
    away_team_player_11 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_11')
    # away team substitutes
    away_team_player_sub_1 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_1')
    away_team_player_sub_2 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_2')
    away_team_player_sub_3 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_3')
    away_team_player_sub_4 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_4')
    away_team_player_sub_5 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_5')
    away_team_player_sub_6 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_6')
    away_team_player_sub_7 = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_7')
    # goalkeeper, defender, midfielder, forward
    away_team_player_1_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_1_position')
    away_team_player_2_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_2_position')
    away_team_player_3_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_3_position')
    away_team_player_4_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_4_position')
    away_team_player_5_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_5_position')
    away_team_player_6_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_6_position')
    away_team_player_7_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_7_position')
    away_team_player_8_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_8_position')
    away_team_player_9_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_9_position')
    away_team_player_10_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_10_position')
    away_team_player_11_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_11_position')
    # home team substitutes' position
    away_team_player_sub_1_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_1_position')
    away_team_player_sub_2_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_2_position')
    away_team_player_sub_3_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_3_position')
    away_team_player_sub_4_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_4_position')
    away_team_player_sub_5_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_5_position')
    away_team_player_sub_6_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_6_position')
    away_team_player_sub_7_position = models.ForeignKey(PlayerPosition, on_delete=models.CASCADE, null=True, related_name='away_team_player_sub_7_position')
    # team count of position
    away_team_line_1_count = models.CharField(max_length=100, blank=True)
    away_team_line_2_count = models.CharField(max_length=100, blank=True)
    away_team_line_3_count = models.CharField(max_length=100, blank=True)
    away_team_line_4_count = models.CharField(max_length=100, blank=True)
    away_team_line_5_count = models.CharField(max_length=100, blank=True)
    away_team_line_6_count = models.CharField(max_length=100, blank=True)
    # season data
    away_position = models.CharField(max_length=100, blank=True)
    away_won = models.CharField(max_length=100, blank=True)
    away_drawn = models.CharField(max_length=100, blank=True)
    away_lost = models.CharField(max_length=100, blank=True)
    away_avg_goal = models.CharField(max_length=100, blank=True)
    away_avg_conceded = models.CharField(max_length=100, blank=True)
    away_clean_sheet = models.CharField(max_length=100, blank=True)
    away_change_created = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s %s %s %s' % (self.match_date_weekday, self.match_date_day, self.match_date_month, self.match_date_year)

