person_first = "Tony"
person_last = "Stark"
age = 51
print(person_first + " is a genious")
#name = input("Enter your name")
#print(name)
#superhero_name = input("tejas enter your superhero name")
#print(superhero_name + "is tejas's superhero")

first = input("Your first number:")
second = input("Your secoond number:")
sum = int(first) + int(second)
print(sum)
name = "Tony Stark"
print(name.replace("T", "M"))
print(name.find("S"))

print(name.upper)
print(name.lower)

print("S" in name)

print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)  #to print the value with decimal we use the / operator
print(5 // 2) #to remove value after the decimal we use the // operator
print(5 % 2)  #it prints the remainder in the operation when we divide 5 / 2 the remainder we get is 1
print(5 ** 2) #to get the product in the power method eg. sqaure, cube, etc


i = 5
i = i + 2
i += 2
i -= 2
i *= 2


result = 2 + 3 * 5
print(result) # * > +


print(3>2)
print(3<2)
print(3<=2)
print(3>=2)
print(3 == 2)


print(3 != 2)
print(3 != 3)


#or
print(2 > 1 or 2 > 3)
print (2 > 1 and 2 > 3)
print(not 3 > 2 )


#if else statements
age = 19
if age >= 18:
    print("you are an adult you can vote")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("You are a child")

#calculator task
#in calculator.py file

#while loop
i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 1
while i <= 5:
    print( i * " * ")
    i = i + 1

#range
for i in range(10):
    print(i)

#list


# break and continue

#students = ["ram", "radhika", "shyam", "kishan", "radha"]

#for student in students:
#    if student == "kishan":
 #       break;
 #   print(student)

students = ["ram", "radhika", "shyam", "kishan", "radha"]
for student in students:
    if student == "shyam":
        continue;
    print(student)

#tuple are immutable
marks = (67, 76, 56, 56, 56, 56, 56, 56,)

print(marks.count(56))

print(marks.index(56))


#sets is a collection of unique collection of data which means theres no chance of duplicating of the data nnd it does not contain any index value of the data
score = {56, 56, 34, 35, 65, 65}
print(score)


#dictionaries are the key value pair type of data
marks = {"eng" : 78, "maths" : 23, "sci" : 23}
print(marks["sci"])


from math import sqrt
print(sqrt(4))

#user defined functions
def sum_num(first, second):
    print(first + second)

sum_num(1,2)