import time
import random

wepons = []


def intro(story):
    print(story)
    time.sleep(2)


def ask2():
    ask2 = input("Would you like to (1) fight or (2) run away?\n")

    if ask2 == '1':
        intro('As the troll moves to attack, you unsheath your new sword')
        intro("The sword of Orogoth shines brightly in your hand\
as you brace yourself for the attack")
        intro('But the troll takes one lookat your\
shiny new toy and runs away!')
        intro('You have rid the town of the troll. You are victorious!')
        again()
    else:
        intro("You ran back into the field. \
Luckily, you don't seem to have been followed\n")
        option()


def ask():
    ask1 = input("Would you like to (1) fight or (2) run away?\n")

    if ask1 == '1':
        intro("You do you best...")
        intro("but your dagger is no match for the troll")
        intro("you have been defeated!")
        again()
    else:
        intro("You run back into the field.\
Luckily, you don't seem to have been followed.\n")
        option()


def house():
    if 'Ogoroth_sword' in wepons:
        intro("You approach the door of the house")
        intro("You are about to knock when the\
door opens and out step a troll's")
        intro("Eep! This is the troll's house!")
        intro("The troll's attacks you!")
        ask2()

    else:
        intro("You approach the door of the house")
        intro("You are about to knock when the door\
opens and out step a troll's")
        intro("Eep! This is the troll's house!")
        intro("The troll's attacks you!")
        ask()


def cave():
    if 'Ogoroth_sword' not in wepons:
        intro("You peer cautiously into the cave")
        intro("It turns out to be only a very small cave")
        intro("Your eye catches a glint of metal behind a rock")
        intro("You have found the magical Sword of the Ogoroth")
        intro("You discard your silly old dagger and take the sword with you")
        intro("You walk back out to the field\n")
        wepons.append("Ogoroth_sword")
        option()
    else:
        intro("You peer cautiously into the cave")
        intro("You've been here before, and gotten all the good stuff")
        intro("You walk back out to the field")
        option()


def tale():
    intro("You find yourself standing in an open field, \
filled with grass and, yellow wildflowers.")
    intro("Rumor has it that a wicked fairie is somewhere\
around here, and has been terrifying the nearby village.",)
    intro("In front of you is a house.")
    intro("To your right is a dark cave.")
    intro("In your hand you hold your trusty (but not very effective) dagger.")


def again():
    ask2 = input('Would you like to play again? (y/n)')
    if 'y' == ask2:
        intro("Excellent! Restarting the game ...")
        tale()
        option()
    else:
        intro('Thanks for playing! See younext time.')


def option():
    intro("Enter 1 to knock on the door of the house")
    intro("Enter 2 to peer into the cave")
    intro("What would you like to do?")
    choice = input("Please enter 1 or 2 \n")
    if choice == '1':
        house()
    elif choice == '2':
        cave()


tale()
option()
