from django.db import models

# Create your models here.


class Season(models.Model):
    season = models.CharField(max_length=100, blank=True)
    html = models.TextField(blank=True)
    description = models.TextField(blank=True)


class Player(models.Model):
    player_name = models.CharField(max_length=100, blank=True)
    player_nation = models.CharField(max_length=100, blank=True)
    player_back_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.player_name, self.player_nation)


class Match(models.Model):
    # match date
    match_date_day = models.CharField(max_length=100, blank=True)
    match_date_month = models.CharField(max_length=100, blank=True)
    match_date_weekday = models.CharField(max_length=100, blank=True)
    match_date_year = models.CharField(max_length=100, blank=True)
    # home team name
    home_team_name = models.CharField(max_length=100, blank=True)
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
    # location of player's position 1st, 2nd, 3rd, 4th, 5th
    home_team_player_1_location = models.CharField(max_length=100, blank=True)
    home_team_player_2_location = models.CharField(max_length=100, blank=True)
    home_team_player_3_location = models.CharField(max_length=100, blank=True)
    home_team_player_4_location = models.CharField(max_length=100, blank=True)
    home_team_player_5_location = models.CharField(max_length=100, blank=True)
    home_team_player_6_location = models.CharField(max_length=100, blank=True)
    home_team_player_7_location = models.CharField(max_length=100, blank=True)
    home_team_player_8_location = models.CharField(max_length=100, blank=True)
    home_team_player_9_location = models.CharField(max_length=100, blank=True)
    home_team_player_10_location = models.CharField(max_length=100, blank=True)
    home_team_player_11_location = models.CharField(max_length=100, blank=True)
    # goalkeeper, defender, midfielder, forward
    home_team_player_1_position = models.CharField(max_length=100, blank=True)
    home_team_player_2_position = models.CharField(max_length=100, blank=True)
    home_team_player_3_position = models.CharField(max_length=100, blank=True)
    home_team_player_4_position = models.CharField(max_length=100, blank=True)
    home_team_player_5_position = models.CharField(max_length=100, blank=True)
    home_team_player_6_position = models.CharField(max_length=100, blank=True)
    home_team_player_7_position = models.CharField(max_length=100, blank=True)
    home_team_player_8_position = models.CharField(max_length=100, blank=True)
    home_team_player_9_position = models.CharField(max_length=100, blank=True)
    home_team_player_10_position = models.CharField(max_length=100, blank=True)
    home_team_player_11_position = models.CharField(max_length=100, blank=True)
    # home team substitutes' position
    home_team_player_sub_1_position = models.CharField(max_length=100, blank=True)
    home_team_player_sub_2_position = models.CharField(max_length=100, blank=True)
    home_team_player_sub_3_position = models.CharField(max_length=100, blank=True)
    home_team_player_sub_4_position = models.CharField(max_length=100, blank=True)
    home_team_player_sub_5_position = models.CharField(max_length=100, blank=True)
    home_team_player_sub_6_position = models.CharField(max_length=100, blank=True)
    home_team_player_sub_7_position = models.CharField(max_length=100, blank=True)
    # count of position
    home_team_line_1_count = models.CharField(max_length=100, blank=True)
    home_team_line_2_count = models.CharField(max_length=100, blank=True)
    home_team_line_3_count = models.CharField(max_length=100, blank=True)
    home_team_line_4_count = models.CharField(max_length=100, blank=True)
#    home_team_line_5_count = models.CharField(max_length=100, blank=True)
#    home_team_line_6_count = models.CharField(max_length=100, blank=True)
    # away team name
    away_team_name = models.CharField(max_length=100, blank=True)
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
    # location of player's position 1st, 2nd, 3rd, 4th, 5th
    away_team_player_1_location = models.CharField(max_length=100, blank=True)
    away_team_player_2_location = models.CharField(max_length=100, blank=True)
    away_team_player_3_location = models.CharField(max_length=100, blank=True)
    away_team_player_4_location = models.CharField(max_length=100, blank=True)
    away_team_player_5_location = models.CharField(max_length=100, blank=True)
    away_team_player_6_location = models.CharField(max_length=100, blank=True)
    away_team_player_7_location = models.CharField(max_length=100, blank=True)
    away_team_player_8_location = models.CharField(max_length=100, blank=True)
    away_team_player_9_location = models.CharField(max_length=100, blank=True)
    away_team_player_10_location = models.CharField(max_length=100, blank=True)
    away_team_player_11_location = models.CharField(max_length=100, blank=True)
    # goalkeeper, defender, midfielder, forward
    away_team_player_1_position = models.CharField(max_length=100, blank=True)
    away_team_player_2_position = models.CharField(max_length=100, blank=True)
    away_team_player_3_position = models.CharField(max_length=100, blank=True)
    away_team_player_4_position = models.CharField(max_length=100, blank=True)
    away_team_player_5_position = models.CharField(max_length=100, blank=True)
    away_team_player_6_position = models.CharField(max_length=100, blank=True)
    away_team_player_7_position = models.CharField(max_length=100, blank=True)
    away_team_player_8_position = models.CharField(max_length=100, blank=True)
    away_team_player_9_position = models.CharField(max_length=100, blank=True)
    away_team_player_10_position = models.CharField(max_length=100, blank=True)
    away_team_player_10_position = models.CharField(max_length=100, blank=True)
   # team count of position
    away_team_line_1_count = models.CharField(max_length=100, blank=True)
    away_team_line_2_count = models.CharField(max_length=100, blank=True)
    away_team_line_3_count = models.CharField(max_length=100, blank=True)
    away_team_line_4_count = models.CharField(max_length=100, blank=True)
#    away_team_line_5_count = models.CharField(max_length=100, blank=True)
#    away_team_line_6_count = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.match_date                                                                  
