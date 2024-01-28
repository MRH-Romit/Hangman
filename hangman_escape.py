import random
import os
from hangman_words import word_list
from hangman_art import logo,stages


chosen_word = random.choice(word_list)
lives=6
split=list(chosen_word)
word_length=len(chosen_word)
new_word=[]
new_word = ["_" for _ in chosen_word]
game_ender=False

print(logo)

while not game_ender and lives > 0:
   
    guess = input("Guess a letter: ").lower()

    correct_guess = False
    for position in range(word_length):
        letter = split[position]
        if letter == guess:
            new_word[position] = letter
            correct_guess = True
    os.system('cls' if os.name == 'nt' else 'clear')
    if not correct_guess:
        lives -= 1
        print(f"Incorrect guess! Lives remaining: {lives}")
        
    if guess in new_word:
        print("you've guess that letter already!!")

    print("Current progress:"+ " ".join(new_word))

    if "_" not in new_word:
        game_ender = True
        print("Congratulations! You guessed the word:"+chosen_word)

    if lives == 0:
        game_ender = True
        print("Sorry, you're out of lives. You lose!")
    print(stages[lives])
print("He died because of you.He shouldn't have trusted you")
    




        
   


