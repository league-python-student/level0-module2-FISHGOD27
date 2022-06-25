import random
from tkinter import messagebox, Tk, simpledialog
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
for i in range(10):
    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring(title='Magic 8 ball', prompt="Ask a yes or no question to the magic 8 ball, and it shall give you your answer.")
    # Make a variable and initialize it to a random number between 0 and 3
    answer = random.randint(0, 5)
    # If the random number is 0
    if question == 'is lukas a russian spy':
        messagebox.showinfo(title='answer', message='He is! And he is going to kill you!')
    elif answer == 0:
        messagebox.showinfo(title='answer', message='NO!')
        # tell the user "Yes"
    elif answer == 1:
        messagebox.showinfo(title='answer', message='YES!')
    # If the random number is 1
    elif answer == 2:
        messagebox.showinfo(title='answer', message='I am not getting paid enough for this!')
        # tell the user "No"
    elif answer == 3:
        messagebox.showinfo(title='answer', message='To be honest, I have no freaking idea.')
    # If the random number is 2
    elif answer == 4:
        messagebox.showinfo(title='answer', message='Thats gnarly!')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
    s1 = "5"

    s2 = "7"

    print(s1 + s2)
