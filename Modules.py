Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
 RESTART: C:\Users\lenovo\AppData\Local\Programs\Python\Python37-32\Functions.py 
Adarsh 23 N
1 2 3
2
2
2
10
{'a': 1, 'b': 2, 'c': 3}
(1, 2, 3, 4, 5) 9
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
Traceback (most recent call last):
  File "C:\Users\lenovo\AppData\Local\Programs\Python\Python37-32\Functions.py", line 119, in <module>
    import Assin2
ModuleNotFoundError: No module named 'Assin2'
>>> 
 RESTART: C:\Users\lenovo\AppData\Local\Programs\Python\Python37-32\Functions.py 
Adarsh 23 N
1 2 3
2
2
2
10
{'a': 1, 'b': 2, 'c': 3}
(1, 2, 3, 4, 5) 9
>>> Functions.seq()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Functions.seq()
NameError: name 'Functions' is not defined
>>> import Functions
Adarsh 23 N
1 2 3
2
2
2
10
{'a': 1, 'b': 2, 'c': 3}
(1, 2, 3, 4, 5) 9
>>> Functions.seq()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Functions.seq()
TypeError: seq() missing 3 required positional arguments: 'first', 'second', and 'third'
>>> Function.seq(second=2,first=4,third=3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    Function.seq(second=2,first=4,third=3)
NameError: name 'Function' is not defined
>>> Functions.seq(second=2,first=1,third=3)
1 2 3
>>> import Functions as F
>>> dir()
['F', 'Functions', 'Kw', 'VKA', '__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'default', 'details', 'ret', 'seq', 'vp']
>>> 
