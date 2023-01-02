# import the library that knows how to run the game
import pgzrun

# make an "actor" to represent the alien. The Actor will keep
# track of where the alien is on the screen and lots of other stuff
slimearm = Actor('alien')
# position the alien's top right corner at coordinates (0, 10)
slimearm.topright = 0, 10

# define variables representing the width and height of the window
WIDTH = 712
HEIGHT = 508

def draw():
    """This method defines what happens when the screen refreshes
    """
    # fill the screen with purple
    screen.fill((40, 6, 100))
    # draw the alien
    slimearm.draw()

def update():
    """This method defines what happens *between* screen refreshes
    """
    # move the alien slightly to the right
    slimearm.left += 2
    # if the alien is off the edge of the screen...
    if slimearm.left > WIDTH:
        # move the alien to the left edge
        slimearm.right = 0

def on_mouse_down(pos):
    """This method defines what happens when you click
    """
    # Check whether the cursor is on the alien
    if slimearm.collidepoint(pos):
        # call the method we wrote to determine what happens
        # when the alien is clicked
        set_alien_hurt()
    else:
        print("you missed me!")
        sounds.wetfart.play()

def set_alien_hurt():
    """Define behavior when alien is hurt
    """
    print("Eek!")
    # play a sound called "eep".
    # I don't know if it waits for the sound to complete before moving on.
    # Let's test!
    sounds.eep.play()
    # Change the alien's image to the hurt version
    slimearm.image = 'alien_hurt'
    # Schedule a future event to reset the alien back to normal.
    # In one second, I think?
    clock.schedule_unique(set_alien_normal, 6.25)
    sounds.dramaticfart.play()

def set_alien_normal():
    """Return alien to normal image
    """
    slimearm.image = 'alien'

# run the game
pgzrun.go()