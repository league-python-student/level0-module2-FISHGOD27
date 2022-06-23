import random
from tkinter import messagebox, Tk, simpledialog
if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    # TODO 1) Get 6 random numbers to put on your lottery ticket
    num1 = random.randint(0,3)
    #num2 = random.randint(0,9)
    #num3 = random.randint(0,9)
    #num4 = random.randint(0,9)
    #num5 = random.randint(0,9)
    #num6 = random.randint(0,9)

    messagebox.showinfo(title='Winning ticket', message='The winning number is 1')
    messagebox.showinfo(title='Your Number', message= str(num1))
    if str(num1) == '1':
         messagebox.showinfo(title='OMG YOU WON!', message='No joke, I will give $5 in cash.')
    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
