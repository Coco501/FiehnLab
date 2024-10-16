"""
This is going to be a multiline comment
yada yada yada
"""
#dont need semi-colons after lines
#strings can be written with " or '
#print() function like cout
#no need to declare data type when initializing variable
#can change data type of variable after declaring it easily
#use type() to get the data type of a variable
#variable names are case sensitive, a != A
#variable names must start with letter or _, no special characters or numbers
#variable names cannot be any of the python keywords
#naming conventions:
#camel = myVariable
#Pascal = MyVariable
#Snake = my_variable
#assigning multiple values in one line is allowed, "x, y, z = 5, 4, "Banana"
#can also assign one value to multiple variables, "x = y = z = 5"
#if you have a list "fruits = [apple, banana, orange]", you can unpack them by assigning variables to its contents: "x, y, z = fruits"
#can print out multiple things separated by comma, print(x, y + z) (comma adds space between them, can use + for no space)
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y + z)
"""
#for numbers though, print(x+y) will give us the sum, not both x and y
#cannot combine string and number when printing with +, like print(str+x)
#use def to define a function and then colon after (), ie def myFunc():
#create global variables by declaring them outside of functions
#if you have a global variable, you can have a new variable with the same name inside a function
#can declare global variables inside functions by writing global before the variable name
#or use "global" to change a global variable when working with it inside a function
#built in data types:
"""
text: str
numbers: int, float, complex (1j, imaginary (j))
sequences: list, tuple, range
mapping: dict
set: set, frozenset
boolean: bool
binary: bytes, bytearray, memoryview
none: NoneType

examples:
x = "Hello World" 	                            str 	
x = 20                              	        int 	
x = 20.5                            	        float 	
x = 1j 	                                        complex 	
x = ["apple", "banana", "cherry"] 	            list 	
x = ("apple", "banana", "cherry") 	            tuple 	
x = range(6) 	                                range 	
x = {"name" : "John", "age" : 36} 	            dict 	
x = {"apple", "banana", "cherry"}           	set 	
x = frozenset({"apple", "banana", "cherry"}) 	frozenset 	
x = True 	                                    bool 	
x = b"Hello" 	                                bytes 	
x = bytearray(5) 	                            bytearray 	
x = memoryview(bytes(5)) 	                    memoryview 	
x = None 	                                    NoneType 	
"""
#for random numbers:
"""
import random
print(random.randrange(1,10))
#this would print random #s between 1 and 9
"""
#casting integers:
"""
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
"""
#empty lists are "false" in terms of boolean, anything but 0 is true
#empty string is false, 0 is false, None is false, (), [], {}, are false
#if statements: if condition:
#then indents are very important, all same indents will be part of the if statement until new ident
"""
x = 0
if x:
    print('x is true')
    print('x is', x)

print('x is false')
"""


