# write your code here!
import requests
import json

currency = input().strip()
url = f'http://www.floatrates.com/daily/{currency}.json'
r = requests.get(url)
currency_dict = json.loads(r.text)
# print(currency_dict.keys())
print(currency_dict['usd'])
print(currency_dict['eur'])




# print('Meet a conicoin!')
# CONICOIN_TO_DOLLAR = 100

# prompt = 'Please, enter the number of conicoins you have: '
# exchange_rates = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17,
                  #'AUD': 1.9622, 'MAD': 0.208}
# conicoins_amount = float(input())

# for currency in exchange_rates:
#   currency_amount = conicoins_amount * exchange_rates[currency]
#   print(f'I will get {currency_amount} {currency} from the sale of {conicoins_amount} conicoins.')
# exchange_rate = float(input('Please, enter the exchange rate: '))
# dollars_amount = conicoins_amount * exchange_rate #CONICOIN_TO_DOLLAR
# print(f'The total amount of dollars: {dollars_amount}')
