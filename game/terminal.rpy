#Terminal
label terminal:
    hide targetpos
    hide posanim
    
    hide starssmall
    hide starsmid
    hide starsbig
    
    hide screen inventory
    
    show bg terminal at topleft
    
    show text "{size=16}Commands: [term1]\n\nNothing to do.{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)



#If commands
    if term1 == "help":
        show text "{size=16}Hello World! \n The terminal gives you the acces tour your entire system.\nType the commands you need and press Enter.\n\n Here some useful commands to start: \n\nlocate = search for known position in the databank. \n Exemple: locate sun, locate prison, locate xy\n\ncam = set up space ship camera. \n help = show this help file. \n More: log, cheat, sos... {/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
    
    if term1 == "cam top":
        show text "{size=16}Commands: [term1]\n\nCamera view changed to top.{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ spaceshipdir = 1

    if term1 == "cam right":
        show text "{size=16}Commands: [term1]\n\nCamera view changed to right.{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ spaceshipdir = 2
        
    if term1 == "cam bottom":
        show text "{size=16}Commands: [term1]\n\nCamera view changed to bottom.{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ spaceshipdir = 3
    
    if term1 == "cam left":
        show text "{size=16}Commands: [term1]\n\nCamera view changed to left.{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ spaceshipdir = 4
        


    if term1 == "cheat":
        show text "{size=16}Commands: [term1]\n\nAha!{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)


    
    if term1 == "sos":
        show text "{size=16}Commands: [term1]\n\nS.O.S message sent. \n{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)

    
        
    if term1 == "locate":
        show text "{size=16}SEARCH IN SPACE\nCommand: [term1]\n\nUse the command locate to find planets and objects. \nExemples: \nlocate xy, locate prison, locate sun...{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)

    if term1 == "cam":
        show text "{size=16}SET UP SPACE SHIP CAMERA\nCommand: [term1]\n\nUse the command to set up the space ship camera. \nExemples: \ncam top, cam bottom, cam left, cam right.{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)


