# Define a function with no parameters that prints a static message
def greet():
    print("Welcome")

# Call the greet function
greet()


# Define a function that accepts a single argument ('message')
def greeting(message):
    print(message)

# Call the greeting function and pass "Welcome" as the argument
greeting("Welcome")


# Define a function that takes two numbers and returns both their sum and product
def calc(a, b):
    return a + b, a * b

# Call the calc function with 5 and 10, unpacking the two returned values into separate variables
total, product = calc(5, 10)

# Print the calculated sum
print(total)

# Print the calculated product
print(product)

#default argument
def greetings(name="Guest"):
    print("Welcome", name)
greetings("Chandan")
greetings()

#keyword argument
def student_info(name,age,city):
    print(name,age,city)
student_info("Chandan",20,"Bangalore")