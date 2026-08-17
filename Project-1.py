tasks = []

while True:
	print("\n1. Add task 2. Show existing tasks 3. Delete tasks 4. Exit")
	choice = input("Please select: ")

	if choice == "1":
		task = input("What task do you want to do?")
		tasks.append(task)

	elif choice == "2":
		
		for task in tasks:
			print(task)

	elif choice == "3":
		
		if not tasks:
			print("There is no task.")
			continue

		for i in range(len(tasks)):
			print(str(i + 1) + ": " + tasks[i])
		number = int(input("Which one do you want to delete?"))
		if number < 1 or number > len(tasks):
			continue

		tasks.pop(number - 1)

	elif choice == "4":
		print("Goodbye!")
		break

	else:
		print("Invalid input, please choose again")


