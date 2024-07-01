import tkinter as tk
from tkinter import messagebox
import random
import time

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.number = random.randint(1, 200)
        self.guessesTaken = 0
        
        self.intro_frame = tk.Frame(root)
        self.intro_frame.pack()
        
        self.intro_label = tk.Label(self.intro_frame, text="May I ask you for your name?")
        self.intro_label.pack()
        
        self.name_entry = tk.Entry(self.intro_frame)
        self.name_entry.pack()
        
        self.start_button = tk.Button(self.intro_frame, text="Start Game", command=self.start_game)
        self.start_button.pack()
        
        self.game_frame = tk.Frame(root)
        
        self.instructions_label = tk.Label(self.game_frame, text="I am thinking of a number between 1 and 200. Go ahead, guess!")
        self.instructions_label.pack()
        
        self.guess_entry = tk.Entry(self.game_frame)
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(self.game_frame, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.feedback_label = tk.Label(self.game_frame, text="")
        self.feedback_label.pack()
        
        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack_forget()
        
    def start_game(self):
        self.name = self.name_entry.get()
        if not self.name:
            messagebox.showwarning("Warning", "Please enter your name.")
            return
        
        self.intro_frame.pack_forget()
        self.game_frame.pack()
        
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="I don't think that is a number. Sorry.")
            return
        
        if guess < 1 or guess > 200:
            self.feedback_label.config(text="Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")
            return
        
        self.guessesTaken += 1
        
        if guess < self.number:
            self.feedback_label.config(text="The guess of the number that you have entered is too low. Try Again!")
        elif guess > self.number:
            self.feedback_label.config(text="The guess of the number that you have entered is too high. Try Again!")
        else:
            messagebox.showinfo("Congratulations", f"Good job, {self.name}! You guessed my number in {self.guessesTaken} guesses!")
            self.end_game()
        
        if self.guessesTaken >= 6 and guess != self.number:
            messagebox.showinfo("Game Over", f"Nope. The number I was thinking of was {self.number}")
            self.end_game()
        
    def end_game(self):
        self.game_frame.pack_forget()
        self.play_again_button.pack()
        
    def play_again(self):
        self.number = random.randint(1, 200)
        self.guessesTaken = 0
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.play_again_button.pack_forget()
        self.intro_frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
