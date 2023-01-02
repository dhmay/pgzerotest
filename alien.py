# import the library that knows how to run the game
import pgzrun
from cutscenes.cutscenes import CutSceneManager, StupidTextCutScene

# make an "actor" to represent the alien. The Actor will keep
# track of where the alien is on the screen and lots of other stuff
slimearm = Actor('alien')
# position the alien's top right corner at coordinates (0, 10)
slimearm.topright = 0, 10

# define variables representing the width and height of the window
WIDTH = 712
HEIGHT = 508

game_state_dict = {
    "phase": "intro",
}

def draw():
    """This method defines what happens when the screen refreshes
    """
    cutscene_manager = game_state_dict["cutscene_manager"]

    if cutscene_manager.running_cutscene is not None:
        cutscene = cutscene_manager.running_cutscene
        cutscene.draw(screen)
        if cutscene.finished:
            cutscene_manager.running_cutscene = None
            if game_state_dict["phase"] == "intro":
                game_state_dict["phase"] = "game"
    else:  # no cutscene running. Main game phase.
        screen.blit("background",(0,0))
        # draw the alien
        slimearm.draw()

def update():
    """This method defines what happens *between* screen refreshes
    """
    if "cutscene_manager" not in game_state_dict:
        game_state_dict["cutscene_manager"] = CutSceneManager()
    cutscene_manager = game_state_dict["cutscene_manager"]

    if game_state_dict["phase"] == "intro" and cutscene_manager.running_cutscene is None:
        cutscene_manager.show_cutscene(StupidTextCutScene())

    if cutscene_manager.running_cutscene is not None:
        cutscene_manager.running_cutscene.update()
    else:
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