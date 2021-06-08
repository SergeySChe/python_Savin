print('Hello World')
import requests
from decimal import *

getcontext().prec = 4


def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if val not in response:
        return None
    money = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value', response.find(val))]

    return f"{Decimal(money.replace(',', '.'))}"


#print(currency_rates('USD'))
