#Topping kinds
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#Price list
prices = [2, 6, 1, 3, 2, 7, 2]

#Topping length
num_pizzas = len(toppings)

#Print out num_pizzas
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Combine two list
pizzas = list(zip(prices, toppings))

#Print out pizzas
print(pizzas)

#Sort the pizzas by prices
pizzas.sort()

#Cheapest pizza
cheapest_pizza = pizzas[0]

#Most expensive pizza
priciest_pizza = pizzas[-1]

#Three cheapest ones
three_cheapest = pizzas[:3]

#Print out three cheapest pizzas
print(three_cheapest)

#Count the numbers of 2 slices on the list
num_two_dollar_slice = prices.count(2)
print(num_two_dollar_slice)
