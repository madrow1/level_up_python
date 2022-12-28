names = ["John", "Paul", "George", "Ringo"]
ages = [20, 21, 22, 23]

# There are two main kinds of loop in Python, for, and while.
# A while loop operates while a condition is met, this issue with while is that they can infinitely loop if the condition is never met
# For example the loop "while i = True: " will continue to loop until the conditional becomes false.
i = 0 
while i < len(ages):
    print(names[i], ages[i])
    i += 1 

# There are also for loops, these are fractional and loop until the loop is whole for x in y 
for name in names:
    print(name)

# It is also possible to combine lists with the zip function and loop through them with two iterators 
# This can then be formatted using {}
for name,age in zip(names,ages):
    print(f"{name} {age}")

# It is possible to use string methods to change the output, the below will reverse the list 
for name in reversed(names):
    print(name)

# The range method can be used if you are not looping to a list or other variable (or if you are, integers cannot be looped so these have to be converted to range)
for i in range(5):
    print(i)

# The enumeration method can 