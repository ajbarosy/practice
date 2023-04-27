import random

# def get_choices(): #function
#   player_choice = input('Enter a choice (rock, paper, scissors): ') #variable
#   options = ['rock', 'paper', 'scissors'] #list
#   computer_choice = random.choice(options)
#   choices = {"player": player_choice, "computer": computer_choice} #dictionary
  
#   return choices

# def check_win(player, computer):
#   print(f"You chose {player}, Computer chose {computer}")
#   if player == computer:
#     return 'It/s a tie'
  
#   elif player == 'rock':
#     if computer == 'scissors':
#       return 'Rock beats scissors, you win!'
#     else: return 'Paper covers rock, you lose'
 
#   elif player == 'paper':
#     if computer == 'rock':
#       return 'Paper covers rock, you win!'
#     else: return 'Scissors cuts paper, you lose'
  
#   elif player == 'scissors':
#     if computer == 'paper':
#       return 'Scissors cuts paper, you win!'
#     else: return 'Rock beats scissors, you lose'

# choices = get_choices()
# result = check_win(choices['player'], choices['computer'])
# print(result)


#PRACTICE

def player_choices():
    player_one = input('Enter a choice: (rock, paper, scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_one = random.choice(options)
    choices = {'player': player_one, 'computer': computer_one}

    return(choices)

def victor(player, computer):
    print(f'You chose {player} and Computer chose {computer}')

    if player == computer:
        return {"It's a tie :/"}
    
    elif player == 'rock':
        if  computer == 'paper':
            return('Paper covers rock, you lose :(')
        else: return('Rock smashes scissors, you win :)')

    elif player == 'paper':
        if  computer == 'scissors':
            return('Paper covers rock, you win :)')
        else: return('Scissors cut paper, you lose :(')

    elif player == 'scissors':
        if  computer == 'rock':
            return('Rock smashes scissors, you lose :(')
        else: return('Scissors cut paper, you win :)')

options = player_choices()
results = victor(options['player'], options['computer'])
print(results)