########## product and price for my items

product1_name, product1_price = 'Smartphone', 100

product2_name, product2_price = 'Computer', 200

product3_name, product3_price = 'Accommodation', 300

########## company name and information 

company_name = 'Alkebulan Enterprises'

company_address = '00100 & 30208'

company_city = 'Nairobi $ Kapsara'

########## ending message

message = 'Thanks for shopping with us today!'

########## a top border 

print('*' * 50)

########## company information first 

print('\t\t{}'.format(company_name.title()))

print('\t\t{}'.format(company_address.title()))

print('\t\t{}'.format(company_city.title()))

########## line between sections

print('=' * 50)

########## header for section of items

print('\tProduct Name\tProduct Price')

########## a statement for each item 

print('\t{}\t\t${}'.format(product1_name.title(), product1_price))

print('\t{}\t\t${}'.format(product2_name.title(), product2_price))

print('\t{}\t\t${}'.format(product3_name.title(), product3_price))

########## a line between sections 

print('=' * 50 )

########## header for section of total

print('\t\t\tTotal')

########## calculate total price and print out 

total = product1_price + product2_price + product3_price 

print('\t\t\t${}'.format(total))

########## a line between sections

print('=' * 50)

########## thank you message

print('\n\t{}\n'.format(message))

########## bottom order

print('*' * 50)

