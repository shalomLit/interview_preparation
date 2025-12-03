import random
from shapes import shapes

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = -1
game_over = False

result = len(chosen_word) * "_"

while not game_over:
    print(f"Word to guess: {result}")
    guess = input("Guess a letter:").lower()

    if guess not in chosen_word:
        lives += 1
        print(shapes[lives])
        if lives == 6:
            print("You lose!")
            game_over = True

    for i, letter in enumerate(chosen_word):
        if guess == letter:
            result = result[:i] + guess + result[i + 1:]

    if "_" not in result:
        print("You win!")
        game_over = True
