Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> string1 = "Hello everyone , how are you"
>>> string1[0]
'H'
>>> string1[-1]
'u'
>>> string[0:4]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    string[0:4]
NameError: name 'string' is not defined
>>> string1[0:4]
'Hell'
>>> string1[0:5]
'Hello'
>>> string1[0:]
'Hello everyone , how are you'
>>> string1[:6]
'Hello '
>>> string1[:]
'Hello everyone , how are you'
>>> string1[-1::-1]
'uoy era woh , enoyreve olleH'
>>> string1
'Hello everyone , how are you'
>>> string1.upper
<built-in method upper of str object at 0x000002809ECD9C10>
>>> string1.upper()
'HELLO EVERYONE , HOW ARE YOU'
>>> string1.lower()
'hello everyone , how are you'
>>> string1.capitalize()
'Hello everyone , how are you'
>>> string1.title()
'Hello Everyone , How Are You'
>>> len(string1)
28
>>> string1.center(28)
'Hello everyone , how are you'
>>> string1.center(40)
'      Hello everyone , how are you      '
>>> string1.center(40,"*-")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    string1.center(40,"*-")
TypeError: The fill character must be exactly one character long
>>> string1.center(40,"*")
'******Hello everyone , how are you******'
>>> string1 = string1.center(40,"*")
>>> string1
'******Hello everyone , how are you******'
>>> string1.lstrip()
'******Hello everyone , how are you******'
>>> string1.lstrip("*")
'Hello everyone , how are you******'
>>> string1.rstrip("*")
'******Hello everyone , how are you'
>>> string1.strip("*")
'Hello everyone , how are you'
>>> string1.replace("Hello","HEY")
'******HEY everyone , how are you******'
>>> string1.count('e')
5
>>> string1
'******Hello everyone , how are you******'
>>> string1.count("HEY")
0
>>> string1
'******Hello everyone , how are you******'
>>> string1.count("Hello")
1
>>> string1.find("e")
7
>>> string1.rfind("e")
29
>>> string1.find("e",8)
12
>>> string1[12]
'e'
>>> string1
'******Hello everyone , how are you******'
>>> string1 = string1.strip("*")
>>> string1
'Hello everyone , how are you'
>>> string1.split(" ")
['Hello', 'everyone', ',', 'how', 'are', 'you']
>>> string1 = string1.split(" ")
>>> string1
['Hello', 'everyone', ',', 'how', 'are', 'you']
>>> string1[0]
'Hello'
>>> string1[-1]
'you'
>>> string1[2]
','
>>> "a" > "b"
False
>>> "b">"a"
True
>>> chr("a")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    chr("a")
TypeError: an integer is required (got type str)
>>> ord("A")
65
>>> ord("B")
66
>>> ord("a")
97
>>> ord("b")
98
>>> chr(65)
'A'
>>> chr(99)
'c'
>>> 10/5
2.0
>>> 10%5
0
>>> 
========================== RESTART: C:/Users/Brain Mentors/if-else.py =========================
enter a number10
Even
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
enter a number5
>>> a = 5
>>> 5 == 5
True
>>> a = 10
>>> a > 5
True
>>> a < 5
False
>>> a =5
>>> a <= 5
True
>>> a >= 5
True
>>> a != 5
False
>>> a = 5
>>> b = 5
>>> a is b
True
>>> a is not b
False
>>> ab = [1,2,3,4]
>>> ab[0]
1
>>> ab[-1]
4
>>> 1 in ab
True
>>> 10 in ab
False
>>> ab = [1,2,3,4]#list
>>> 5 not in ab
True
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
enter a number12
Even
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
enter a number12
even
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
enter a number12
even
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
enter a number11
odd
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
{a} is greatest
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
200 is greatest
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
200 is greatest
200 is greator
>>> 
= RESTART: C:/Users/Brain Mentors/if-else.py
200 is greatest
>>> 
>>> 1 > 5 or 5 < 10
True
>>> 1 > 5 and 5 < 10
False
>>> 1 > 5 and not 5<10
False
>>> a = True
>>> if (not a):
	print("hello")

>>> if (a):
	print("hello")

hello
>>> 1 < 5 and not 5 > 10
True
>>> 