#locate planets
    
    if term1 == "locate xy":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Planet\nName: Planet XY\nPosition: x293, y331{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "293"
        $ tooy = "331"
        jump copynav
        
        
    if term1 == "locate prison":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Space Ship\nName: Prison\nPosition: x320, y370{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "320"
        $ tooy = "370"
        jump copynav

    if term1 == "locate sun":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Sun\nName: Sun333\nPosition: x300, y300{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "300"
        $ tooy = "300"
        jump copynav

    if term1 == "locate aldabran":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Planet\nName: Aldabran\nPosition: x184, y253{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "184"
        $ tooy = "253"
        jump copynav
        
    if term1 == "locate meteoroid":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Meteoroid\nName: Meteoroid 539\nPosition: x210, y375{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "210"
        $ tooy = "375"
        jump copynav
        
    if term1 == "locate dealer":
        show text "{size=16}Commands: [term1]\n\nENTRY WAS DELETED\nPosition: x280, y120{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "280"
        $ tooy = "120"
        jump copynav

        
    if term1 == "locate betria":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Planet\nName: Betria\nPosition: x402, y242{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "402"
        $ tooy = "242"
        jump copynav

    if term1 == "locate matar":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Planet\nName: Matar\nPosition: x256, y200{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "256"
        $ tooy = "200"
        jump copynav
        
        
    if term1 == "locate polaris":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Planet\nName: Polaris\nPosition: x180, y470{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "180"
        $ tooy = "470"
        jump copynav

    if term1 == "locate iss":
        show text "{size=16}Commands: [term1]\n\nDATA FOUND\nType: Space Station\nName: Industrial Space Station\nPosition: x341, y143{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        $ toox = "341"
        $ tooy = "143"
        jump copynav
        

    if term1 == "locate planets" and coorcopy >= 1:
    
        show text "{size=16}PLANETS LIST\nCommands: [term1]\n\nDATA FOUND\nprison: x320 y370 \nxy: x293 y331 \nsun: x300 y300 \naldabran: x184 y253 \nmeteoroid: x210 y375 \nbetria: x402 y242 \nmatar: x256 y200 \npolaris: x180 y470 \niss: x341 y143{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
        
        menu:
            "show distance map":
                hide text
                hide bg
                hide ship
                show distance at truecenter
                menu:
                    "back":
                        hide distance
                        jump terminal
            
            "back":
                $ term1 = ""
                jump terminal

    
    
#log
    image logtext = Text("{size=16}[log]{/size}", xpos = 50, ypos=190, xanchor=0.0, yanchor=0.0, xmaximum = 500)

    if term1 == "log":
        hide text
        show text "{size=16}NAVIGATION LOG:\n[log]{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0, xmaximum = 500)
        #show logtext
        jump log
        
        
        
# IO-NET
    if term1 == "ionet":
        hide text
        
        call ioupdate from _call_ioupdate_1
        
        show text "{size=16}WELCOME TO THE IO-NETWORK!\nCommand: [term1]\n\nCONNECTED NODES: [io_nodes]\n\nmeteoroid node: [io_meteoroid]\npolaris node: [io_pol]\nbetria lake node: [io_blake]\nbetria islands node: [io_bislands]\naldabran node: [io_alswreck]\n\nNEEDED NODES: [io_maxnodes]{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0, xmaximum = 500)
        
        if io_nodes == io_maxnodes:
            "It's seems all needed nodes for a basic network are running and connected!"
            "Do you want to start a basic network and decentralize it? This will share all the data around the network. Do you want to do it?"
            menu:
                "yes":
                    pass
                "no":
                    $ term1 = ""
                    jump terminal
            with flash
            "IO-net Basic Network started and decentralized."
            "Enjoy the freedom... ! "
            hide bg
            jump win





#Menu
    menu:
        "Use the Terminal":
            python:
                term1 = renpy.input("Type a command:")
                term1 = term1.strip()
                if not term1:
                    term1 = "0"

            jump terminal
                
        "Help":
            $ term1 = "help"
            jump terminal
        "back":
            if backto == "spaceship":
                jump spaceship
            if backto == "cockpit":
                jump cockpit
            if backto == "xy":
                show posanim at Position(xpos = 280, ypos=210, xanchor=0.5, yanchor=0.5):
                jump xy
            if backto == "polaris":
                show posanim at Position(xpos = 455, ypos=368, xanchor=0.5, yanchor=0.5):
                jump polaris

#term copy nav
label copynav:
    hide logtext
    
    menu:
        "Copy Coordinates to Navigation System":
            show text "{size=16}Copying coordinates...\n\nPlease wait... \n{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
            $ term1 = ""
            pause 1
            show text "{size=16}JOB DONE:\nCoordinates copied to Ship Navigation System!{/size}" at Position(xpos = 298, ypos=160, xanchor=0.5, yanchor=0.0)
            pause 2
            
            if backto == "spaceship" or backto == "cockpit":
                hide text
                jump cockpit
            #if backto == "cockpit":
                #jump cockpit
                
            else:
                jump terminal
        "back":
            $ term1 = ""
            jump terminal


#nvigation log
label log:
    menu:
        "Planets":
            menu:
                
                "xy" if v_xy == True:
                    $ term1 = "locate xy"
                    jump terminal
                    
                "aldabran" if v_aldabran == True:
                    $ term1 = "locate aldabran"
                    jump terminal
                    
                "betria" if v_betria == True:
                    $ term1 = "locate betria"
                    jump terminal
                    
                "matar" if v_matar == True:
                    $ term1 = "locate matar"
                    jump terminal
                
                "polaris" if v_polaris == True:
                    $ term1 = "locate polaris"
                    jump terminal
                    
                "back":
                    jump log
        
        "Other":
            menu:
                "sun" if v_sun == True:
                    $ term1 = "locate sun"
                    jump terminal
                    
                "meteoroid" if v_meteoroid == True:
                    $ term1 = "locate meteoroid"
                    jump terminal
        
                "industrial space station" if v_iss == True:
                    $ term1 = "locate iss"
                    jump terminal
                    
                "prison" if v_prison == True:
                    $ term1 = "locate prison"
                    jump terminal
                
                "dealer" if v_dealer == True:
                    $ term1 = "locate dealer"
                    jump terminal
                    
                "back":
                    jump log
        
                
        "back":
            hide logtext
            $ term1 = ""
            jump terminal
    
