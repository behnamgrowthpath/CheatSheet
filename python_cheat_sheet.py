#? -->  should I do or not
#! --> be careful about it
#todo --> don't forget to add here
#// --> it had tested and didn't work
#* --> highlighted


name = input("what is your name?")  # save as string ( " or ' )    usage of backslash --> print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')
print('hi ' + name)                  # \n : new line   \t : tab  \  : space
print('%' * 4)

# string formatting --> also it has many other functions to do more stuff

course = ' python for beginners' 
# We can slice a string using a similar notation:
course[1:11]

adadha = [4, 6, 7]
massage = "Numbers: {0} {1} {2}".format(adadha[0], adadha[1], adadha[2])  # Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.
print(massage)
a = "{x}, {y}".format(x=5, y=12)
print(a)
b = f'also numbers: {adadha[0]} , {adadha[1]} & {adadha[2]}'
print(b)
# Conditional expressions are also known as applications of the ternary operator.
a = 7
b = 1 if a >= 5 else 42
print(b)

print("$ ".join(["spam", "eggs", "ham"]))
# prints "spam$ eggs$ ham"
print("Hello ME".replace("ME", "world"))
# prints "Hello world"
print("This is a sentence.".startswith("This"))
# prints "True"
print("This is a sentence.".endswith("sentence."))
# prints "True"
print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."
print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"
print("spam, eggs, ham".split(", "))
# prints "['spam', 'eggs', 'ham']"
course.find('p') # returns the index of the first occurrence of p (or -1 if not found)
# 20 // 6 = 3 --> int
# 2 ** 4 = 16 
# 12 / 6 = 2.0 --> float
# 7 % 2 = 1
# In-place operators ( += ) can be used for any numerical operation (+, -, *, /, %, **, //).

# Numberic functions:
print(max([1, 4, 9, 2, 5, 6, 8]))
print(min(1, 2, 3, 4, 0, 2, 1))
print(sum([1, 2, 3, 4, 5]))
print(abs(-99))  # meghdar mide
price = 10
rating_1234 = 4.9
is_published = True  # False

if is_published is None:  # --> None == null
    del is_published  # make it undefined

print(type(price))  # = integer
price = float(price)             # float() / str() / int() / bool()
print(type(price))  # = float

print("Annie" > "Andy")  # shows true

if not 1 != 2:
    x = 2
elif (1 == 2):
    x = 3
else:
    x = 4 
print(x)

# we use "and", "or" & "not" within the booleans.

# [lists] :  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

str = "Hello world!"
print(str[6])

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

""" --> comment
To check if an item is in a list, the in operator can be used. 
It returns True if the item occurs one or more times in the list, and False if it doesn't.
The in operator is also used to determine whether or not a string is a substring of another string.
"""
print(1 in nums)
print(2 not in nums)
# this returns a boolean ,so it could use as the condition of code like in if statements.

nums.append(4)  # clear / copy / count / extend / index / insert / pop / remove / reverse / sort
nums.append(6) # adds 6 to the end
nums.insert(0, 6) # adds 6 at index position of 0
print(len(nums))  # max / min

square = [1, 2, 3, 4, 5, 6, 7]
print(square[3:5:1])  # like Range the second index doesn't appear. # slicing # we can use negative value in second index to count from the end. also we can use negative value in third index to go backward.

evens = [i**2 for i in range(10) if i % 2 == 0]
print(evens)

nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")
if any([i % 2 == 0 for i in nums]):
    print("At least one is even")
dict_nums = {}
for v in enumerate(nums):
    a , b = v
    dict_nums[a] = b
print(dict_nums)

# {Dictionaries} : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# We can use strings or numbers to define keys. They should be unique. We can use any types for the values.
squares = {1: 1, 2: True , 3: "error", 4: 16.5}
squares[8] = 64
squares[3] = 9

print(squares)


ages = {"Dave": 24, "Mary": 42, "John": 58}  # a dictionary can store any types of data as values.
print(ages["Dave"])

# in / not in --> booleans

pairs = {1: "apple", "orange": [2, 3, 4], None: "True"}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary")) # get function just returns values.

# (Tuples) : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

tp = ("1", "2", 3, 4, [1, 2, 3], (5, 6))  # tuples are faster than the lists ,but they can not be changed. They are like read-only lists.
print(tp[1::3])  # slicing # we can use negative value in second index to count from the end. also we can use negative value in third index to go backward.
print(tp[:3:1])
numbers = (1, 2, 3, 4)
a, *b, c = numbers
# A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables.

