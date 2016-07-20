#IO-Net

label ioupdate:
    $ io_nodes = int(io_meteoroid) + int(io_pol) + int(io_blake) + int(io_alswreck) + int(io_bislands)
    
    return


label ioinstall:
    play sound "snd/modem.ogg"
    
    show text (_("Copying.")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 0.5
    hide text
    pause 0.5
    show text (_("Copying..")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 0.5
    hide text
    pause 0.5
    show text (_("Copying...")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 0.5
    hide text
    pause 0.5
    show text (_("Copying done.")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 1
    hide text
    play audio "snd/collect.ogg"
    with flash
    
    # set meteoroid node
    if spaceshippos == 5: 
        $ io_meteoroid = 1
        show ionetsender at Position(xpos = 135 , ypos=377, xanchor=0.5, yanchor=0.5)
    
    # set polaris node    
    if spaceshippos == 9:
        $ io_pol = 1
        show ionetsender at Position(xpos = 70 , ypos=377, xanchor=0.5, yanchor=0.5)
    
    # set betria lake node    
    if spaceshippos == 7 and onislands == False:
        $ io_blake = 1
        show ionetsender at Position(xpos = 137 , ypos=377, xanchor=0.5, yanchor=0.5)
        
        
    # set betria island node    
    if spaceshippos == 7 and onislands == True:
        $ io_bislands = 1
        show ionetsender at Position(xpos = 137 , ypos=377, xanchor=0.5, yanchor=0.5)
        

    # set aldabran node    
    if spaceshippos == 4:
        $ io_alswreck = 1
        show ionetsender at Position(xpos = 137 , ypos=377, xanchor=0.5, yanchor=0.5)
        

    
    
    show text (_("Installation...")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 2
    show text (_("Connecting to\nnetwork...")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 2
    show text (_("Sending request\nfor Node ID...")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 2
    show text (_("Create Node...")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 2
    show text (_("Connecting...")) at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
    pause 2
    hide text
    
    play sound "snd/connected.ogg"
    with flash
    
    "Connected!\nIO-net node is ready. Enjoy!"
    
    #this goes straigt to ioinfo
    


label ioinfo:
    
    call ioupdate from _call_ioupdate
     
    "Welcome to IO-net!\n\nNode Status: Connected\nNodes in Network: [io_nodes]\n\nPlease enter ionet in a Terminal for more information."
    
    return

