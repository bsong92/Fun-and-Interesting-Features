import string
import time
import random


def print_pause(message, delay=1):
    time.sleep(delay)
    print(message)


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here, "
                "and has been terrifying the nearby village")


def destination():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    while True:
        choice = input("Please enter 1 or 2.\n")
        if choice == '1':
            house()
            break
        elif choice == '2':
            cave()
            break
        else:
            print("You must type either 1 or 2.")


def house():
    print_pause("You open the door and find the trace of an enemy.")
    print_pause(f"Then steps out a {enemy}, which you have to face")
    print_pause(f"You opened the {enemy}'s house.")
    combat(weapon)


def cave():
    global weapon
    global visit
    print_pause("You look in to the cave and see no trace of an enemy.")
    if visit is False:
        print_pause("However you see a shining sword and pick it up.")
        print_pause(f"You switch your {weapon} with the 'Magical Sword'.")
        weapon = 'Magical Sword'
    elif visit is True:
        print_pause("You've been here before and it is empty.")
    visit = True
    print_pause("You return to the field to make the next decision.")
    destination()


def combat(weapon):
    print_pause(f"You can two options - 1. Fight with {enemy}. 2. Run away!")
    while True:
        decision = input("Choose 1 or 2.\n")
        if decision == '1':
            if weapon in starting_weapons:
                print_pause("You try hard...")
                print_pause(f"But with your {weapon}, it's a no start and "
                            "you lose.")
                print_pause("You lost!")
                print_pause("Game Over!")
                reset()
            elif weapon == 'Magical Sword':
                print_pause(f"The {enemy} moves to attack, you take out "
                            "your new sword.")
                print_pause(f"You blow a total {damage} to the enemy.")
                print_pause(f"The {enemy} is hurt and scared and runs away!")
                print_pause(f"You have rid the town of the {enemy}. "
                            "You are victorious!")
                reset()
        elif decision == '2':
            print_pause("You run away back to the field!")
            destination()
        else:
            print("You must type either 1 or 2.")


def reset():
    while True:
        choice = input("Play one more time? (y/n)").lower()
        if choice == "y":
            print_pause("Okay. I'm restarting.")
            weapon = random.choice(starting_weapons)
            game()
        elif choice == "n":
            print_pause("Thanks for playing. See you next time.")
            exit()
        else:
            print("Invalid input. Please type (y/n).")


def game():
    global enemy
    global weapon
    global starting_weapons
    global damage
    global visit
    enemies = ['pirate', 'ogre', 'troll', 'flying monster']
    starting_weapons = ['dagger', 'arrow', 'wand']
    damage = random.randint(0, 100)
    enemy = random.choice(enemies)
    weapon = random.choice(starting_weapons)
    visit = False

    intro()
    destination()
    reset()


game()
