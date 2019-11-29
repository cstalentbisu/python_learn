Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import *
>>> color('red','red')
>>> begin_file()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    begin_file()
NameError: name 'begin_file' is not defined
>>> from turtle import *
>>> color('red','red')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    color('red','red')
  File "<string>", line 5, in color
turtle.Terminator
>>> from turtle import *
>>> color('red','red')
>>> for i in range(5):
	fd(200)
	rt(144)

	
>>> end_fill()
>>> >>> from turtle import *
>>> color('red','red')
>>> for i in range(5):
	fd(200)
	rt(144)

	
>>> end_fill()
>>> 
SyntaxError: invalid syntax
>>> from turtle import *
>>> color('red','blue')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    color('red','blue')
  File "<string>", line 5, in color
turtle.Terminator
>>> cls
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> clear
<function clear at 0x0000022BCA897DC0>
>>> from turtle import *
>>> color('red','red')
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	fd(200)
	rt(144)

	
>>> 
