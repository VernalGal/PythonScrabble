import random

def jumble_word(word):
    jumbled_word = ''.join(random.sample(word, len(word)))
    return jumbled_word

def play_game():
    words = ['python', 'programming', 'computer', 'keyboard', 'mouse', 'laptop']
    word = random.choice(words)
    jumbled_word = jumble_word(word)
    print(f'Unjumble the letters to make a word: {jumbled_word}')

    num_of_guesses = 0
    while True:
        guess = input('Enter your guess (type \'quit\' to exit): ')
        num_of_guesses += 1

        if guess.lower() == 'quit':
            print('Thanks for playing!')
            break
        elif guess.lower() == word:
            print(f'Congratulations! You guessed the word in {num_of_guesses} guesses.')
            break
        else:
            print('Incorrect guess. Try again.')

play_game()

