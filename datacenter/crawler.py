import time
import cv2
import numpy
import glob

from selenium import webdriver
from PIL import Image

from datacenter.models import Season, Player, Match


def register_home_team_players(match, html):
    shirt_number_tag = 'Shirt number </span>"'
    goal_keeper_tag = 'Goalkeeper</h3>'
    defenders_tag = 'Defenders</h3>'
    forwards_tag = 'Forwards</h3>'
    substitutes_tag = 'Substitutes</h3>'

    html = html[html.find(goal_keeper_tag) + 15:]
    html_goal_keeper = html[:html.find(defenders_tag)]
    html = html[html.find(defenders_tag):]
    html_goal_keeper = html_goal_keeper[html_goal_keeper.find(shirt_number_tag) + 19:]
    html_goal_keeper = html_goal_keeper[:html_goal_keeper.find('"')]
    

def register_home_team_formation(match, driver):
    formation = driver.find_elements_by_class_name("matchTeamFormation")
    print(formation[0].text)
    print(formation[1].text)
    home_formation = formation[0].text.split('-')
    away_formation = formation[1].text.split('-')
    match.home_team_defender_count = home_formation[0]
    match.home_team_midfielder_count = home_formation[1]
    match.home_team_forward_count = home_formation[2]
    match.away_team_defender_count = away_formation[0]
    match.away_team_midfielder_count = away_formation[1]
    match.away_team_forward_count = away_formation[2]
    match.save()
    return match, driver


def get_line_up_source(driver, link):
    driver.get(link)
    time.sleep(1)
    driver.find_elements_by_class_name("matchCentreSquadLabelContainer")[0].click()
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


def crawling_and_create_match_database(match, link):
    driver = setup_chrome()
    driver = get_line_up_source(driver, link)
#    html = get_line_up_source(driver, link)
    match, driver = register_home_team_formation(match, driver)
#    match, html = register_home_team_formation(match, html)
#    match, html = register_home_team_players(match, html)

def get_latest_match_link(html):
    href_start = 'data-href="//'
    href_end = '"'
    html = html[html.find(href_start) + 13:]
    link = 'https://%s' % html[:html.find(href_end)]
    print(link)
    html = html[html.find(href_end):]
    return html, link

def get_latest_match_date(html):
    tag = 'class="date long"'
    date_start = '<strong>'
    date_end = '</strong>'

    html = html[html.find(tag) + 17:]
    date = html[html.find(date_start) + 8:html.find(date_end)]

    print('match date : "%s"' % date)

    return html, date


def get_season_html(key):
    season = Season.objects.get(season=key)
    print('season %s' % season.season)
    return season.html


def start(key):
    html = get_season_html(key)
    html, match_date = get_latest_match_date(html)

    match = Match.objects.create(match_date=match_date)

    html, link = get_latest_match_link(html)
    crawling_and_create_match_database(match, link)

