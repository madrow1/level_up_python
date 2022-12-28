# Strings in python are a way of storing text variables, they are immutable and can be defined using single or double quotes.
greet = "Hello World"
print(greet)

# Multiple strings can be contatonated together using a + 
extended_greet = "Hello" + " " + "World" 
print(extended_greet)

# It is also possible to format strings with {$variable}, for this to work f must be before the string, so the format is : 
# f"string {$variable}" 
name = "Rowan"
interupt = f"Hello, {name}"
print(interupt)

# The .format() string method can also be used 
format_test = "Hello {}"
formatted = format_test.format(name)
print(formatted)