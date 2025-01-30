# Introduction
Welcome to a crash course in python basics. By the end of this document, you will have all the tools to create your very own python game!

This doc is for reference for you to use in the future to make other projects or create a replica of the project. 

# Table Of Contents
Here's what we are covering in this course:

- Print Statements, Commenting, and Formatting
- If-Else Statements
- Variables & User Input
- While Loops

# Print Statements
Print statements allow you to display some text for the user to see. In python, this is pretty simple.

```
print("Hello World!")
```
The user sees:
> Hello World!

> [!IMPORTANT]
> Remember to include the double quotes (") when writing your text inside the brackets!

## Commenting
Sometimes, it helps to keep track of what your code is doing, or maybe even to help someone else understand your code. Commenting is a way of doing that.

Comments are lines of code that the computer doesn't run, they are only there for you to see.

To comment a line of code in python, we put a # before we start writing. Everything in that row after  the # will not be run or recognized by the computer as code.

Here's a good example of commenting:

```
print("Hello World!") #This prints hello world
```

The output of this is:
> Hello World!

You will see this often in the sample outline provided for the game. It is designed to help you understand how the code is working and to be able to edit and write your own code.

## General Formatting
There are certain tools we can use to make our end result look a little more clean.

For example, adding spaces between lines.

This text looks a little crowded, so let's add a line of blank space in between to make it look better.

```
You have been defeated mere mortal.
You died.
```

```
print("You have been defeated mere mortal.")
print()
print("You died.")
```
I added an extra print statement in between the two, which creates an extra line. Every new print statement prints on the next line down. The result of this code is:

```
You have been defeated mere mortal.

You died.
```
Also, when using ASCII text for stylistic purposes, we must use 3 double quotes and a backslash so that the text will display properly.

Here's what that looks like:
```
print("""\Hello World!""")
```

# If-Else Statements
If-else statements are a way for a computer to make a decision. The computer thinks like this:

If X happens, then I do A.
If Y happens, then I do B.
If neither happens, then I do C.

This is translated into code like this:

```
if x > y:
    print("Hello")

elif x > z:
    print("World")

else:
    print("None")
```
> [!IMPORTANT]
> All the if statements end with a colon :. Make sure you include that when writing, otherwise the code won't work.

Here, the code is comparing values. It goes through the conditions step by step, and if the condition is true, it performs the action in that section.

For example, if x is bigger than y, it will print:
>Hello

If x is not bigger than y, it will go to the next one and ask if x is bigger than z. If it is, then it will print:
>World

If it goes through the first 2 and neither are true, it will go to the very last one and print:
>None

>[!NOTE]
>If you are saying that a variable is equal to something else, then you must have two equal signs.
```
if attack == 1:
    ...
```

You can make the chain of if-else statements as long as you want, but most of the time you won't need that many.

> [!IMPORTANT]
> Make sure to indent when you do your if statements, otherwise the computer will just think it's another line of code and not inside the if statement.


## Nesting
You can also have if-else statements inside of other if-else statements. For example:

```
if (x > y):
    print("Hello")

    if (z > y):
        print("World")

    else:
        print ("None")

else:
    print("Nothing")
```
It will still go through the conditions one by one. If the first if statement is true, it will go inside and move to the next if statement.

For example, if x is bigger than y, then it will print:
>Hello

From there, if z is bigger than y, it will print:
>World

If z isn't bigger than y, it will print:
>None

It would just end from there.

The final result would be:

```
Hello
World
None
```

# Variables
Variables are a way to make our lives a little bit easier. Rather than having to remember the value ourselves and write it over and over, we can name a variable to keep it for us.

For example:
```
health = 100
```
We now have a variable called health that we can do lots of stuff with. For example, we can do some math with it and the variable will automatically update.

```
health = 100
health = health - 20
print(health)
```

The output of this is:
> 80

>[!IMPORTANT]
> When you print variables, don't put them in quotes, just write the name of the variable.

## Combining Variables and Strings
Now you might want to print a sentence like:
```
You have 20 health left.
```
Now rather than doing the math yourself and manually typing out the amount of health you have, we can use the variable when we print.

```
print("You have", health, "left.")

```
The comma is like a plus sign between the two strings. It allows us to combine variables and print them alongside strings.

This way, no matter what the value of the health is, it will always print the right value because we used a variable instead of manually writing out the health.

## User Input
Sometimes we want the user to give us information to store, like their name. For that, we can assign a variable to an input statement. Whatever we write in the input statement will be displayed and whatever the user types in will be stored in the variable. 

Here's how that looks in code:

```
name = input("What is yoour name: ")
```
When run, it will display this:
> What is your name:

and then I can type in my name:
>What is your name: May

and then if we print the variable "name", we get this:
>May

A standard input statement always takes the input as a string. If the user inputs a number into that statement, it will save the number as a string, so we can't really do any math with it.

If we want to be able to do math with a variable, similar to health, then we need to specify that the input as a number/integer.

Here's what that looks like in code:
```
num = int(input("Please enter a number: "))
```
The "int" specifies that the input will be an integer/number. This way, we can do math with the variable.

>[!NOTE]
> There are also other types of variables/data types that we can specify besides the integer. However, they aren't nessesary for this project so they aren't covered. Just know that they exist.

# Loops
Loops help us do the same task over and over again without having to run the program ourselves over and over again.

There are many kinds of loops, but this course will focus on while loops.

While loops work like this:

>While x is true, do this.

This helps us in a number of scenarios, but for the game we could make a condition for a loop something like this:

>While the user is alive and the enemy is alive, do this.

What determines if the enemy and user are alive? The health variable! So we say as long as the health of both people is bigger than 0, keep doing the loop.

Here's what that looks like in code:
```
while user_health > 0 and enemy_health > 0:
    ...
```
Loops work the same as if-else statements. They will perform whatever task is inside the loop (indented) as long as the condition is true.

> [!IMPORTANT]
> You don't have to have only 2 conditions. You can have any number of condiitons. If you want more than 1 condiiton, use "and" to join them together.



