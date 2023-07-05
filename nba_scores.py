from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"  #Endpoint i.e.The specific data that we want

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']
    
    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("----------------------------------------------")
        print(f"{home_team} vs {away_team}, {clock}, {period}")


get_scoreboard()