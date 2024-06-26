# -*- coding: utf-8 -*-
"""session12-task-generator-decorator-iterator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lKVrogPUGsIBgrQimzmYginZddEKufbj

## Namespace and Scope

###`Q1:` Write `Person` Class as given below and then display it's namespace.

```
Class Name - Person

Attributes:
name - public
state - public
city - private
age - private

Methods:
address - public
It give address of the person as "<name>, <city>, <state>"
```
"""

#Write your code here



"""###`Q2:` Write a program to show namespace of object/instance of above(Person) class."""

# Write your code here



"""###`Q3:` Write a recursive program to to calculate `gcd` and print no. of function calls taken to find the solution.
```
gcd(5,10) -> result in 5 as gcd and function call 4
```
"""

#Write your code here



"""## Itterator And Generator

###`Q4:` Create MyEnumerate class,
Create your own `MyEnumerate` class such that someone can use it instead of enumerate. It will need to return a `tuple` with each iteration, with the first element in the tuple being the `index` (starting with 0) and the second element being the `current element` from the underlying data structure. Trying to use `MyEnumerate` with a noniterable argument will result in an error.

```
for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')
```

Output:
```
0 : a
1 : b
2 : c
```
"""

#Write your code here





"""###`Q5:` Iterate in circle
Define a class, `Circle`, that takes two arguments when defined: a sequence and a number. The idea is that the object will then return elements the defined number of times. If the number is greater than the number of elements, then the sequence  repeats as necessary. You can define an another class used as a helper (like I call `CircleIterator`).

```
c = Circle('abc', 5)
d = Circle('abc', 7)
print(list(c))
print(list(d))
```

Output
```
[a, b, c, a, b]
[a, b, c, a, b, c, a]
```
"""

#Write your code here







"""###`Q6:` Generator time elapsed
Write a generator function whose argument must be iterable. With each iteration, the generator will return a two-element tuple. The first element in the tuple will be an integer indicating how many seconds have passed since the previous iteration. The tuple’s second element will be the next item from the passed argument.

Note that the timing should be relative to the previous iteration, not when the
generator was first created or invoked. Thus the timing number in the first iteration
will be 0

```
for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)
```

Output:
```
(0.0, 'a')
(2.005651817999933, 'b')
(2.0023095009998997, 'c')
(2.001949742000079, 'd')
```
Note: Your output may differ because of diffrent system has different processing configuration.
"""

#Write yor code



"""## Decorators

###`Q7:` Write a Python program to make a chain of function decorators (bold, italic, underline etc.) on a given function which prints "hello world"

```
def hello():
    return "hello world"
```

```
bold - wrap string with <b> tag. <b>Str</b>
italic - wrap string with <i> tag. <i>Str</i>
underline- wrap string with <u> tag. <u>Str</u>
```
"""

#Write your code here



"""###`Q8:` Write a decorator called `printer` which causes any decorated function to print their return values. If the return value of a given function is `None`, printer should do nothing.


"""

#Write your code here



"""###`Q9:` Make a decorator which calls a given function twice. You can assume the functions don't return anything important, but they may take arguments.
```
#Lets say given function
def hello(string):
    print(string)

#on calling after specified decorator is inplaced
hello('hello')
```

Output:
```
hello
hello
```
"""

#Write your cod here





"""### `Q10:` Write a decorator which doubles the return value of any function. And test that decoratos is working correctly or not using `asert`.

```
add(2,3) -> result in 10. Without decorator it should be 5.
```
"""

# Write your code here

