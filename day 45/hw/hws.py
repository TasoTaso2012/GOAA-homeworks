#1
print("Hello world")

#2
a = 5
b = 10
print(f"{a}{b}")

#3
str1 = "Hello"
str2 = "World"
print(f"{str1}{str2}") 

#5
a=5
b=10
print(a == b)


a=5
b=10
print(a != b)


a=5
b=10
print(a > b)


a=5
b=10
print(a < b)


a=5
b=10
print(a >= b)


a=5
b=10
print(a <= b)


#6
10 == 4 +10  
5 + 3 == 8 

20 != 12  
5 + 7 > 10  

#7 

#True and True = True 
#True and False = False
#False and True = False
#False and False = False
#True or True = True
#True or False = True
#False or True = True
#False or False = False

#8 

x = 5
y = 10
z = 5
(x == y) and (y == z)

x = 5
y = 10
z = 5
(x != y) or (y != z)

x = 5
y = 3
(x > y) or (x< y)

#9 
for i in range(1, 11):
    print(i)

#10 
text = "Hello, World!"

for i in range(len(text)):
    print(text[i])


#11
i = 1
while i <= 10:
    print(i)
    i += 1  

#12 
sum = 0  
i = 1 

while sum < 50:
    sum += i  
    i += 1 

print("Final sum:",  sum)
print("Last number added:",i - 1)

#13 
def average(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count


test_list = [1, 3, 4, 5, 2]
print(average(test_list))


#14
def square_numbers(numbers):
    squared_list = [] 
    for number in numbers:
        squared_list.append(number ** 2) 
    return squared_list 


test_list = [3, 12, 5, 2, 6]
print(square_numbers(test_list))

#15 
my_list = [1, 2, 3]
my_list.append(4) 
my_list.insert(2, 10) 
my_list.pop(1)
my_list.index(10) 


my_string = "Hello World"
my_string.upper()
my_string.lower()
my_string.capitalize




