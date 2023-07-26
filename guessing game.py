import random

user = input("Enter name: ")
print(f"Welcome {user} to Guessing game101, have fun!")

keep_playing = True
while keep_playing:
      print("There are diferent levels: easy, medium and hard")
      print("For easy, you have 6 chances to guess a number between 1-10")
      print("For meduim, you have 4 chances to guess a number between 1-20")
      print("For hard, you have 4 chances to guess a number between 1-50")
      break
game_level = input("Select desired level: ").lower()
if game_level == "easy":
  secret_number = random.randint(1,10)
  guess_count = 0
  guess_limit = 6
  while guess_count < guess_limit:
        guess = int(input("Guess:  "))
        guess_limit -= 1
        if guess == secret_number:
            print("You got it right!")
            break
        else:
          print("That was wrong")
          print(f"You have {guess_limit} guesses left")

  else:
      print("Game Over!")

elif game_level == "medium":
    secret_number = random.randint(1,20)
    guess_count = 0
    guess_limit = 4
    while guess_count < guess_limit:
       guess = int(input("Guess:  "))
       guess_count += 0
       guess_limit -= 1
       if guess == secret_number:
          print("You got it right!")
          break
       else:
          print("That was wrong")
          print(f"You have {guess_limit} guesses left")
    else:
      print("Game Over!")

elif game_level == "hard":
    secret_number = random.randint(1,50)
    guess_count = 0
    guess_limit = 4
    while guess_count < guess_limit:
        guess = int(input("Guess:  "))
        guess_limit -= 1
        if guess == secret_number:
            print("You got it right!")
            break
        else:
          print("That was wrong")
          print(f"You have {guess_limit} guesses left")
    else:
      print("Game Over!")

else:
    print("Invalid, try easy, medium or hard")