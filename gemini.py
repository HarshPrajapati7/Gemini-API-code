import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    """Check the user's guess."""
    global attempts
    guess = int(entry.get())
    if guess < secret_number:
        messagebox.showinfo("Result", "Too low!")
    elif guess > secret_number:
        messagebox.showinfo("Result", "Too high!")
    else:
        attempts += 1
        messagebox.showinfo("Congratulations", f"Congratulations! You guessed the number in {attempts} attempts.")
        reset_game()

def reset_game():
    """Reset the game."""
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    messagebox.showinfo("New Game", "A new game has started! Try to guess the number between 1 and 100.")

# Create Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")

# Create label and entry for user input
label = tk.Label(root, text="Enter your guess:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Create button to check the guess
check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.pack()

# Create button to reset the game
reset_button = tk.Button(root, text="New Game", command=reset_game)
reset_button.pack()

# Run Tkinter event loop
root.mainloop()
