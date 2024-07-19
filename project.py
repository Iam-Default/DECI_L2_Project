import time
import random

def print_pause(message, pause=1):
    print(message)
    time.sleep(pause)

def intro():
    print_pause("You are an astronaut aboard the International Space Station (ISS).")
    print_pause("Suddenly, the alarms go off and you realize the ISS is being hacked.")
    print_pause("You must act quickly to regain control before it crashes into Earth.")
    print_pause("You will earn points for making progress and solving challenges.")

def generate_password():
    passwords = ["orbit", "galaxy", "cosmos", "astronaut", "gravity"]
    return random.choice(passwords)

def main_hallway():
    global score
    print_pause("\nYou are in the main hallway of the ISS.")
    print_pause("You see a computer terminal and a toolbox.")
    choice = input("Do you want to check the (computer) terminal or the (toolbox)? ").lower()
    if choice == 'computer':
        score += 10
        computer_terminal()
    elif choice == 'toolbox':
        score += 5
        toolbox()
    else:
        print_pause("Invalid choice, try again.")
        main_hallway()

def computer_terminal():
    global password, score
    print_pause("\nYou approach the computer terminal.")
    print_pause("The screen displays a message: 'Unauthorized access detected. System lockdown in progress.'")
    choice = input("Do you want to try to (hack) the system or (call) for help? ").lower()
    if choice == 'hack':
        score += 10
        hack_system()
    elif choice == 'call':
        score += 5
        call_for_help()
    else:
        print_pause("Invalid choice, try again.")
        computer_terminal()

def toolbox():
    global score
    global multitool
    print_pause("\nYou open the toolbox and find various tools.")
    print_pause("You find a multitool, and a piece of paper that that says: The Password is " + password)
    choice = input("Do you want to take the multitool?(yes)/(no) ").lower()
    if choice == 'no':
        score += 0
        print_pause("You head back to the main hallway.")
        main_hallway()
    elif choice == 'yes':
        score += 20
        print_pause("You take the multitool and head back to the main hallway.")
        multitool = True
        main_hallway()
    else:
        print_pause("Invalid choice, try again.")
        toolbox()

def hack_system():
    global password, score
    print_pause("\nYou attempt to hack the system.")
    print_pause("You need to enter a password to proceed.")
    user_password = input("Enter the password: ")
    if user_password == password:
        score += 20
        print_pause("Access granted! You successfully regain control of the system.")
        print_pause("The ISS is safe, and you have averted the disaster.")
        print_pause(f"Your final score is: {score}")
        play_again()
    else:
        print_pause("Access denied. The system remains locked.")
        main_hallway()

def call_for_help():
    global score
    print_pause("\nYou try to call for help.")
    print_pause("You reach Mission Control and explain the situation.")
    print_pause("Mission Control instructs you to find the manual override in the control room.")
    score += 5
    control_room()

def control_room():
    global score
    print_pause("\nYou head to the control room.")
    print_pause("You see the manual override lever and a panel with wires.")
    choice = input("Do you want to pull the (lever) or fix the (panel)? ").lower()
    if choice == 'lever':
        score += 5
        pull_lever()
    elif choice == 'panel':
        score += 15
        fix_panel()
    else:
        print_pause("Invalid choice, try again.")
        control_room()

def pull_lever():
    global score
    print_pause("\nYou pull the manual override lever.")
    print_pause("The system reboots and you lose control of the ISS.")
    print_pause("The ISS falls to earth and you die.")
    score -= 20
    print_pause(f"Your final score is: {score}")
    play_again()

def fix_panel():
    global score
    global multitool
    print_pause("\nYou open the panel and see a tangle of wires.")
    print_pause("You need to reconnect the wires correctly to regain control.")
    if multitool == True:
        print_pause("Using the multitool, you carefully reconnect the wires.")
        print_pause("The system reboots and you regain control of the ISS.")
        print_pause("The ISS is safe, and you have averted the disaster.")
        print_pause(f"Your final score is: {score}")
        play_again()
    else:
        print_pause("The wires are too complex to understand on you own.")
        print_pause("You will need a multitool to fix it.(Hint: You can find one in the toolbox)")
        main_hallway()
        
def play_again():
    choice = input("Do you want to play again? (yes/no) ").lower()
    if choice == 'yes':
        main()
    else:
        print_pause("Thank you for playing! Goodbye.")
        exit()

def main():
    global score, password, multitool
    score = 0
    password = generate_password()
    multitool = False
    intro()
    main_hallway()

if __name__ == "__main__":
    main()
