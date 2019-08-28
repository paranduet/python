###################################################################################
#	Author: H.M. Shah Paran Ali
#	Programming Language: Python
#	Description: pyschool(http://www.pyschools.com/quiz/view_summary) problem practice
#	Email: paran.duet@gmail.com
###################################################################################

################ Variables and Data Types ############
# Topic 1: Question 1: Assign the value 5 to a, and value 6 to b. Assign the value of a + b to variable c.####

a =5
b =6
c =a+b

##### Addition Or Concatenation: Topic 1: Question 2 : It is important to take note of the difference between 
# adding numbers and 'adding' string. 5 + 5 will not produce the same result as '5' + '5'.

'2' + '5' produces '25'

### Using Float : Topic 1: Question 3 :Floating point number is represented with a dot(.) 
# followed by one or more decimals (can be zero).

#Compute the area and perimeter of a circle with radius = 3
pi = 3.14
area =pi*3*3
perimeter =2*pi*3

### Integer And Float : Topic 1: Question 4 :Numbers that contains decimal point are called floating point numbers.
# The type(x) function will return if the argument x is a float. You can use the float(x) and int(x) function to convert values between float and integer.

# Change the type of the variable x to float
# Change the type of variable y to integer

x = 123446754336788543835697
y = 3.14159265358979323846
x =float(x)
y =int(y)

### Using String :Topic 1: Question 5 :Declare a string literal by enclosing the literal using single, double or triple quotes.
# Triple quote allows the literal to span multiple lines.

# Assign foobar which gives the output shown in the last example.
# Hint: Use the triple quote as the outermost quote

foobar ='''"No, thanks, Mom," I said, "I don't know how long it will take."'''

### String And Number :Topic 1: Question 6 :Certain mathematical operations such as addition and multiplication can be used on the String datatype.
# Study the examples given below to see how it works:

# Assign 'HelloWorld!' to variable a
a ="HelloWorld!"

# b contains 'HelloWorld!HelloWorld!HelloWorld!HelloWorld!HelloWorld!'
b = a*5

### Number Of Characters :Topic 1: Question 7 :You can make use of the len(x) function to find out the number of characters in a string.

greeting = "Hello Google!"
# number of characters stored in the variable greeting
number_of_char =len(greeting)

# repeat the greetings based on the number of character in 'greeting'
greetings = greeting*number_of_char 
 
#### String Concatenation :Topic 1: Question 8 :Adding two strings or making multiple copies of the same string.

# Write a function, given a string of characters, return the string together with '_'s of the same length.
def underline(title):
	UndLine=""
	for i in range(len(title)):
		UndLine = UndLine + '_'
	return title +'\n' + UndLine

### String Methods :Topic 1: Question 9 :Introducing some string methods.
# Use one or more string methods in above examples, extract the substring
# surrounded by 'xyz' at the beginning and end. Replace the ',' in the substring with '|'.
# and remove all trailing space.

str1  = 'abcefghxyzThis,is,the,target,string  xyzlkdjf'
idx1 = str1.find( 'xyz'  )                    # get the position of 'xyz'
idx2 = str1.find( 'xyz', idx1+1)            # get the next 'xyz'
str1 = str1[idx1+3:idx2].replace(',', '|')    # replace ',' with '|'
str1 = str1.strip()                             # strip trailing spaces. 

### Basic Types :Topic 1: Question 10 :Like other programming languages, Python also has some basic types like numbers, strings, lists and dictionaries.
# Assign arbitrary values to the variables such that they are of the types used in the examples

a ="abc"
b =123
c =13.32
d =[12,"Paran"]

### Naming Variables :Topic 1: Question 11 :There are some rules in the naming of variables.

b and d

### Complex Number :Topic 1: Question 12 : A integer or floating-point number with trailing 'j' or 'J' is a complex number.

# Compute the sum and product of 2 complex numbers:
# (2+3j) and (4+5j)
import cmath
a = 2+3j
b = 4+5j
sum_ab = a+b
prod_ab = a*b

### String Formatting Operations :Topic 1: Question 13 :Format string output by using the '%' operator

# Write a function that does a decimal to hexadecimal conversion.
# Hint: Make use of "%x" for hexadecimal format.
def dec2hex(num):
	data = hex(num)
	if len(data) < 4 : return data[:2] + '0' + data[2:]
	else: return data
a = 34
b = 0
c = 10

### Accessing String Elements :Topic 1: Question 14 :Accessing string elements.

# Extract each word from 'greetings' and assign to 
# variables 'first', 'middle' and 'last'.
greetings = "How are you"
first  = greetings[ 0:3 ]
middle = greetings[ 4:7 ]
last   = greetings[ 8:11 ]

### Integer (Octal And Hexadecimal) :Topic 1: Question 15 :Octal and hexadecimal integer.

a = 25
b = a
c = a

### Scope Of Variables : Topic 1: Question 16 : Illustrating local and global variables.

x = 1, y = 4

### Data Type :Topic 1: Question 17 :Python supports several data types. The commonly used ones are int, str, float, list, tuple and dictionary.

<type 'int'>

### And/ Or Operator :Topic 1: Question 18 :Python supports the following logical operators: and, or and not.
# These operators can be chained to test for more than one conditions.

True