# {Sets} : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

num_set = {1, 2, 3, 4, 5}
num_list = list(num_set)
print(num_list)
word_set = set(["spam", "eggs", "sausage"])
print( word_set )
num_set.add(44)  # also such other functions.
# They share some functionality with lists, such as the use of in to check whether they contain a particular item.
# Basic uses of sets include membership testing and the elimination of duplicate entries.
# They can't be indexed. 

String = 'GeeksForGeeks'
set1 = set(String)
print(set1)

set1 = set(["Geeks", "For", "Geeks"])  
print(set1)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)  # ejtema
print(first & second)  # eshterak
print(first - second)  # menha
print(second - first)  # menha
print(first ^ second)  # delta

"""
When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast look up for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
lists:  SIMPLE, CHANGEABLE, MUTABLE, ORDERED.
sets: UNIQUENESS, UNORDERED, IMMUTABLE, NOT CHANGEABLE,
tuples: IMMUTABLE, NOT CHANGEABLE, ORDERED
"""

# loops : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

i = 1
while True:
    i += 1
    break    # start from the first line after the loop
    continue  # stop the current loop and start from the beginning

words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

char = "testing for loops"
count = 0
for x in char:
    if(x == 't'):
        count += 1
print(count)  # shows the number of 't' in the text.

# The range() function returns a sequence of numbers.
print(list(range(10)))
print(range(20) == range(1, 20))  # False : 0-19 != 1-19
# range can have a third argument, which determines the interval of the sequence produced, also called the step.
for i in range(5):
    print(i)

# Functions : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def my_func(x):  # x is the function argument.
    print("here is the " + x)


my_func(input("write a text for my_func defenition: "))


def my_func_with_return(x):
    return int(x) + 1 
    # Any code after the return statement will never happen. we can use return as we use break in the loops.


print(my_func_with_return(input("write a number for my_func defenition: ")))


def multiply(x, y):
    return x * y


a, b = 1, 2
operation = multiply   # variables can become functions.
print(operation(a, b))

# The None object is returned by any function that doesn't return anything else.

# Pure functions are same as function in mathematic because they return same values for same arguments.

"""
Creating a function normally (using def) assigns it to a variable automatically. 
This is different from the creation of other objects - such as strings and integers - which can be created on the fly, without assigning them to a variable. 
The same is possible with functions, provided that they are created using lambda syntax. Functions created this way are known as anonymous.
"""

def my__func(f, arg):
    return f(arg)


print(my__func(lambda x: 2*x*x, 5))

# lambdas can only do things that require a single expression - usually equivalent to a single line of code.
double = lambda x: x * 2 # lambda variable_name : s.th we want to return which includes variable_name
print(double(7))

print((lambda x: x**2 + 5*x + 4)(-4)) # --> very useful

# The function MAP takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument. 
# The function FILTER filters an iterable by removing items that don't match a predicate (a function that returns a Boolean). 
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x + 5, nums))
print(result)
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)  


def polynomial(x):
    return x**2 + 5*x + 4

print(polynomial(-4))

# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function. 
# .  **kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance. The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.
# Named parameters to a function can be made optional by giving them a default value. These must come after named parameters without a default value.

def my_func(x, y=7, *args, **kwargs):
    print(kwargs, args, x, y)

my_func(2, 3, 4, 5, 6, a=7, b=8)


"""
The else statement is most commonly used along with the if statement, but it can also follow a for or while loop, which gives it a different meaning. 
With the for or while loop, the code within it is called if the loop finishes normally (when a break statement does not cause an exit from the loop).
"""

"""
The module itertools is a standard library that contains several functions that are useful in functional programming. 
One type of function it produces is infinite iterators.
    count / cycle / repeat / chain / takewhile / ccumulate / permutations / product
"""
# Generators / Decorators / Recursion : ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Generators are a type of iterable, like lists or tuples. 
# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops. 
# The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)
# Finite generators can be converted into lists by passing them as arguments to the list function.
# In fact, they can be infinite!

# Decoratos are functions that modify other functions.


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    wrap()

def print_text():
    print("Hello world!")


def decorated(): decor(print_text)
decorated()
# We can also use @ symbol to decorate s.th but its confusing.

