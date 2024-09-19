#WHILE LOOP PRACTICE
#Question no 1
count:int=1
while count<=5:
    print("malaika ",end="")
    i=1
    while i<2:
        print("naz ",end="")
        i=i+1

    count=count+1
    print()

#Question no 2
#print numbers from 1 to 100
i:int=1
while i<=100:
    print(i)
    i=i+1

#Question no 3
#print numbers from 100 to 1
i:int=100
while i>=1:
    print(i)
    i=i-1

#Question no 4
#print multiplication table of a number n
n:int=int(input("enter a number= "))
i:int=1
while i<=10:
    print(f"{n}*{i}=",n*i)
    i=i+1

#Question no 5
#print the elements of the following using a while loop
#[1,4,9,16,25,36,48,81,100]
nums:list=[1,4,9,16,25,36,48,81,100]
i=0
while i<len(nums):
    print(nums[i])
    i=i+1

#Question no 6
#search for a number in this tuple using while loop
#(1,2,3,4,5,6,7,8,9,10,4)
num:int=(1,2,3,4,5,6,7,8,9,10,4)
x:int=int(input("enter a number between 1 and 10= "))
i=0
while i<len(num):
    if (num[i]==x):
        print("found x at",i)
    else:
        print("finding....")
    i=i+1
   
#FOR LOOP PRACTICE
#Question no 1
#print the elements of the following using a for loop
#[1,4,9,16,25,36,48,81,100]
nums:list=[1,4,9,16,25,36,48,81,100]
for elements in nums:
    print(elements)

#Question no 2
#search for a number in this tuple using for loop
#(1,2,3,4,5,6,7,8,9,10,4)
num:int=(1,2,3,4,5,6,7,8,9,10,5,4)
x:int=int(input("enter a number between 1 and 10= "))
i=0
for number in num:
    if(number==x):
        print("found x at",i)
    i=i+1

#RANGE FUNCTION range(start,stop,step size)
#Question no 1
count=(range(7)) #range(stop)
for i in count:
    print(i)

#Question no 2
count=(range(2,7)) #range(start,stop)
for i in count:
    print(i)

#Question no 3
count=(range(2,7,2)) #range(start,stop,step)step size 2 means that it will add 2 in starting value until it stops
for i in count:
    print(i)


#PRACTICE OF ASSIGNMENT QUESTIONS
#Question no 1
#  a program* that uses a while loop to print the first 25 integers.
count:int=1
while count<=25:
    print(count)
    count=count+1

# Question no 2
#  a program* that uses a while loop to print the first 10 even numbers
count:int=1
num:int=2
while count<=10:
    print(num)
    num=num+2
    count=count+1

# Question no 3
#  *Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.
nums:list = [1, -2, -3, 4, 5, -6, -7, 8]
positive_nums = []
for num in nums:
    if num >= 0:
        positive_nums.append(num)
nums = positive_nums
print(nums)

# Question no 4
# a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number
n:int=int(input("enter a number to find the factorial of that num= "))
def factorial(n):
    result = 1  
    while n > 0:
        result *= n  
        n -= 1  
    return result 
print(factorial(n))  

# Question no 5
#  a program* to remove all the odd numbers from an array
nums:list=[1,2,3,4,5,6,7,8,]
for num in nums:
    if num % 2!= 0:
        nums.remove(num)
print(nums)

# Question no 6 
# a function* that takes an array, an index, and a value as parameters. Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array
def insert_value(array,index,value):
    array.insert(index,value)
    return array
print(insert_value([1,2,3,4,5,6,7,8,9,10],2, 5))

# Question no 7
#a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array
def sum_of_num(array):
    total=0
    i=0
    while i<len(array):
        total+=array[i]
        i+=1
    return total
print(sum_of_num([1,2,3,4,5,6,7,8]))

# Question no 8
#Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.
def celsius_to_farenheit(celsius_temp):
    i=0
    while i<len(celsius_temp):
        celsius_temp[i]=(celsius_temp[i]* 9/5) + 32 
        i+=1
        return celsius_temp
celsius_input = input("Celsius temperatures= ")
celsius_list = [float(temp) for temp in celsius_input.split(',')] 
print("Fahrenheit temperatures:", celsius_to_farenheit(celsius_list))

# Question no 9
# Implement a simple shopping cart program using an array. Create functions to add items, remove items, and update quantities using array methods. Print the cart's contents after each operation
cart = []
def add_item(item):
  cart.append(item)
  print(cart)
def remove_item(item):
  cart.remove(item)
  print(cart)
def update_quantity(item, quantity):
  cart[cart.index(item)] = (item, quantity)
  print(cart)
add_item('chocolate')
add_item('mango')
remove_item('mango')
update_quantity('chocolate', 2)
