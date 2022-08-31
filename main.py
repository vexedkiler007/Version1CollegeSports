import undetected_chromedriver as uc
from save import save_html
import os
import codecs
from bs4 import BeautifulSoup
from deffinistion_football_ import average_dif_oppenents
import time

def cleanstring(team_string: str):
    """ Removes All Characters except for Alpha Numeric and Periods"""
    b = []
    for char in team_string:
        if char.isalpha():
            b.append(char)
        if char == '.':
            b.append(char)
    return ''.join(b)


def scrapescore(html: str):
    gamesplayed = []
    soup = BeautifulSoup(html, 'html.parser')
    scorecards = soup.find_all(class_="single-score-card")
    for scorecard in scorecards:
        tables = scorecard.find_all('table')
        try:
            for table in tables:
                teams = table.find_all('tr')
                uncleaned_home = teams[1].find(class_='team').text
                cleaned_home = cleanstring(uncleaned_home)
                uncleaned_home_score = teams[1].find(class_='total-score')
                if uncleaned_home_score:
                    uncleaned_home_score = uncleaned_home_score.text
                uncleaned_away_score = teams[2].find(class_='total-score')
                if uncleaned_away_score:
                    uncleaned_away_score = uncleaned_away_score.text
                uncleaned_away = teams[2].find(class_='team').text
                cleaned_away = cleanstring(uncleaned_away)
                gamesplayed.append((cleaned_away, uncleaned_away_score, cleaned_home, uncleaned_home_score))
        except IndexError or AttributeError:
            pass
    return gamesplayed

def scrapeweb(url,index):
    driver = uc.Chrome()
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    save_html(html,index)
    driver.quit()

def getgames(url,index):
    if not (f'{index}.html' in os.listdir(os.getcwd())):
        scrapeweb(url,index)
    else:
        codecs.open(f'{index}.html', 'r', 'utf-8')




def main():
    sum1 = 0
    sum2 = 0
    for _ in range(1,19):

        games = f'https://www.cbssports.com/college-football/scoreboard/FBS/2021/regular/{_}/'
        list_games = getgames(games,_)
    listofgames = []

    for file_ in os.listdir(os.getcwd()):

        if len(file_) >= 5:
            if file_[-5::] == '.html':
                html = codecs.open(file_,'r', 'utf-8')
                listofgames += scrapescore(html)
    listofgames_mod = []


    for games in listofgames:
        stripedtouple = []
        for strings in games:
            if strings:
                stripedstring = strings.replace(".",'')
                stripedtouple.append(stripedstring)
        listofgames_mod.append(stripedtouple)
    print(average_dif_oppenents(listofgames_mod,'LSU','KansasState'))





if __name__ == '__main__':
    main()





























def cleanstring(team_string):
    b = []
    for char in team_string:
        if char.isalpha():
            b.append(char)
    return ''.join(b)













#
#
# for scorecard in scorecards:
#     team = scorecard.find_all(class_="team")
#
#     try:
#         away = team[2].text.strip(' ')
#         team2_score = team
#         home = team[1].text.strip(' ')
#         cleanedstring_home = cleanstring(home)
#         cleanedstring_away = cleanstring(away)
#         print(cleanedstring_away,cleanedstring_home)
#         prin