# Recursion is the fundamental part of recursion is self-reference - functions calling themselves.


def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)


print(factorial(5))

# Modules : //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
The basic way to use a module is to add 'import module_name' at the top of your code, and then using 'module_name.var' to access functions and values with the name var in the module.
There is another kind of import that can be used if you only need certain functions from a module.
These take the form 'from module_name import var1,var2' and then var can be used as if it were defined normally in your code. 
You can import a module or object under a different name using the 'as' keyword. # from math import sqrt as square_root
The complete documentation for the standard library is available online at www.python.org.
Many third-party Python modules are stored on the Python Package Index (PyPI). 
The best way to install these is using a program called pip. This comes installed by default with modern distributions of Python.
If you don't have it, it is easy to install online. Once you have it, installing libraries from PyPI is easy.
Look up the name of the library you want to install, go to the command line (for Windows it will be the Command Prompt), and enter pip install library_name. Once you've done this, import the library and use it in your code.
"""

# Exceptations : /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
Different EXCEPTIONs are raised for different reasons. 
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly.
TypeError: a function is called on a value of an inappropriate type or using a mutable object as the key of dictionary or trying to reassign a value in tuple.
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
KeyError: when we call s.th that is not define in dictionary.
MemoryError: trying to make s.th too extentive. --> solved by Generators
RuntimeError: some infinite loops in functions.
AttributeError: s.th not defined in the class but called within the project.
To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
The try block contains code that might throw an exception. If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. If no error occurs, the code in the except block doesn't run.
"""

try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

except (ValueError, TypeError) as e:
    print(e)
except:    # won't happen if other exceptions happen
    print("An error occurred")
finally:   # always happen
    print("This code will run no matter what")

# try/finally even have other usages in somewhereelse.
# we can use raise statment to show exception without any apearance.
"""
The else statement can also be used with try/except statements. 
In this case, the code within it is only executed if no error occurs in the try statement.
"""

"""
# An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
# An expression is tested, and if the result comes up false, an exception is raised.
print(1)
assert 2 + 2 == 4 ,"not true"
print(2)
assert 1 + 1 == 3 ,"not true"     # AssertionError: not true  --> this is what shows us on the screen
print(3)                          # does not happen
# the rest of the code won't happen
"""

# Opening & Working with Files :  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
file = open("filename.txt", "r+") # "w" "r" "a" "-b"
print(file.read(16)) # bytes of file
print(file.read(4))
cont = file.read()
# After all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.
for line in file:
        print(line)
# also we can use print(file.readlines())
file.write("This has been written to a file") 
# The "w" mode will create a file, if it does not already exist. 
# When a file is opened in write mode, the file's existing content is deleted.
# The write method returns the number of bytes written to a file, if successful.  -->  file.write(msg) == len(msg)
# do stuff to the file
file.close()

# The file is automatically closed at the end of the with statement, even if exceptions occur within it.
with open("filename.txt") as f:
  print(f.read())

# Text analyzer :
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count
filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} -> {1}%".format(char, round(perc, 2)))
"""
# Classes and inheritance: ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""
The __init__ method is the most important method in a class. 
This is called when an instance (object) of the class is created, using the class name as a function.
Method is s.th like function but it runs on an object.
All methods must have self as their first parameter, although it isn't explicitly passed, Python adds the self argument to the list for you; you do not need to include it when you call the methods. Within a method definition, self refers to the instance calling the method.
In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.
Classes can have other methods defined to add functionality to them. 
Remember, that all methods must have self as their first parameter.
Classes can also have class attributes, created by assigning variables within the body of the class.
Inheritance provides a way to share functionality between classes. 
Magic methods are special methods which have double underscores at the beginning and end of their names. They are also known as dunders.
One common use of them is operator overloading. This means we can define custom behavior for each operator.
"""
class animal :
  legs = 2 
  def __init__(self, color, generation):
      self.color = color
      self.generation = generation
class dog(animal) :
  legs = 4   
  def voice(self):
    print("wooof!")
    print(super().legs) # The function super is a useful inheritance-related function that refers to the parent class. It can be used to find the method with a certain name in an object's superclass.
billy = dog("","")
patrick = dog("gray","1th")
print(patrick.color)
patrick.voice()

