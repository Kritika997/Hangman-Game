import string
from words import choose_word
from images import IMAGES
# print(IMAGES[0])
def get_hint(secret_word, letters_guessed):
  import random
  letters_not_guessed = []
  index = 0
  while (index < len(secret_word)):
      letter = secret_word[index]
      if letter not in letters_guessed:
          if letter not in letters_not_guessed:
              letters_not_guessed.append(letter)
      index += 1
  return random.choice(letters_not_guessed) 
def is_word_guessed(secret_word, letters_guessed):
    
    if secret_word==get_guessed_word(secret_word, letters_guessed):
      return True
    return False

def get_guessed_word(secret_word, letters_guessed):
   
    i = 0
    guessed_word = " "
    while i<len(secret_word):
        if secret_word[i] in letters_guessed:
          guessed_word = guessed_word+ secret_word[i]
        else:
            guessed_word = guessed_word+ "_"
        i += 1
    
    return guessed_word

def get_available_letters(letters_guessed):
    
    import string
    letters_left = ""
    all_letters = string.ascii_lowercase 
    for letter in all_letters:
      if letter not in letters_guessed:
        letters_left = letters_left+letter
    return letters_left
def ifValid(guess):
    if len(guess) != 1:
        return False

    if not guess.isalpha():
        return False

    return True 


def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    print(secret_word)
    difficulty_level = input("Enter your level on which level you want to play:\n1.Easy\n2.Medium\n3.Hard\n").lower()
    if difficulty_level == "easy":
      lives = 8
      images= [0,1,2,3,4,5,6,7]
    elif difficulty_level == "medium":
      lives = 6
      images=[0,2,4,5,6,7]
    elif difficulty_level == "hard":
      lives = 4
      images=[0,2,5,7]
    else:
      print("you didn't chose any level so you will play easy only")
      lives = 8
    i = 0
    letters_guessed = []
    letters_not_guessed = []
    remaining_lives = lives
    i = 0
    while remaining_lives>=1:
      user = input("do you want hint or not Yes/No: ").lower()
      if user == "yes":
        letters_not_guessed = get_hint(secret_word, letters_guessed)
        print(letters_not_guessed)
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)
        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if (not ifValid(letter)):
            continue
        if letter in secret_word:
          letters_guessed.append(letter)
          print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          print ("")
          if is_word_guessed(secret_word, letters_guessed) == True:
            print (" * * Congratulations, you won! * * ")
            print ("")
            break
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            pic = images[i]
            print (IMAGES[pic])
            remaining_lives = remaining_lives-1
            print("you Have only",remaining_lives,"Lives")
            i = i+1
      else:
        if user == "no":
          available_letters = get_available_letters(letters_guessed)
          print ("Available letters: " + available_letters)
          print(letters_guessed)
          guess = input("Please guess a letter: ")
          letter = guess.lower()
          if (not ifValid(letter)):
            continue
          if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")
            if is_word_guessed(secret_word, letters_guessed) == True:
              print (" * * Congratulations, you won! * * ")
              print ("")
              break
          else:
              print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
              letters_guessed.append(letter)
              # images = 8-remaining_lives
              pic = images[i]
              print (IMAGES[pic])
              print ("")  
              remaining_lives = remaining_lives-1
              print("you Have only",remaining_lives,"Lives")
              i = i + 1
        else:
          print("user input is not valid")  
    else:
        print ("Sorry, you ran out of guesses. The word was " + str(secret_word) + ".")
secret_word = choose_word()
hangman(secret_word)
