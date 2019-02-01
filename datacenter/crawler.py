import time
import cv2
import numpy
import glob

from selenium import webdriver
from PIL import Image

from datacenter.models import Season, Player, Match


def register_substitute(match, player, position):
    if not match.home_team_player_sub_1:
        match.home_team_player_sub_1 = player
        match.home_team_player_sub_1_position = position
    elif not match.home_team_player_sub_2:
        match.home_team_player_sub_2 = player
        match.home_team_player_sub_2_position = position
    elif not match.home_team_player_sub_3:  
        match.home_team_player_sub_3 = player
        match.home_team_player_sub_3_position = position
    elif not match.home_team_player_sub_4:
        match.home_team_player_sub_4 = player
        match.home_team_player_sub_4_position = position
    elif not match.home_team_player_sub_5:
        match.home_team_player_sub_5 = player
        match.home_team_player_sub_5_position = position
    elif not match.home_team_player_sub_6:
        match.home_team_player_sub_6 = player
        match.home_team_player_sub_6_position = position
    elif not match.home_team_player_sub_7:
        match.home_team_player_sub_7 = player
        match.home_team_player_sub_7_position = position
    elif not match.away_team_player_sub_1:
        match.away_team_player_sub_1 = player
        match.away_team_player_sub_1_position = position
    elif not match.away_team_player_sub_2:
        match.away_team_player_sub_2_position = position
        match.away_team_player_sub_2 = player
    elif not match.away_team_player_sub_3:
        match.away_team_player_sub_3 = player
        match.away_team_player_sub_3_position = position
    elif not match.away_team_player_sub_4:
        match.away_team_player_sub_4 = player
        match.away_team_player_sub_4_position = position
    elif not match.away_team_player_sub_5:
        match.away_team_player_sub_5 = player
        match.away_team_player_sub_5_position = position
    elif not match.away_team_player_sub_6:
        match.away_team_player_sub_6 = player
        match.away_team_player_sub_6_position = position
    elif not match.away_team_player_sub_7:
        match.away_team_player_sub_7 = player
        match.away_team_player_sub_7_position = position
    else:
        print('error!! error!! error!! error!! error!!\nerror!! error!! error!! error!! error!!')
    match.save()
    return match


def parse_and_get_or_create_player(player):
    player_data = player.split('\n')
    shirt_number = player_data[0]
    player_name = player_data[1]
    position = None
    if player_data[len(player_data) - 1] == '':
        player_data = player_data[:len(player_data) - 1]
    if player_data[len(player_data) - 1] == 'C':
        player_nation = player_data[len(player_data) - 3]
    else:
        target = player_data[len(player_data) - 1]
        if target == 'Defender' or target == 'Midfielder' or target == 'Goalkeeper' or target == 'Forward':
            position = target
            player_nation = player_data[len(player_data) - 2]
        else:
            player_nation = player_data[len(player_data) - 1]
#    print('%s %s %s' % (shirt_number, player_name, player_nation))
    player, created = Player.objects.get_or_create(player_name=player_name, player_nation=player_nation, player_back_number=shirt_number)
    return player, position


def split_players(players):
    return players.split('Shirt number\n')[1:]


def register_substitutes(match, substitutes):
    substitutes = split_players(substitutes)
    for substitute in substitutes:
        player, position = parse_and_get_or_create_player(substitute)
        match = register_substitute(match, player, position)
    return match


