
price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Taxe rate is: ', tax)

