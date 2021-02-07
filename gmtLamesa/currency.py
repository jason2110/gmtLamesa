from forex_python.converter import CurrencyRates 

c = CurrencyRates()
Currency = c.get_rate('USD', 'EUR')  #convert USD to EURO
print(Currency)
