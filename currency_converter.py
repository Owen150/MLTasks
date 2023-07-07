from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    
    #Converting the data from a dictionary to a list by getting all the items so that we can sort the data by the different currency names
    #The items will give tuples that contain the key-the currencyName, value-associated with each currency
    data = list(data.items())
    #Will be sorted by the first item in the set/list i.e. currencyName
    data.sort()
    
    return data

def print_currencies(currencies):    
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")
        
def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()
    printer.pprint(data)
        

#data = get_currencies()
#print_currencies(data)
exchange_rate("USD", "CAD")