import random

def play_game():
    user_input = input("What's your choice? 'rock', 'scissors', or 'paper': ").strip().lower()
    print("Your input:", user_input)  # Debugging statement
    
    if user_input not in ['rock', 'scissors', 'paper']:
        return 'Invalid input. You must enter "rock", "scissors", or "paper".'

    computer_choice = random.choice(['rock', 'scissors', 'paper'])
    print("Computer's choice:", computer_choice)  # Debugging statement

    if user_input == computer_choice:
        return 'It is a tie!'
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'paper' and computer_choice == 'rock') or \
         (user_input == 'scissors' and computer_choice == 'paper'):
        return 'YOU WON!'
    else:
        return 'YOU LOST!'

result = play_game()
print(result)
