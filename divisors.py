
print("")
print("This prints out a list of all the divisors of the number you input.")
print("")
print("Enter a number:")
num = int(input("--> "))
list_of_num = []

list_range = list(range(1,num+1))

for elem in list_range:

	if num % elem == 0:
		list_of_num.append(elem)
print(list_of_num)













