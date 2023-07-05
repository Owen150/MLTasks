from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"  #Endpoint i.e.The specific data that we want

printer = PrettyPrinter()

data = get(BASE_URL + ALL_JSON).json()
printer.pprint(data)