#MADE BY MRCAT
import os
import random
import time
from colorama import init, Fore #<----- Install this
import pygame #<------- This too :3

# Initialize colorama
init(autoreset=True)

# Initialize Pygame mixer
pygame.mixer.init()

# Load the sound file
audio_file = "boom.mp3"
pygame.mixer.music.load(audio_file)

def print_title():
    print("\n" + Fore.CYAN + "-----------------------------")
    print(Fore.CYAN + "    Russian Rolette by ᴅᴏʀᴏⓒ ")
    print(Fore.CYAN + "-----------------------------")

def guess_the_number():
    secret_number = random.randint(1, 10)

    print("Try to guess the correct number between 1 and 10.")

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess == secret_number:
            print(Fore.GREEN + "Congratulations! You guessed the correct number.")
            break
        else:
            print(Fore.RED + "Incorrect guess. Try again.")
            attempts += 1

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
        time.sleep(1)
        pygame.mixer.music.play()
        os.system("shutdown /s /t 2")
        print("You died.")

if __name__ == "__main__":
    print_title()

    while True:
        print("\n1. Play")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