def register_starter(match, player, position):
    if not match.home_team_player_1:
        match.home_team_player_1 = player
        match.home_team_player_1_position = position
    elif not match.home_team_player_2:
        match.home_team_player_2 = player
        match.home_team_player_2_position = position
    elif not match.home_team_player_3:  
        match.home_team_player_3 = player
        match.home_team_player_3_position = position
    elif not match.home_team_player_4:
        match.home_team_player_4 = player
        match.home_team_player_4_position = position
    elif not match.home_team_player_5:
        match.home_team_player_5 = player
        match.home_team_player_5_position = position
    elif not match.home_team_player_6:
        match.home_team_player_6 = player
        match.home_team_player_6_position = position
    elif not match.home_team_player_7:
        match.home_team_player_7 = player
        match.home_team_player_7_position = position
    elif not match.home_team_player_8:
        match.home_team_player_8 = player
        match.home_team_player_8_position = position
    elif not match.home_team_player_9:
        match.home_team_player_9 = player
        match.home_team_player_9_position = position
    elif not match.home_team_player_10:
        match.home_team_player_10 = player
        match.home_team_player_10_position = position
    elif not match.home_team_player_11:
        match.home_team_player_11 = player
        match.home_team_player_11_position = position
    elif not match.away_team_player_1:
        match.away_team_player_1 = player
        match.away_team_player_1_position = position
    elif not match.away_team_player_2:
        match.away_team_player_2 = player
        match.away_team_player_2_position = position
    elif not match.away_team_player_3:
        match.away_team_player_3 = player
        match.away_team_player_3_position = position
    elif not match.away_team_player_4:
        match.away_team_player_4 = player
        match.away_team_player_4_position = position
    elif not match.away_team_player_5:
        match.away_team_player_5 = player
        match.away_team_player_5_position = position
    elif not match.away_team_player_6:
        match.away_team_player_6 = player
        match.away_team_player_6_position = position
    elif not match.away_team_player_7:
        match.away_team_player_7 = player
        match.away_team_player_7_position = position
    elif not match.away_team_player_8:
        match.away_team_player_8 = player
        match.away_team_player_8_position = position
    elif not match.away_team_player_9:
        match.away_team_player_9 = player
        match.away_team_player_9_position = position
    elif not match.away_team_player_10:
        match.away_team_player_10 = player
        match.away_team_player_10_position = position
    elif not match.away_team_player_11:
        match.away_team_player_11 = player
        match.away_team_player_11_position = position
    else:
       print('error!! error!! error!! error!! error!!\nerror!! error!! error!! error!! error!!')
    match.save()
    return match


def register_starters(match, players):
    for player in players:
        match = register_starter(match, player)
    return match


def split_starters_by_positions(match, players):
    goal_keeper = players.split('Goalkeeper\n')[1].split('Defender')[0]
    defenders = players.split('Goalkeeper\n')[1].split('Defender')[1].split('Midfielder')[0]
    midfielders = players.split('Goalkeeper\n')[1].split('Defender')[1].split('Midfielder')[1].split('Forward')[0]
    forwards = players.split('Goalkeeper\n')[1].split('Defender')[1].split('Midfielder')[1].split('Forward')[1]
    goal_keeper_data = split_players(goal_keeper)[0]
    defenders_data = split_players(defenders)
    midfielders_data = split_players(midfielders)
    forwards_data = split_players(forwards)

    player, position = parse_and_get_or_create_player(goal_keeper_data)
    match = register_starter(match, player, 'Goalkeeper')

    for defender_data in defenders_data:
        player, position = parse_and_get_or_create_player(defender_data)
        match = register_starter(match, player, 'Defender')
    for midfielder_data in midfielders_data:
        player, position = parse_and_get_or_create_player(midfielder_data)
        match = register_starter(match, player, 'Midfielder')
    for forward_data in forwards_data:
        player, position = parse_and_get_or_create_player(forward_data)
        match = register_starter(match, player, 'Forward')
    match.save()
    return match


def register_team_players(match, team):
    starters = team.text.split('Substitutes\n')[0]
    substitutes = team.text.split('Substitutes\n')[1]
    match = split_starters_by_positions(match, starters)
    match = register_substitutes(match, substitutes)
    return match


def register_all_players(match, driver):
    teams = driver.find_elements_by_class_name("matchLineupTeamContainer")
    match = register_team_players(match, teams[0])
    match = register_team_players(match, teams[1])
    return match, driver


