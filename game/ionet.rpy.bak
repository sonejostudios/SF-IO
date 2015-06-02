#IO-Net

label ioupdate:
    $ io_nodes = int(io_meteoroid) + int(io_pol) + int(io_blake) + int(io_alswreck) + int(io_bislands)
    
    return


label ioinstall:
            show text "Copying." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 0.5
            hide text
            pause 0.5
            show text "Copying.." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 0.5
            hide text
            pause 0.5
            show text "Copying..." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 0.5
            hide text
            pause 0.5
            show text "Copying done." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 1
            hide text
            with flash
            
            # set meteoroid node
            if spaceshippos == 5: 
                $ io_meteoroid = True
                show ionetsender at Position(xpos = 135 , ypos=377, xanchor=0.5, yanchor=0.5)
            
            # set polaris node    
            if spaceshippos == 9:
                $ io_pol = True
                show ionetsender at Position(xpos = 70 , ypos=377, xanchor=0.5, yanchor=0.5)
            
            # set betria lake node    
            if spaceshippos == 7 and onislands == False:
                $ io_blake = True
                show ionetsender at Position(xpos = 137 , ypos=377, xanchor=0.5, yanchor=0.5)
                
                
            # set betria island node    
            if spaceshippos == 7 and onislands == True:
                $ io_bislands = True
                show ionetsender at Position(xpos = 137 , ypos=377, xanchor=0.5, yanchor=0.5)
                

            # set aldabran node    
            if spaceshippos == 4:
                $ io_alswreck = True
                show ionetsender at Position(xpos = 137 , ypos=377, xanchor=0.5, yanchor=0.5)
                

            
            
            show text "Installation..." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 2
            show text "Connecting to\nnetwork..." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 2
            show text "Sending request\nfor Node ID..." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 2
            show text "Create Node..." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 2
            show text "Connecting..." at  Position(xpos = 300 , ypos=300, xanchor=0.5, yanchor=0.5)
            pause 2
            hide text
            with flash
            
            "Connected!\nIO-net node is ready. Enjoy!"
            
            #this goes straigt to ioinfo
            


label ioinfo:
    
    call ioupdate
     
    "Welcome to IO-net!\n\nNode Status: Connected\nNodes in Network: [io_nodes]\n\nPlease enter ionet in a Terminal for more information."
    
    return

