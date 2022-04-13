# write your code here!
# print('Meet a conicoin!')
# CONICOIN_TO_DOLLAR = 100


# prompt = 'Please, enter the number of conicoins you have: '
exchange_rates = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17,
                  'AUD': 1.9622, 'MAD': 0.208}
conicoins_amount = float(input())

for currency in exchange_rates:
    currency_amount = conicoins_amount * exchange_rates[currency]
    print(f'I will get {currency_amount} {currency} from the sale of {conicoins_amount} conicoins.')
# exchange_rate = float(input('Please, enter the exchange rate: '))
# dollars_amount = conicoins_amount * exchange_rate #CONICOIN_TO_DOLLAR
# print(f'The total amount of dollars: {dollars_amount}')
