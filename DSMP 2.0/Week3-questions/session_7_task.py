# -*- coding: utf-8 -*-
"""session-7-task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16xj8bZOOwxWUujBBKbFWRZZqiGETPYN-

##`Q-1:` Rectangle Class
1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

2. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

3. Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

Eg.
After making above classes and methods, on executing below code:-
```
my_rectangle = Rectangle(3 , 4)
my_rectangle.display()
```

`Output:`
```
The length of rectangle is:  3
The width of rectangle is:  4
The perimeter of rectangle is:  14
The area of rectangle is:  12
```
"""

# write your code here

"""##`Q-2: Bank Class`

1. Create a Python class called `BankAccount` which represents a bank account, having as attributes: `accountNumber` (numeric type), `name` (name of the account owner as string type), `balance`.
2. Create a constructor with parameters: `accountNumber, name, balance`.
3. Create a `Deposit()` method which manages the deposit actions.
4. Create a `Withdrawal()` method  which manages withdrawals actions.
5. Create an `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account.
6. Create a `display()` method to display account details.
Give the complete code for the  BankAccount class.

Eg.
After making above classes and methods, on executing below code:-
```
newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.Withdrawal(700)

newAccount.Deposit(1000)

newAccount.display()
```

`Output:`
```
Account Number :  2178514584
Account Name :  Mandy
Account Balance :  3100 ₹
```
"""

# write your code here

"""##`Q-3:Computation class`

1. Create a `Computation` class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
2. Create a method called `Factorial()` which allows to calculate the factorial of an integer n. Integer n as parameter for this method

3. Create a method called `naturalSum()` allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.

4. Create a method called `testPrime()` in  the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.

5. Create  a method called `testPrims()` allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only `1` as their common divisor. Eg. 4 and 9 are prime to each other.

5. Create a `tableMult()` method which creates and displays the multiplication table of a given integer. Then create an `allTablesMult()` method to display all the integer multiplication tables 1, 2, 3, ..., 9.

6. Create a static `listDiv()` method that gets all the divisors of a given integer on new list called  Ldiv. Create another `listDivPrim()` method that gets all the prime divisors of a given integer.
"""

# write your code here

"""##`Q-4`: Build flashcard using class in Python.

Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

**Example 1:**

Approach:

- Create a class named FlashCard.
- Initialize dictionary fruits using __init__() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
- Now randomly choose a pair from fruits by using _random_ module and store the key in variable _fruit_ and _value_ in variable color.
- Now prompt the user to answer the color of the randomly chosen fruit.
- If correct print correct else print wrong.

Output:
```bash
welcome to fruit quiz
What is the color of Strawberries
pink
Correct answer
Enter 0, if you want to play again: 0
What is the color of watermelon
green
Correct answer
Enter 0, if you want to play again: 1
```
"""

# write your code here

"""## `Q-5:` Problem 5 based on OOP Python.

TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:
- eligibility criteria:
    - if experience is more than 3 years, average feedback should be 4.5 or more
    - if experience is 3 years or less, average feedback should be 4 or more
- he/she should posses the technology skill for the course

Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

**Note:**
- Consider all instance variables to be private and methods to be public.
- An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
- *check_eligibility()*: Return true if eligibility criteria is satisfied by the instructor. Else, return false
- *allocate_course(technology)*: Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.

Represent a few objects of the class, initialize instance variables using setter methods, invoke
appropriate methods and test your program.
"""

# write your code here