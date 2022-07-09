# # ver_1
# print("# ver_1")
# sum = 0.0

# print ("This program will take several numbers, then average them.")
# count = int(input("How many numbers would you like to sum:  "))
# current_count = 1
 
# while current_count < count+1:
# 	print ("Number",current_count)
# 	number = float(input("Enter a number:  "))
# 	sum = sum + number
# 	current_count += 1
 
# print("The average was:",sum/count)

# ver_2
print("# ver_2")

#Continuously updates the average as new numbers are entered.

print ("Welcome to the Average Calculator, please insert a number")
current_average = 0
num_of_nums = 0
while True:
    new_number = int(input("New number "))
    num_of_nums = num_of_nums + 1
    current_average = (round((((current_average * (num_of_nums - 1)) + new_number) / num_of_nums), 3))
    print ("The current average is " + str((round(current_average, 3))))
