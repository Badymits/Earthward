# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init:
    image splash1 = "Syntax.png"
    image splash2 = "bb.png"
    image splash3 = "edit_1.jpg"

# The game starts here.
label splashscreen:
    
    
    $ renpy.pause(0, hard=True)
    scene black

    $ renpy.pause(0, hard=True)

    show splash1 with dissolve
    $ renpy.pause(1.0, hard=True)

    show splash2 with dissolve
    $ renpy.pause(1.0, hard=True)

    play music "audio/Kingdom-Hearts-Birth-By-Sleep-OST-Dearly-Beloved.ogg"
    
    scene black with dissolve
    $ renpy.pause(3.0, hard=True)
    
    return

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "Test shabu"

    # This ends the game.

    return
