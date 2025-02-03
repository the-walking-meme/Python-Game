import math

print("""\
██████╗ ██╗      ██████╗ ██╗    ██╗    ███████╗ ██████╗ ██████╗     ██████╗ ██╗      ██████╗ ██╗    ██╗
██╔══██╗██║     ██╔═══██╗██║    ██║    ██╔════╝██╔═══██╗██╔══██╗    ██╔══██╗██║     ██╔═══██╗██║    ██║
██████╔╝██║     ██║   ██║██║ █╗ ██║    █████╗  ██║   ██║██████╔╝    ██████╔╝██║     ██║   ██║██║ █╗ ██║
██╔══██╗██║     ██║   ██║██║███╗██║    ██╔══╝  ██║   ██║██╔══██╗    ██╔══██╗██║     ██║   ██║██║███╗██║
██████╔╝███████╗╚██████╔╝╚███╔███╔╝    ██║     ╚██████╔╝██║  ██║    ██████╔╝███████╗╚██████╔╝╚███╔███╔╝
╚═════╝ ╚══════╝ ╚═════╝  ╚══╝╚══╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚══╝╚══╝ 
                                                                                                       """)

#VARIABLES
health = 100
enemy_health = 100
attack1 = 20
attack2 = 30
attack3 = 50
e_attack = 30
surrender = "n"

print()
user_name = input("WHAT IS YOUR NAME WARRIOR?: ")
print()
print("WONDERFUL! LET US BEGIN ON OUR ADVENTURE!!!")
print()

#START
print("YOU HAVE ENCOUNTERED AN ENEMY!!!!")
print()
print("""\
██████╗ ██████╗ ███████╗ █████╗ ██████╗  ██████╗██╗      █████╗ ██╗    ██╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║     ██╔══██╗██║    ██║
██║  ██║██████╔╝█████╗  ███████║██║  ██║██║     ██║     ███████║██║ █╗ ██║
██║  ██║██╔══██╗██╔══╝  ██╔══██║██║  ██║██║     ██║     ██╔══██║██║███╗██║
██████╔╝██║  ██║███████╗██║  ██║██████╔╝╚██████╗███████╗██║  ██║╚███╔███╔╝
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ 
                                                                          
""")
print()
print("FIGHT!")
print()

#ATTACK SEQUENCE
while surrender == "n":

    print("""\
.:;S;:/           .:;.;:. 
S     S           S  S  S 
`:;S;:'           `:;S;:' 
                          
""")

    #list of attacks for user input
    print()
    print("1. Shadow Strike")
    print("2. Blazing Vortex")
    print("3. Phantom Dagger")
    print()
    attack = int(input("Which attack do you choose: "))
    print()

    #if-else statements for each attack
    if attack == 1:
        enemy_health = enemy_health - attack1
        print(user_name, "did 20 damage!")
        print()

    elif attack == 2:
        enemy_health = enemy_health - attack1
        print(user_name, "did 30 damage!")
        print()

    else:
        enemy_health = enemy_health - attack1
        print(user_name, "did 50 damage!")
        print()

    #display how much health the enemy has
    print("The enemy has ", enemy_health, "left!")
    print()

    #if the enemy and the user are both alive
    if enemy_health > 0 and health > 0:

        #enemy attack phase
        print("DREADCLAW ATTACKED!!!")
        print()

        health = health - e_attack

        #display user health
        print("You have ", health, "left!")
        print()

        #if the user died
        if health <= 0:
            break;

        else:
            #ask if they want to surrender
            surrender = input("Do you want to surrender (y/n): ")
            print()

    else:
        break;

#ending message
if surrender == "y":
    print("""\
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
""")
    print("You have surrendered. The enemy has won.")

elif health <= 0:
    print("""\
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝
""")
    print("You Died. The enemy has won.")

else:
    print("""\
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
""")
    print("Congratulations!! The enemy was defeated!")


