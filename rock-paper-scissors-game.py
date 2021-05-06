# import library
from tkinter import *
import random

# initialize window
root = Tk()
root.geometry('400x400')
root.resizable(width=False, height=False)
root.title('Rock-Paper-Scissors')
root.config(bg='seashell3')

# input field to display the result
Result = StringVar()


# input field to take the user's choice
user_take = StringVar()


def start():
    """" move to the second page to play a game """
    home_frame.pack_forget()
    game_frame.pack()


def home():
    """" move to the home page """
    game_frame.pack_forget()
    home_frame.pack()


# fun to reset
def reset():
    """ reset input fields to restart game """
    Result.set("")
    user_take.set("")


# fun to close
def close():
    """ exit from game and close the application """
    root.destroy()


def play():
    """ compare between choices then print the result to user """
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')


# home_page
home_frame = Frame(root, bg='seashell3')
heading = Label(home_frame, text='Rock-Paper-Scissors', font='arial 18 bold', bg='seashell2')
start_btn = Button(home_frame, font='arial 13 bold', text='Start', padx=5, bg='seashell4', command=start)
start_btn.place(x=70, y=310)
close_btn = Button(home_frame, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=close)
close_btn.place(x=230, y=310)

# game_page
game_frame = Frame(root, bg='seashell3')
result = Entry(game_frame, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50, )
result.place(x=25, y=250)
play_btn = Button(game_frame, font='arial 13 bold', text='Play', padx=5, bg='seashell4', command=play)
play_btn.place(x=150, y=190)
reset_btn = Button(game_frame, font='arial 13 bold', text='Reset', padx=5, bg='seashell4', command=reset)
reset_btn.place(x=70, y=310)
home_btn = Button(game_frame, font='arial 13 bold', text='Home', padx=5, bg='seashell4', command=home)
home_btn.place(x=230, y=310)
instruction = Label(game_frame, text='Select One', font='arial 15 bold', bg='seashell2')
instruction.place(x=150, y=70)


# computer_choice
comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'


# Dictionary to create multiple buttons
values = {"Paper": "paper",
          "Rock": "rock",
          "Scissors": "scissors"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(game_frame, text=text, variable=user_take,
                value=value).pack(side=TOP, ipady=5)


# home_frame widgets
home_frame.pack()
heading.pack()
start_btn.pack()
close_btn.pack()

# game_frame widgets
# game_frame.pack()
instruction.pack()
play_btn.pack()
reset_btn.pack()
home_btn.pack()
result.pack()

# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
root.mainloop()
