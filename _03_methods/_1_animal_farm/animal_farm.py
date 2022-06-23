import tkinter as tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound

window = None


def animals():
    global window
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.
    question = simpledialog.askstring(title='Animal', prompt='what animal would you like?')
    if question == 'cow':
        moo()
    elif question == 'duck':
        quack()
    elif question == 'cat':
        meow()
    elif question == 'dog':
        woof()
    elif question == 'llama':
        llama_scream()
    # TODO 2. Make it so that the user can keep entering new animals.

    # TODO 3. If the user enters 'exit', stop the program


# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()


def moo():
    playsound('moo.wav')
    show_image('cow.jpg')



def quack():
    playsound('quack.wav')
    show_image('duck.jpg')



def woof():
    playsound('woof.wav')
    show_image('dog.jpg')



def meow():
    playsound('meow.wav')
    show_image('cat.jpg')



def llama_scream():
    playsound('llama.wav')
    show_image('llama.jpg')



if __name__ == '__main__':
    animals()
