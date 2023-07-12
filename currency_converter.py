from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "d80eb222102aad1189ad"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    
    #Converting the data from a dictionary to a list by getting all the items so that we can sort the data by the different currency names
    #The items will give tuples that contain the key-the currencyName, value-associated with each currency
    data = list(data.items())
    #Will be sorted by the first item in the tuple i.e. currencyName
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
    data = get(url).json()
    
    if len(data) == 0:
        print("Invalid Currencies.")
        return
    
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid Amount.")
        return
    
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()
    
    print("Welcome to the currency converter")
    print("List - lists the different currencies")
    print("Convert - converts from one currency to another")
    print("Rate - gets the exchange rate of two currencies")
    print()
    
    while True:
        command = input("Enter a command to proceed (q to quit): ").lower()
        
        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized Command!")
            

main()                      