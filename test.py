from time import sleep
from selenium import webdriver


def run(url):
    url = "https://premierleague.com/match/38567"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("window-size=1280x900")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)

    driver.get(url)

    sleep(5)
    stats = driver.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[1]/div/div/ul/li[3]')[0]

    print(stats.get_attribute('outerHTML'))
    stats.click()
    sleep(1)
    print('click stats')
#    driver.find_elements_by_class_name("matchNav")[0]
#    print('tablinks')
#    driver.find_elements_by_xpath('//li[@data-tab-index="2"]')[0].click()
#    print('data-tab-index=2')
    head_to_head = stats.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[3]/div[1]/ul/ul/li[1]')[0]
    print(head_to_head.get_attribute('outerHTML'))
    print(head_to_head.text)
    head_to_head.click()
    sleep(1)
    print('click head-to-head')
#    driver.find_elements_by_class_name("matchCentreStatsTabToggles")
#    print('matchcentrestatstabtoggles')
    container = head_to_head.find_elements_by_xpath('//*[@id="mainContent"]/div/section/div[2]/div[2]/div[2]/section[3]/div[2]/div[1]/div[2]/section/table/tbody')[0]
    rows = container.text.split('\n')

    i = 0
    for row in rows:
        print('new row')
        fields = row.split(' ')

        home_value = fields[0]
        away_value = fields[len(fields) - 1]

        print('%s vs %s' % (home_value, away_value))

        i = i + 1
        if i == len(rows) - 2:
            break
