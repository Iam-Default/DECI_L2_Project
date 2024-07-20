import time
import random

# Function to print a message with a 1-second pause
def print_pause(message):
    print(message)
    time.sleep(1)

# Function to print the player's current score
def print_score(score):
    print("Your current score is:", score)

# Function to validate user input against a list of options
def valid_input(prompt, options):
    choice = input(prompt).lower()
    while choice not in options:
        print_pause("Invalid choice. Please try again.")
        choice = input(prompt).lower()
    return choice

# Function to print the introduction and game setup
def intro():
    print_pause("You are an astronaut aboard the International Space Station (ISS).")
    print_pause("Suddenly, the alarms go off and you realize the ISS is being hacked.")
    print_pause("You must act quickly to regain control before it crashes into Earth.")
    print_pause("You will earn points for making progress and solving challenges.")

# Function to generate a random password from a list
def generate_password():
    passwords = ["orbit", "galaxy", "cosmos", "astronaut", "gravity"]
    return random.choice(passwords)

# Function for the main hallway scene
def main_hallway():
    global score
    print_score(score)
    print_pause("\nYou are in the main hallway of the ISS.")
    print_pause("You see a computer terminal and a toolbox.")
    choice = valid_input("Do you want to check the (computer) terminal or the (toolbox)? ", ["computer", "toolbox"])
    if choice == 'computer':
        score += 10
        computer_terminal()
    else:
        score += 5
        toolbox()

# Function for the computer terminal scene
def computer_terminal():
    global password, score
    print_pause("\nYou approach the computer terminal.")
    print_pause("The screen displays a message: 'Unauthorized access detected. System lockdown in progress.'")
    choice = valid_input("Do you want to try to (hack) the system or (call) for help? ", ["hack", "call"])
    if choice == 'hack':
        score += 10
        hack_system()
    else:
        score += 5
        call_for_help()

# Function for the toolbox scene
def toolbox():
    global score
    global multitool
    print_score(score)
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

# Function to handle hacking the system
def hack_system():
    global password, score
    print_score(score)
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

# Function to handle calling for help
def call_for_help():
    global score
    print_score(score)
    print_pause("\nYou try to call for help.")
    print_pause("You reach Mission Control and explain the situation.")
    print_pause("Mission Control instructs you to find the manual override in the control room.")
    score += 5
    control_room()

# Function for the control room scene
def control_room():
    global score
    print_pause("\nYou head to the control room.")
    print_pause("You see the manual override lever and a panel with wires.")
    choice = valid_input("Do you want to pull the (lever) or fix the (panel)? ", ["lever", "panel"])
    if choice == 'lever':
        score += 15
        pull_lever()
    else:
        score += 15
        fix_panel()

# Function to handle pulling the lever
def pull_lever():
    global score
    print_score(score)
    print_pause("\nYou pull the manual override lever.")
    print_pause("The system reboots and you lose control of the ISS.")
    print_pause("The ISS falls to earth and you die.")
    score -= 20
    print_pause(f"Your final score is: {score}")
    play_again()

# Function to handle fixing the panel
def fix_panel():
    global score
    global multitool
    print_score(score)
    print_pause("\nYou open the panel and see a tangle of wires.")
    print_pause("You need to reconnect the wires correctly to regain control.")
    if multitool:
        print_pause("Using the multitool, you carefully reconnect the wires.")
        print_pause("The system reboots and you regain control of the ISS.")
        print_pause("The ISS is safe, and you have averted the disaster.")
        print_pause(f"Your final score is: {score}")
        play_again()
    else:
        print_pause("The wires are too complex to understand on your own.")
        print_pause("You will need a multitool to fix it.(Hint: You can find one in the toolbox)")
        main_hallway()
        
# Function to ask the player if they want to play again
def play_again():
    choice = input("Do you want to play again? (yes/no) ").lower()
    if choice == 'yes':
        main()
    else:
        print_pause("Thank you for playing! Goodbye.")
        exit()

# Main function to start the game
def main():
    global score, password, multitool
    score = 0
    password = generate_password()
    multitool = False
    intro()
    main_hallway()

# Start the game
if __name__ == "__main__":
    main()
