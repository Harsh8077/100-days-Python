#Random Word Game

from random_word import RandomWords
r = RandomWords()

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
  O   |
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

end_of_game = False
chosen_word = r.get_random_word()
word_length = len(chosen_word)


lives = 6


display = []
for _ in range(word_length):
    display += "_"
print("Here are the empty spaces now try to guess the word, you have only 6 lives.")
print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()


    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
      lives=lives-1
      print(stages[lives])
    if lives == 0:
      print("You lose!")
      print("The Word is:"+ chosen_word)

    print(f"{' '.join(display)}")
  
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print("The Word is:"+ chosen_word)
