from tkinter import *
import tkinter.messagebox
import random
import math

t=Tk()
t.title("Guesser")
t.geometry("350x250")

num=random.randint(1, 100)

def say_name():
    guess_name=name_entry.get()
    tkinter.messagebox('Greeting',"Hello"+name_entry+"I Am Thinking Of A Number Between 1 And 100 Can You Guess It")

def guess_number():
    guess_number=int(guess_entry.get())
    if guess_number == num:
        tkinter.messagebox("Congrats","You Guessed Right")
    if guess_number < num:
        tkinter.messagebox("low", "You'r Guess Is To Low")
    if guess_number > num:
        tkinter.messagebox("high", "You'r Guess Is To High")

        
    












t.mainloop()