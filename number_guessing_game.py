import random, time

def game_start():
    print("\nWelcome to the Number Guessing Game! \nI'm thinking of a number from 1 and 100. \nYou have 5 chances to guess the correct number.")


def choose_mode():
    diff = ""
    print("\nPlease select the difficulty level: \n1. Easy (10 tries) \n2. Medium (5 tries) \n3. Hard (3 tries)")
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice == "1":
                diff = "Easy"
                print(f"Great! You have selected the {diff} difficulty level. \nLet's start the game!")
                return "10"
            elif choice == "2":
                diff = "Medium"
                print(f"Great! You have selected the {diff} difficulty level. \nLet's start the game!")
                return "5"
            elif choice == "3":
                diff = "Hard"
                print(f"Great! You have selected the {diff} difficulty level. \nLet's start the game!")
                return "3"
        except ValueError:
            print("Enter a number.")


def game(guesses, num):
    attempts = 0
    while guesses != 0:
        attempts = attempts + 1
        try:
            guess = int(input("Enter your guess: "))
            if guess == num:
                print(f"Congratulations! You have guessed the correct number in { attempts } attempts.\n")
                break
            elif guess > num:
                print(f"Incorrect! The number is less than {guess}.")
            elif guess < num:
                print(f"Incorrect! The number is greater than {guess}.")
        except ValueError:
            print("Enter a number.")
            guesses = guesses + 1
        guesses = guesses - 1
    if guesses == 0:    
        print(f"You failed. The number was {num}.\n")
    
def main():
    game_start()
    guesses = int(choose_mode())
    num = random.randint(1,100)
    print(num)
    game(guesses, num)

main()
time.sleep(2)
for i in range(40):
    print("Closing Down...")
    time.sleep(0.05)