import os
from random import choice
from hangman_art import stages, logo
from hangman_words import words

LIVES = 6

selected_word = choice(words)
# print(selected_word)
result = ["_"] * len(selected_word)

def show_result():
    for char in result:
        print(char, end=" ")
    print("\n")

print(logo)
show_result()
while "_" in result and LIVES > 0:
    guess = str(input("Guess a letter:")).lower()
    os.system("clear")
    # print(guess in selected_word)
    if guess in result:
        print(f"You have already guessed {guess}")
    elif guess in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i] == guess:
                result[i] = guess
        print("You guessed it right.")
        show_result()
    else:
        LIVES = LIVES - 1
        print(f"You guessed {guess}, that's not correct. You loose a life.")
        show_result()
        print(stages[LIVES])

if LIVES == 0:
    print(f"Hanged!!! Game Over. The letter was: {selected_word}")
else:
    print(f"Yay!!! You Guuessed it -> {selected_word}")
