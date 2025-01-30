import math

print("""\Title""")

#VARIABLES
health = 100
enemy_health = 100
attack1 = 20
attack2 = 30
attack3 = 50
e_attack = 30
surrender = "n"

user_name = input("What is your name: ")


#START
print("YOU HAVE ENCOUNTERED AN ENEMY!!!!")

#ATTACK SEQUENCE
while surrender == "n":

    print("""\hero and enemy visual""")

    #list of attacks for user input
    print("attack 1")
    print("attack 2")
    print("attack 3")
    attack = int(input("Which attack do you choose: "))

    #if-else statements for each attack
    if attack == 1:
        enemy_health = enemy_health - attack1
        print(user_name, "did 20 damage!")

    elif attack == 2:
        enemy_health = enemy_health - attack1
        print(user_name, "did 30 damage!")

    else:
        enemy_health = enemy_health - attack1
        print(user_name, "did 50 damage!")

    #display how much health the enemy has
    print("The enemy has ", enemy_health, "left!")

    #if the enemy and the user are both alive
    if enemy_health > 0 and health > 0:

        #enemy attack phase
        print("The enemy attacked!!!")

        health = health - e_attack

        #display user health
        print("You have ", health, "left!")

        #if the user died
        if health <= 0:
            break;

        else:
            #ask if they want to surrender
            surrender = input("Do you want to surrender (y/n): ")

    else:
        break;

#ending message
if surrender == "y":
    print("You have surrendered. The enemy has won.")

elif health <= 0:
    print("You Died. The enemy has won.")

else:
    print("Congratulations!! The enemy was defeated!")


