number = int(input("Enter the number whose tables are to be generated:\n"))
limit =int(input("Enter the limit:\n"))
#Multiplication
print("****Multiplication table****")
for i in range(1, limit + 1):
	result = number * i
	print(f"{number} x {i} = {result}")
	
print("--------------------------")

#Division,
print("****Division table****")
for i in range(1, limit + 1):
	result = number/i
	print(f"{number} / {i} = {result:.2f} ")