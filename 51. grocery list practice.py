import datetime

print('Welcome to Grocery List App.')

now=datetime.datetime.now()

food=['Meat', 'Cheese']

print('Current date and time:',str(now))
print('You currently have', food[0],' and', [1], ' in your list:')



food_add1=input('Type of food to add to the grocery list:')
food_add2=input('Type of food to add to the grocery list:')
food_add3=input('Type of food to add to the grocery list:')

if food_add1 not in food:
    food.append(food_add1.title())
if food_add2 not in food:
    food.append(food_add2.title())
if food_add3 not in food:
    food.append(food_add3.title())
    

print('Here is your grocery list:',food)
print('Here is your grocery list sorted:',sorted(food))

print('Simulating grocery shopping...')


print('Current grocery list:',len(food),'items')
just_buy=input('What food did you just buy:')

for just_buy in food:
    food.remove(just_buy)
    print('Remove',just_buy,' from from list...')
    print('Current grocery list:',len(food),'items')