def register_formations(match, driver):
    formations = driver.find_elements_by_class_name("matchTeamFormation")
    print('%s vs %s' % (formations[0].text, formations[1].text))
    home_formation = formations[0].text.split('-')
    away_formation = formations[1].text.split('-')
    match.home_team_line_1_count = home_formation[0]
    match.home_team_line_2_count = home_formation[1]
    match.home_team_line_3_count = home_formation[2]
    try: 
        match.home_team_line_4_count = home_formation[3]
    except:
        match.home_team_line_4_count = 0
    try:
        match.home_team_line_5_count = home_formation[4]
    except:
        match.home_team_line_5_count = 0
    try:
        match.home_team_line_6_count = home_formation[5]
    except:
        match.home_team_line_6_count = 0

    match.away_team_line_1_count = away_formation[0]
    match.away_team_line_2_count = away_formation[1]
    match.away_team_line_3_count = away_formation[2]
    try:
        match.away_team_line_4_count = away_formation[3]
    except:
        match.away_team_line_4_count = 0
    try:
        match.away_team_line_5_count = away_formation[4]
    except:
        match.away_team_line_5_count = 0
    try:
        match.away_team_line_6_count = away_formation[5]
    except:
        match.away_team_line_6_count = 0
    match.save()
    return match, driver


def click_line_up_button(driver, link):
    driver.get(link)
    time.sleep(2)
    driver.find_elements_by_class_name("matchCentreSquadLabelContainer")[0].click()
    time.sleep(2)
    return driver


def setup_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("window-size=1280x900")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
    return driver


def register_score(match, driver):
    scorebox_container = driver.find_elements_by_class_name("scoreboxContainer")[0]
    score = scorebox_container.find_elements_by_class_name("matchScoreContainer")[0]
    score = score.text.split('-')
    match.home_team_goal = score[0]
    match.away_team_goal = score[1]
    print("%s : %s" % (score[0], score[1]))
    match.save()
    return match, driver


def register_team_name(match, driver):
    teams_container = driver.find_elements_by_class_name("teamsContainer")[0]
    home_team = teams_container.find_elements_by_class_name("home")[0]
    home_team_name = home_team.find_elements_by_class_name("long")[0].text
    away_team = teams_container.find_elements_by_class_name("away")[0]
    away_team_name = away_team.find_elements_by_class_name("long")[0].text
    match.home_team_name = home_team_name
    match.away_team_name = away_team_name
    print("%s vs %s" % (home_team_name, away_team_name))
    match.save()
    return match, driver


def crawling_and_create_match_database(match, link):
    driver = setup_chrome()
    driver = click_line_up_button(driver, link)
    match, driver = register_team_name(match, driver)
    match, driver = register_score(match, driver)
    match, driver = register_formations(match, driver)
    match, driver = register_all_players(match, driver)
    return 'done'

def get_latest_match_link(html):
    href_start = 'data-href="//'
    href_end = '"'
    target = html.find(href_start)
    if target == -1:
        return html, None
    html = html[target + 13:]
    link = 'https://%s' % html[:html.find(href_end)]
    html = html[html.find(href_end):]
    return html, link

def get_latest_match_date(html):
    tag = 'class="date long"'
    date_start = '<strong>'
    date_end = '</strong>'
    target = html.find(tag)
    if target == -1:
        return html, None
    html = html[target + 17:]
    date = html[html.find(date_start) + 8:html.find(date_end)]
    next_date = html.find(tag)
    parsed_html = html[:next_date]
    html = html[next_date:]
    print('match date : "%s"' % date)

    return html, parsed_html, date


def get_season_html(key):
    season = Season.objects.get(season=key)
    print('season %s' % season.season)
    return season.html


def start(key):
    html = get_season_html(key)

    while True:
        html, parsed_html, match_date = get_latest_match_date(html)
        if not match_date:
            break
        match_date = match_date.split(' ')
        while True:
            link = None
            parsed_html, link = get_latest_match_link(parsed_html)
            if not link:
                break
            match = None
            match = Match.objects.create(match_date_weekday=match_date[0], match_date_day=match_date[1], match_date_month=match_date[2], match_date_year=match_date[3])
            result = crawling_and_create_match_database(match, link)

