import random

name = raw_input('Hello! What is your name?\n')

guesses_made = 0

number = random.randint(1, 20)
print 'Well, %s, I am thinking of a number between 1 and 20.' % (name)

while guesses_made < 6:
  try:

      guess = int(raw_input('Take a guess: '))

      guesses_made += 1

      if guess < number:
          print 'Your guess is too low. You have %s guesses remaining' % (6 - guesses_made)

      if guess > number:
          print 'Your guess is too high. You have %s guesses remaining' % (6 - guesses_made)

      if guess == number:
          break

  except ValueError:
    print 'You need to type in a number, dum dum'

if guess == number:
    print 'Good job, %s! You guessed my number in %s guesses!' % (name, guesses_made)
else:
    print 'Nope. The number I was thinking of was %s' % (number)