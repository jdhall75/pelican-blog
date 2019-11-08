Title: Getting Started
Date: 2019-11-08 13:30
Category: Python
slug: python-starter
Author: Jason Hall
status: published
tags: python, learning, educational
keywords: python, learning, educational, python learning, classes
Summary: Places to practice your Python 

---

# Yet another introduction to Python


## Places to get familiar with Python
This will be a quick introductory write up on Python the language and a couple of tools that you can use while you're getting started. 


### Python REPL - (Good) 
---
What the heck is REPL, right?  I just had to google it myself.  It stands for **_Read - Evaluate - Print - Loop_**.  The Python REPL will allow you to enter in python code and get immediate feedback from it.  It's good for starting off and allows you to get aquainted with the language or work out a quick tid bit in a larger application.  Lets take a quick look at it.

```python
C:\Users\jdhall>python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # In python a # sign starts a comment
# text wrapped in quotes is know as a string
>>> 'this is a string'
'this is a string'
>>> # this is an comment about the next line
# 8 is an integer or an int
# When you type it into the REPL and hit enter it will Read the statement, Evaluate it, Print it back to you, and the return you to the REPL command line(Loop). 
>>> 8
8
# you see no quotes around it. Look back at the this is a string example
# You can use the REPL as a calculation
>>> 10 * 15
150
>>> 100 / 2
50.0
>>> 100 + 200
300
# you can add strings together as well
>>> "String 1" + "String 2"
'String 1String 2'
>>>
```

#### Quick Recap
So, What did we see?  We saw that we can play with python directly on the command line and learned about the 2 simplest forms of data type.

##### Strings
String Can be enclosed with any of the following forms
```python
'A string in single quotes'

"A string in double quotes"

'''
This is known as a docstring.  It can be used 
for assigning multi line text to a variable.  The text
is wrapped in 3 single or double quotes.  The 
reason its called a docstring is its meant to be 
for documentation purposes, but you'll see it used
in a lot of other places.  We will get into 
variables  and docstrings soon.
'''
```

##### Integers
Integers are whole numbers, no decimal places.  Those would be floats or a floating point number.  
As we saw above you can add numbers together, but one thing I didn't go over is you can't add strings and integers together.
You can add a float and a integer together however.  It has to do how these data types are handled by Python.

Picking up where we left off above.

```
...
>>> "String 1" + "String 2"
'String 1String 2'
# You can see here we get an error aka. an exception when trying to add a string and an integer
>>> 8+"this is a string"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
# but the int and the float worked just fine.  The result is float is returned by the REPL
>>> 10 + 10.5
20.5
```
 
### [REPL.it](https://repl.it/) (Better)
---
REPL.it it s a really handy tool for working with Python.  It supports many other languages as well.  So if PHP or C++ is your thing you can get some real use out of it.  The main thing I like about it over the command line REPL is you can a code "editor".  You don't have to arrow up or keep typing the same things in over and over again to sus' something out.  The other added benefits to using REPL.it are; a file manager, a simple way to run your app(the run button), the ability to save your work in the cloud, access to popular python packages, the list goes on and on...  There is all of that and a "bag of chips",  you have access to a whole community of developers that you can ask for help, share your REPL, and use "live editing" with someone else to see where you may have gone wrong.

![REPL.it](/images/replit_front_25.png)


This is where I'm gonna leave ya for now.  We'll be back at it next week.  Look at the more info stuff below. Play around with the REPL and I'll get some stuff together for next week.

## More info
[Python Builtin Datatypes](https://docs.python.org/3/library/stdtypes.html)

