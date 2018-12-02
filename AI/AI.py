#Welcome to Tanner's first AI Game!
import time
import random
import os
import sys
clear = lambda: os.system('cls')
#Start of Program

'''Ideas:
Rock paper scissors
Hangman'''

def player():
    player_choice = input('Rock, Paper, or Scissors (R,P,or S):')
    player_choice = player_choice.lower()
    if player_choice.startswith('r'):
        oRock = open("rock.txt", "r")
        rock = oRock.read()
        oRock.close()
        new_rock = int(rock) + 1
        oRock = open("rock.txt", "w")
        oRock.write(str(new_rock))
        oRock.close()
        player_choice = 'Rock'
    elif player_choice.startswith('p'):
        oPaper = open("paper.txt", "r")
        paper = oPaper.read()
        oPaper.close()
        new_paper = int(paper) + 1
        oPaper = open("paper.txt", "w")
        oPaper.write(str(new_paper))
        oPaper.close()
        player_choice = 'Paper'
    elif player_choice.startswith('s'):
        oScissors = open("scissors.txt", "r")
        scissors = oScissors.read()
        oScissors.close()
        new_scissors = int(scissors) + 1
        oScissors = open("scissors.txt", "w")
        oScissors.write(str(new_scissors))
        oScissors.close()
        player_choice = 'Scissors'
    else:
        print('Invalid Input!')
        player()
    return player_choice
def ai():
    options = ('Rock', 'Paper', 'Scissors')
    aiRock = open("rock.txt", "r")
    rock_val = int(aiRock.read())
    aiRock.close()
    aiPaper = open("paper.txt", "r")
    paper_val = int(aiPaper.read())
    aiPaper.close()
    aiScissors = open("scissors.txt", "r")
    scissors_val = int(aiScissors.read())
    aiScissors.close()
    values = (rock_val, paper_val, scissors_val)
    if max(values) == rock_val:
        greatest_value = 'Rock'
    elif max(values) == paper_val:
        greatest_value = 'Paper'
    elif max(values) == scissors_val:
        greatest_value = 'Scissors'
    else:
        random_choices = ('Rock', 'Paper', 'Scissors')
        randomChoice = random.choice(random_choices)
    if greatest_value == 'Rock':
        winning_value = 'Paper'
    elif greatest_value == 'Paper':
        winning_value = 'Scissors'
    elif greatest_value == 'Scissors':
        winning_value = 'Rock'
    else:
        winning_value = randomChoice
    return winning_value

def game_loop():
    player_choice = player()
    winning_value = ai()
    if player_choice == 'Rock' and winning_value == 'Paper':
        winner = 'Computer'
    elif player_choice == 'Rock' and winning_value == 'Scissors':
        winner = 'Player'
    elif player_choice == 'Rock' and winning_value == 'Rock':
        winner = 'Tie'
    elif player_choice == 'Paper' and winning_value == 'Scissors':
        winner = 'Computer'
    elif player_choice == 'Paper' and winning_value == 'Rock':
        winner = 'Player'
    elif player_choice == 'Paper' and winning_value == 'Paper':
        winner = 'Tie'
    elif player_choice == 'Scissors' and winning_value == 'Rock':
        winner = 'Computer'
    elif player_choice == 'Scissors' and winning_value == 'Paper':
        winner = 'Player'
    elif player_choice == 'Scissors' and winning_value == 'Scissors':
        winner = 'Tie'
  
    try:
        print('The winner is ' + winner + '.')
    except UnboundLocalError:
        print('Sorry, you have crashed the game!')
        time.sleep(2)
        sys.exit()
    print('The player chose ' + player_choice + ' and the computer chose ' + winning_value + '.')
    again = input('Play again y/n?')
    again = again.lower()
    if again.startswith('y'):
        game_loop()
    else:
        sys.exit()

game_loop()