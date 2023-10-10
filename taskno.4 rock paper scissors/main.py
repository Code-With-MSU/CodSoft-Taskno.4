import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Enter your name:").grid(row=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1)
        return self.entry  # Focus on the entry field

    def apply(self):
        self.result = self.entry.get()

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!", fg="blue")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result_label.config(text=f"{user_name} wins!", fg="green")
    else:
        computer_score += 1
        result_label.config(text="Computer wins!", fg="red")

    update_score()

def update_score():
    score_label.config(text=f"{user_name}: {user_score}  Computer: {computer_score}")

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    determine_winner(user_choice, computer_choice)

def show_game_rules_and_get_name():
    global user_name
    rules = (
        "       Game Rules\n"
        "1. Rock beats Scissors.\n"
        "2. Scissors beats Paper.\n"
        "3. Paper beats Rock.\n\n"
        "Developed by: Muhammad Samiullah"
    )
    messagebox.showinfo("Game Rules", rules)
    
    dialog = CustomDialog(root, "User Name")
    user_name = dialog.result

    if user_name:
        welcome_message = f"Welcome, {user_name}!"
        messagebox.showinfo("Welcome", welcome_message)

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("900x600")
root.resizable(False, False)

# Initialize variables
user_score = 0
computer_score = 0
user_name = "User"

bg_image = tk.PhotoImage(file="pic.png")

bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

text_label = tk.Label(root, text="Rock, Paper, and Scissors", font=("Helvetica", 30, "bold"), bg="lemon chiffon", fg="black")
text_label.grid(row=1, column=2, columnspan=3, padx=200, pady=50)

option_label = tk.Label(root, text="Choose your option", font=("Helvetica", 15, "bold"), bg="lemon chiffon", fg="black")
option_label.grid(row=2, column=0, columnspan=6, padx=10)

rock_image = tk.PhotoImage(file="rock.png")
paper_image = tk.PhotoImage(file="paper.png")
scissors_image = tk.PhotoImage(file="scissors.png")

rock_button = tk.Button(root, image=rock_image, command=lambda: play("Rock"))
paper_button = tk.Button(root, image=paper_image, command=lambda: play("Paper"))
scissors_button = tk.Button(root, image=scissors_image, command=lambda: play("Scissors"))

rock_button.grid(row=3, column=2, padx=20, pady=20)
paper_button.grid(row=3, column=3, padx=20, pady=20)
scissors_button.grid(row=3, column=4, padx=20, pady=20)

result_label = tk.Label(root, text="Result", font=("Helvetica", 20, "bold"), bg="lemon chiffon", fg="black")
result_label.grid(row=4, column=0, columnspan=6, pady=20)

show_game_rules_and_get_name()

score_label = tk.Label(root, text=f"{user_name}: 0  Computer: 0", font=("Helvetica", 14, "bold"), bg="lemon chiffon", fg="black")
score_label.grid(row=7, column=0, columnspan=6)




root.mainloop()
