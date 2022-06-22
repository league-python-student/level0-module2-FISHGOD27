import random
from tkinter import messagebox, Tk, simpledialog
if __name__ == '__main__':

    window = Tk()
    window.withdraw()
    # TODO 1) Get 6 random numbers to put on your lottery ticket
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    num4 = random.randint(0,9)
    num5 = random.randint(0,9)
    num6 = random.randint(0,9)

    messagebox.showinfo(title='Winning ticket', message='The winning numbers are 1 4 6 6 2 8')
    messagebox.showinfo(title='Your Numbers', message= str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6))
    if str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) == '146628':
         messagebox.showinfo(title='OMG YOU WON!', message='No joke, I will give $1000 in cash.')
    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
