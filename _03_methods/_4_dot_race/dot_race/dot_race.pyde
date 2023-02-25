# When you are done, this program will draw an ellipse
# that travels across the screen when the mouse is pressed.

# ***********  SOUND ***************
# Some computers are unable to play sounds.
# If you cannot play sound on this computer, set canPlaySounds to false.
# If you are not sure, ask your teacher



def setup():
    size(800, 400)
    global x
    global x2
    global counter
    global has_started
    # 1. Set the variable named x to 50.
    x=50
    x2=50
    counter=30
    has_started=0

def draw():
    background(200, 200, 200)
    global x
    global x2
    global counter
    global has_started
    # 2. Draw an ellipse of height and width 50. Make sure to use the x variable
    # for its X position. Pick a y value that places it half way down the window.


    textSize(24)
    textAlign(CENTER)



    # 3. Fill in the ellipse with a nice color. Remember to put it above the code
    # where you draw the ellipse.

    # 4. If the mouse is pressed change the x value so that the dot moves to the right

    if mousePressed:
        x+= 7
    if keyPressed:
        has_started = 3
    if has_started == 3:
        counter = counter - 1
    else:
         text("Press the space bar to start the race", width/2, height/2)
    if counter <= 0:
        noStroke()
        fill('#FFFFFF')
        rect(750, -5, 50, 405)
        fill('#5D1AFF')
        ellipse(x,100, 50,50)
        fill('#F5DD05')
        ellipse(x2,200, 50,50)
        x2=x2+5

    else:
        text(counter, width/3, height/4)


        #background('#FFFFFF')
        #text("2", width/3, height/4)

    # 5. If your dot moves slowly, make it move faster. If it moves too quickly,
    # slow it down (you have to figure out what part of your code to change)

    # 6. Use an if statement to play a sound (ding) when your dot crosses the finish
    # line (right side of window). A playSound() method is provided (you have to
    # uncomment the code at the bottom of this program to get this to work)
    if x > 800:
        play_sound()
        x2=-50
    if x2 > 800:
       text("You Lost!" , width/2, height/2)
       x=-50



def play_sound():
    fill(0)
    textSize(36)
    text("WINNER!!", width/2, height/2)