class math2D :
  def __init__(self, x,y,string):
    self.x = x
    self.y = y
    self.string = string 
  def __add__(self, other):   # such other ones are __sub__(-) , __mul__(*) , __truediv__(/) , __floordiv__(//) , __mod__(%) , __pow__(**) , __and__(&) ,__xor__(^) , __or__(|)   
                              # also python have these for comparisons  __lt__(<) , __le__(<=) , __eq__(==) , __ne__(!=) , __gt__(>) , __ge__(>=) 
                              # __len__(len()) , __getitem__(indexing) , __setitem__(assignning to indexed values) , __delitem__(deleting indexed values) , __iter__(iteration over object) , __containd__(in)
    return math2D(self.x + other.x , self.y + other.y,"")
    # The expression x + y is translated into x.__add__(y) # If the types are different we can use "r" after first two underscores.
  def __truediv__(self,other):
    line = "$" * len(other.string)
    return "\n".join([self.string,line,other.string])



A = math2D(3,4,"Robert")
B = math2D(5,6,"Kiosuki")
result = A + B
print(result)
print(A / B)

# __del__ is for managing the memory and garbage collection.


class forshow :
  qwerty = 1      # --> public
  _qwerty = 2     # --> encapsulation: s.th with low chance of usong out of the class
  __qwerty = 3    # --> private: it could be used as public with _ClassName__PrivateObject
  @classmethod
  def NotSelfUse(cls,parameter):        # --> class method
    return None
  @staticmethod
  def NoAdditionalArgument(parameter0): # --> static method are identical to normal functions that belong to a class.
    return None
  @property 
  def ReadOnlyAttribute(self):
    return True
  """
  Properties can also be set by defining setter / getter functions.
  The setter function sets the crosspending property's value.
  The getter gets the value.
  """
  @ReadOnlyAttribute.setter
  def ReadOnlyAttribute(self, value):
    forshow.ReadOnlyAttribute.value = bool(input("True/False"))
    return value
  
# GAME :
"""
def get_input():
  command = input(": ").split()  # split --> divide a string to seprated words
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return
  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))
def say(noun):
  return 'You said "{}"'.format(noun)
verb_dict = {"say": say,  "examine": examine,}
class GameObject:
  class_name = ""
  desc = ""
  objects = {}
  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self
  def get_desc(self):
    return self.class_name + "\n" + self.desc
class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)
  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line
  @desc.setter
  def desc(self, value):
    self._desc = value
goblin = Goblin("Gobbly")
def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)
def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg
while True:
  get_input()
  """

#
#
#
#
#
#
#
#
#
#


  # Regular expressions are a powerful tool for various kinds of string manipulation.
import re
pattern = r"spam"   # To avoid any confusion while working with regular expressions, we would use raw strings as r"expression". Raw strings don't escape anything, which makes use of regular expressions easier.
if re.match(pattern, "spamspamspam"):  # The re.match function can be used to determine whether it matches at the beginning of a string. If it does, match returns an object representing the match, if not, it returns None.
  print("Match")
else:
  print("No match")
# The function re.search finds a match of a pattern anywhere in the string.
# The function re.findall returns a list of all substrings that match a pattern.
# The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
"""
The regex search returns an object with several methods that give details about it. 
These methods include group which returns the string matched, start and end which return the start and ending positions of the first match, and span which returns the start and end positions of the first match as a tuple.
"""
match = re.search(pattern, "eggspamsausage")
if match:
  print(match.group())
  print(match.start())
  print(match.end())
  print(match.span())
# Sub method replaces all occurrences of the pattern in string with repl, substituting all occurrences, unless count provided. This method returns the modified string. 
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

""""""

# Metacharacters are what make regular expressions more powerful than normal string methods.
# The first metacharacter we will look at is . (dot). This matches any character, other than a new line.
pattern = r"gr.y"
if re.match(pattern, "grey"):
  print("Match 1")
if re.match(pattern, "gray"):
  print("Match 2")

""""""

# The next two metacharacters are ^ and $. These match the start and end of a string, respectively.
# The pattern "^gr.y$" means that the string should start with gr, then follow with any character, except a newline, and end with y.

""""""

# Character classes provide a way to match only one of a specific set of characters.
# A character class is created by putting the characters it matches inside square brackets.
pattern = r"[aeiou]"
if re.search(pattern, "yeki az on class bayad hadeaghal inja bashe"):
  print("Match 2")
# Character classes can also match ranges of characters. 
pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS8"):
  print("Match 1")
