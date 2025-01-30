# Game Extras
This is for those of you who have complete the basics and want to make your game a little fancier/more complex!

Here's what we will cover:
- random attacks/random damage
- misses and critical hits
- enemy difficulties

# Random Attacks & Random Damage
To have a random output, we need to use a random number generator. First, we are going to import the random module.

```
import random
```
Next, we can use the randint function to generate a random number. The function takes 2 arguements, which is two numbers that determine the range we want to generate in.
>[!NOTE]
> The range is an inclusive range, which means the endpoints that we specify can also be included in the numbers that can be generated.

We can also assign this new number to a variable.
```
e_attack = random.randint(1,3)
```
With this, you can have the enemy perform random attacks based on what random number is generated. Even you as the builder will never know what attack is coming next

The same can be adapted for damage inflicted. You can just edit the range that the numbers are generated in.

# Misses and Critical Hits
We can also include chances of misses and critical hits. We will still use the random module and randint generator. You can use a range of 1-2 to determine if a hit is a miss/critical hit, and edit the damage accordingly.

For example, if a critical hit is 2x the damage, some code might look like this:

```
damage = 20
crit = random.randint(1,2)

if crit == 1:
    hero_health = hero_health - (damage * 2)
```
In this case, if you get the crit, the damage is 40 instead of 20.

Similarly, you can have misses by applying the same concept. Try it for yourself before using this guide.

The code might look like this:
```
miss = random.randint(1,2)

if miss == 1:
    print("Uh Oh! You Missed!")
```

# Enemy Difficulties
How about addint some difficulties for the enemies you face? We can do this using some pretty big if-else statements.

At the start, we can have the user choose a difficulty. Based on that, we can have a giant if-else statement that includes the entire code for that difficulty battle.

```
diff = int(input("Please choose difficulty(1,2,3): ))

if diff == 1:
    ...#this would be all code for the entire battle
...
```

## Functions
The if-else statements are functional, but a little messy. We can make it neater by using functions. Functions are tiny pieces of code that we can call to run certain tasks. They only run when we call them, not as a part of the main code.

Functions are usually found at the very end of your code, outside of everything else.

First, we would need to create a function. In the same file as your game code, create a function:
```
def diff_easy():
    ...
```
Now our function is created. Inside this, we can define our variables, create the entire battle sequence for this difficulty specifically.

For example, in the easy difficulty your enemy might have 100 health, but in the hard difficulty it has 200 health. Here's how that might look:
```
def diff_easy():
    e_health = 100
    ...

def diff_hard():
    e_health = 200
    ...
```
Now how do we put these functions into practice? Well we have to call them in our main code, using some if-else statements. Here's how we call a function:
```
diff_easy()
```
When the computer sees that, it will automatically jump to the function of the same name and run the code inside it.

Try calling each difficulty function using if else statements, then come back and check your work.

Here's how the code would look like:
```
diff = int(input("Please choose a difficulty(1/2): ))

if diff == 1:
    diff_easy()

else:
    diff_hard()
```
All the functions would be written right after this code. You can add functions for any task, this is just one example.

>[!IMPORTANT]
>These functions take arguements, which are listed in the brackets. 
>If there is a value in the main code that you want to use in the function, you have to include it in the brackets when you call it and when you create the function.
```
health = 100

diff = int(input("Please choose a difficulty(1/2): ))

if diff == 1:
    diff_easy(health)

else:
    diff_hard(health)

def diff_easy(health):
    e_health = 100
    ...

def diff_hard(health):
    e_health = 200
    ...
```