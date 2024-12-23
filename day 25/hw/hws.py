#1
name="anastasia"
print(name[1])
#2
num1=12
num2=48
print(num1+num2)
#3
str1="goa"     
str2="best"
print(str1+str2)

#concatenation means combining multiple strings into a single string.

#4
int1=32
int2=75
print(int2/int1)


#IMPLICIT CONVERSION:
#when you divide integers in python,the answer in terminal would be
#a float,even if the answer could be an integer.pyhton does this because 
#to make sure the division is accurate.
#thats called implicit conversion


#EXPLICIT CONVERSION:
#when you want to change one type into another using functions
#for example when you want to change float into intenger
#you have to use int() function.
#that is called explicit conversion.

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
print(5 + 2 == 1 -1)
print(4 - 1 == 3 + 2)
print(9 + 2 - 2 != 1)

#7
#true and false = false
#true and true = true
#false and false = false
#false and true = true


#true or false = true
#true or true = true
#false or false = false
#false or true = true

#8
a=5
b=10
print(a == b)  #false


a=5
b=10
print(a != b)  #true


a=5
b=10
print(a > b)  #false


a=5
b=10
print(a < b)  #true


a=5
b=10
print(a >= b)  #false
#9
for i in range(1,10):
    print(i)
#11
string="hello world!"
for i in string:
    print(i)

#12

i=1
while i <=10:
    print(i)
    i=i+1

#13
i=1
while i <= 100:
    print(i)
    i=i+1
    if i == 50:
        i =61

#14
i=1
total=0
while total <50:
    total=total+1
    print(total)
    i=i+1


