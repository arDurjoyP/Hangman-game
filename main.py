import random
from hangman_words import word_list
from logo import stages, art
print(art)
chosen_word = random.choice(word_list)
# print(f"psst, chosen word is {chosen_word}")

lives = 6

display = []
for x in chosen_word:
    display += "_"

end_game = False


while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"you already guessed {guess} try another word")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_game = True
        print("you won! You guessed the word")

    if guess not in chosen_word:
        lives -= 1
        print("You lost a Life")
        if lives == 0:
            end_game = True
            print("You lost game over")
    
    print(stages[lives])
    






    