if re.search(pattern, "E3"):
  print("Match 2")
if re.search(pattern, "1ab"):
  print("Match 3")
"""
Place a ^ at the start of a character class to invert it. 
This causes it to match any character other than the ones included. 
Other metacharacters such as $ and ., have no meaning within character classes. 
"""

""""""

# The metacharacter * means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible. The "previous thing" can be a single character, a class, or a group of characters in parentheses.
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
  print("Match 1")
if re.match(pattern, "eggspamspamegg"):
  print("Match 2")
if re.match(pattern, "spam"):
  print("Match 3")
# The example above matches strings that start with "egg" and follow with zero or more "spam"s.
# The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".
# The metacharacter ? means "zero or one repetitions".
"""
Curly braces can be used to represent the number of repetitions between two numbers.
The regex {x,y} means "between x and y repetitions of something". 
Hence {0,1} is the same thing as ?.
If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
"""

# Groups: '([^aeiou][aeiou][^aeiou])+' matchs one or more repetitions of a non-vowel, a vowel and a non-vowel
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
  print(match.group())
  print(match.group(0))
  print(match.group(1))
  print(match.group(2))
  print(match.groups())

# Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
# Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
  print(match.group("first"))
  print(match.groups())
# Another important metacharacter is |. This means "or", so red|blue matches either "red" or "blue".
pattern = r"gr(a|e)y"

""""""

"""
There are various special sequences you can use in regular expressions. They are written as a backslash followed by another character. 
One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. 
This matches the expression of the group of that number.
"""
pattern = r"(.+) \1"
match = re.match(pattern, "word word")
if match:
  print ("Match 1")
match = re.match(pattern, "?! ?!")
if match:
  print ("Match 2")    
match = re.match(pattern, "abc cde")
if match:
  print ("Match 3")
"""
More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively. 
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.
"""
"""
Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively. 
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else.
"""
pattern = r"\b(cat)\b"
match = re.search(pattern, "The cat sat!")
if match:
  print ("Match 1")
match = re.search(pattern, "We s>cat<tered?")
if match:
  print ("Match 2")
match = re.search(pattern, "We scattered.")
if match:
  print ("Match 3")

# Email:
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

str = "Please contact info@sololearn.com for assistance"
match = re.search(pattern, str)
if match:
    print(match.group())

import this
"""
The Zen of Python, by Tim Peters  --> import this

--> PEP

    Most Python code is either a module to be imported, or a script that does something. 
However, sometimes it is useful to make a file that can be both imported as a module and run as a script. 
To do this, place script code inside if __name__ == "__main__". 
This ensures that it won't be run if the file is imported.
"""

"""
In Python, the term packaging refers to putting modules you have written in a standard format, so that other programmers can install and use them with ease. 
This involves use of the modules setuptools and distutils. 
The first step in packaging is to organize existing files correctly. Place all of the files you want to put in a library in the same parent directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory.
This directory goes into another directory containing the readme and license, as well as an important file called setup.py. 
Example directory structure:

SoloLearn/
    LICENSE.txt
    README.txt
    setup.py
    sololearn/
      __init__.py
      sololearn.py
      sololearn2.py

The next step in packaging is to write the setup.py file. 
This contains information necessary to assemble the package so it can be uploaded to PyPI and installed with pip (name, version, etc.).
Example of a setup.py file:
from distutils.core import setup

setup(
    name='SoloLearn', 
    version='0.1dev',
    packages=['sololearn',],
    license='MIT', 
    long_description=open('README.txt').read(),
)

After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer).
To build a source distribution, use the command line to navigate to the directory containing setup.py, and run the command python setup.py sdist.
Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary distribution. 
Use python setup.py register, followed by python setup.py sdist upload to upload a package.
Finally, install a package with python setup.py install.

The previous lesson covered packaging modules for use by other Python programmers. However, many computer users who are not programmers do not have Python installed. Therefore, it is useful to package scripts as executable files for the relevant platform, such as the Windows or Mac operating systems. This is not necessary for Linux, as most Linux users do have Python installed, and are able to run scripts as they are. 
For Windows, many tools are available for converting scripts to executables. For example, py2exe, can be used to package a Python script, along with the libraries it requires, into a single executable.
PyInstaller and cx_Freeze serve the same purpose.
For Macs, use py2app, PyInstaller or cx_Freeze.
"""
