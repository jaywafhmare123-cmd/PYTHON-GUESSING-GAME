secret_game = "GRAND THEFT AUTO 6"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_game and not out_of_guesses:
   if guess_count < guess_limit:
       guess = input("Guess the secret game: ")
       guess_count += 1
   else:
       out_of_guesses = True

if out_of_guesses:
   print("You guessed the wrong game!")
else:
   print("You guessed the correct game!")
