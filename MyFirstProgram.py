#asks for name and desire to play game
print("Hello! This is Jade's first independent Python program.")
name = input("What's your name? ")
print("\nNice to meet you, " + name.title() + "!")
response = input("Would you like to play a guessing game? (y/n) ")
while response.lower() != "y" and response.lower() != "n":
  print("\nThat's not a valid answer. You have to say y or n.")
  response = input("Would you like to play a guessing game? (y/n) ")

#weeds out people who don't want to play
if response.lower() == "n":
  print("\nwell alright then. not like I'm offended or anything...")
  input("Press Enter to close this program and continue with your sad, sad life.")

#introduces game and sets up value
elif response.lower() == "y":
  print("\nHooray, I love games! :D")
  print("OK, so I'm thinking of a whole number between 1 and 10. \nYou have three chances to guess it!")
  import random
  number = random.randint(1,10)
  count = 1

#takes guesses and ends program
  while count<4:
    print("\nGuess Number " + str(count))
    guess=input("What's your guess? ")
    if int(guess)==number:
      print("Well done! You guessed my number!")
      break
    else:
      count+=1
      if count<4:
        print("Bad luck! You've got " + str(4-count) + " guesses left.")
      else:
        print("Bad luck! You've run out of guesses!")
        print("My number was " + str(number))
  input("\nPress Enter to exit the game.")
   
        
      
