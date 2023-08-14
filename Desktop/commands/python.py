#Basic Programs To Crack The Interview #

# Write a program Positive or Negative Number#
n = int(input())
if n > 0 :
	print("POsitive")
else:
	print("Negative")


# Write A program To Find Even Or odd Number#

n = int(input())
if n % 2 == 0:
	print("Even Number")
else:
	print("Odd Number")

# To Find the sum of First N Natural Numbers#


n = int(input())
sum = 0 
for i in range(n+1):
	sum += i 
print(sum)

# To find the sum of number in a given range#

n = int(input())
m = int(input())
sum = 0 
for i in range(n,m+1):
	sum += 1 
print(sum)

#to find the greatest of 2 numbers #

number1 = int(input())
number2 = int(input())
if number1 > number2:
	print(number1)
else:
	print(number2)


#find the Greatest Number of 3 numbers#

number1 = int(input())
number2 = int(input())
number3 = int(input())
if number1 > number2 and number1 > number3 :
	print(number1)
elif number2 > number1 and number2 > number3:
	print(number2)
else:
	print(number3)

# Write a Program To Find Leap Year or not #

year = 2004
if (year % 400 ==0) and (year %100 == 0):
	print("Leap Year")
elif (year % 4 == 0):
	print("Leap Year")
else:
	print("Not a Leap Year")
	
# write a Program To Check Prime Or Not #
n = int(input())