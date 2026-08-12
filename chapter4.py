squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

my_foods = ['hamburger','french fries','ice cream']
friend_foods=my_foods[:]
friend_foods.append('cake')

print(my_foods)
print(friend_foods)