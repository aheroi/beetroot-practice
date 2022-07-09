country = input('What county do you live in?  ')
  
if country.lower() == 'canada':
    province = input('what province do you live in? ')
    if province.lower() in ('alberta', \
            'nunavut', 'yukon'):
        tax = 0.05
    elif province.lower() == 'ontario':
        tax = 0.13
    else:
        tax = 0.15

    print(f'for {province.capitalize()} province tax rate is: ', tax)
else:
    print('Non Canadian residents do not pay sales tax.')
