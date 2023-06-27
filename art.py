import time
import random
name=input('What is your name? ')
print(f'Hello {name}. Let\'s play Hangman!')
time.sleep(1)
print('Start guessing...')
time.sleep(0.5)
words=['compete','substance','flowers','writer','sisters','receipt','reaction','jobless','python','programming']
word=random.choice(words)
guesses=''
turns=10
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end='')
        else:
            print('_',end='')
            failed+=1
    if failed == 0:
        print('You won!')
        break
    guess=input('guess a character: ')
    guesses+=guess
    if guess not in word:
        turns-=1
        print('Wrong')
        print(f'You have {turns} more guesses')
        if turns == 0:
            print('You loose')
