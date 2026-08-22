with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)

with open('file1.txt','w') as file:
	file.write("I love programming.\n")
	file.write("I love creating new games.\n")