#Step 4
import random
# from replit import clear
logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |                         # hang man
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)

def game():
  word_list = ["apple" , "banana" , "mango" ,"pineapple" , "watermelon" ]
  chosen_word = random.choice(word_list)
  word_length = len(chosen_word)
  #print(f'Pssst, the solution is {chosen_word}.')

  display = []
  for _ in range(word_length):
      display.append("_")


  end_of_game = False
  lives = 7
  print("  ")
  print(f"its a {len(display)} letter word fruit and its starts with {chosen_word[0]}\n")
  while not end_of_game:
      guess = input("Guess a letter: \n").lower()
      # clear()
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
      if guess not in chosen_word:
          lives -= 1
          if lives == 0:
              print(stages[0])
              end_of_game = True
              print("You lose.")
              print(f"the correct word is {chosen_word}")
              play_again = input("do you want to play again ? y / n ")
              if play_again == "y":
                game()      # ikkada recurtion undi
              else:
                return

          print(stages[lives])
      print(f"{' '.join(display)}")
      if "_" not in display:
          end_of_game = True
          print("You win.")
          play_again = input("do you want to play again ? y / n \n ")
          if play_again == "y":
            game()   # ikkada recurtion undi
          else:
            return
game()
