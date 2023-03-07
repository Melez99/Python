# types of data
age = 20 # int
first_name = "John" # string
last_name = "Smith"
is_new = True # bool
print(first_name, last_name, age, is_new)

# string concatenation
name = input("What is your name? ")
print("Hello " + name)

# string concatenation + data type conversion
birth_year = input("what is your year of birth? ")
age = 2023 - int(birth_year)
print("You are " + str(age) +" years old")

# calculator exercise
first_number = input("First: ")
second_number = input("Second: ")
Sum = float(first_number) + float(second_number)
print("Sum: " + str(Sum))

# methods
course = "Python"
print(course)
print(course.upper())
print(course.lower())
print(course.find("y"))   # find the index of first occurrence of the character in the string
print(course.replace("Python", "Snake"))
print("Python" in course)

# arithmetic operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(round(10 / 3, 2)) # result is float and rounded at 2 d.p.
print(10 // 3) # result is an integer
print(10 % 3) # remainder of the division
print(10 ** 3) # 10 to the power of 3

# augmented assignment operator
x = 10
x = x + 3  # the result will be 13
x += 3  # the equation above has been rearranged and the results is 13
print(x)

# comparison operators
x = 3 > 2
print(x)
x = 3 >= 2
x = 3 < 2
x = 3 <= 2
x = 3 == 2
x = 3 != 2

# logical operators
price = 33
print(price > 13 and price <= 33) # both are operators are considered
print(price > 13 and price <= 33) # one expression is considered
print(not price < 30) # inverses true to false

# if statements --- indentation
temperature = 33
if temperature > 30:
    print("Hot day")
    print("Drink plenty of water")

temperature = 3
if temperature > 30:
    print("Hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30)
    print("Nice day")
elif temperature > 10: # (10, 20)
    print("Slightly cold day")
else:
    print("Cold day")

# Kg -> Lbs weight converter
Weight_o = float(input("Weight: "))
Weight_c = input("(K)g or (L)bs: ")
if Weight_c.upper() == "K":
    converted = Weight_o * 2.20
    print("Weight in Lbs: " + str(converted))
elif Weight_c.upper() == "L":
    converted = Weight_o * 0.45
    print("Weight in Lbs: " + str(converted))

# while loops
i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i * "*")
    i = i + 1

# lists
names = ["Mattia", "Ahmed", "Pier", "Dennis"]
print(names)
print(names[0])
print(names[-1])
names[3] = "Denis"
print(names)
print(names[0:-1])

# list methods
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(len(numbers))
print(1 in numbers)
numbers.append(6)
print(numbers)
numbers.insert(0, -1)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.clear()
print(numbers)

# for loops
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

# range() function
numbers = range(5)
for number in numbers:
    print(number)

numbers = range(5, 10)
for number in numbers:
    print(number)

numbers = range(5, 10, 2) # range with a step of 2
for number in numbers:
    print(number)

# tuples
numbers = (1, 2, 3) # tuples cannot be modified


