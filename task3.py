#Building a number guessing game
import random

#User's name
print("Hello! what is your name: ")
myName = input()
print("Hi " + str(myName) + "!" + " Let's play a number guessing game.")

def random_game():

    play = True
    while play:

        easy = random.randint(1, 10)
        medium = random.randint(1, 20)
        hard = random.randint(1, 50)
        # prompts the user to select a difficulty to play on
        print("Would you like to play on easy, medium, or hard? Type 'e' for easy, 'm' for medium, or 'h' for hard" )

        level_selection = True
        while level_selection:
            level = input()
            if level == "e":
                print("Awesome! We will begin with easy!")
                level_selection = not True
                break
            if level == "m":
                print("Awesome! We will begin with medium!")
                level_selection = not True
                break
            if level == "h":
                print("Awesome! We will begin with hard!")
                level_selection = not True
                break
            else:
                print("Invalid input!\n Please enter either e, m, or h. ")

    # if the user selects e for Easy - 6 tries
        if level == 'e':
            print("You have 6 chances to guess a number between 1 - 10.")
            guesses_left = 6
            while guesses_left != 0:
                try1 = int(input("What's your guess?: "))
                if try1 == easy:
                    print("You got it right! " + str(easy))
                    break
                elif try1 != easy:
                    print("That was wrong, try again!")
                guesses_left -= 1
                print("You now have " + str(guesses_left) + " guesses left!")

                # if the user run out of guesses
                if guesses_left == 0:
                    print("Game over!")

    # if the user selects m for medium - 4 tries
        if level == 'm':
            print("You have 4 chances to guess a number between 1 - 20")
            guesses_left = 4
            while guesses_left != 0:
                try1 = int(input("What's your guess?: "))
                if try1 == medium:
                    print("You got it right! " + str(medium))
                    break
                elif try1 != medium:
                    print("That was wrong, try again!")
                guesses_left -= 1
                print(("You now have " + str(guesses_left) + " guesses left!"))

                # if the user run out of guess
                if guesses_left == 0:
                    print("Game over!")

    # if the user selects m for hard - 3 tries
        if level == 'h':
            print("You have 3 chances to guess a number between 1 - 50")
            guesses_left = 3
            while guesses_left != 0:
                try1 = int(input("What's your guess?: "))
                if try1 == hard:
                    print("You got it right! " + str(hard))
                    break
                elif try1 != hard:
                    print("That was wrong, try again!")
                guesses_left -= 1
                print(("You now have " + str(guesses_left) + " guesses left!"))

                # if the user run out of guess
                if guesses_left == 0:
                    print("Game over!")

        maybe_play = True
        while maybe_play:
            again = input("would you care to play again?\nyes or no\n")
            if again == 'no' or again == 'No':
                print("OK, Thank you for playing!")
                maybe_play = not True
                play = not True
            elif again == 'yes' or 'Yes':
                print("Ok, Let's play again!")
                maybe_play = not True
                play = True
            else:
                print("Please enter either yes or no.")
                input()
                maybe_play = not True
                play = not True

random_game()
