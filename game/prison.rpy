#PRISON CELL
label prisoncell:
    show screen clock
    
    show bg prisoncellpic behind text at topleft
    if sta_prisondoor == False:
        with Dissolve(1.0)
        
    
    show posanim at Position(xpos = 230, ypos=270, xanchor=0.5, yanchor=0.5):
    
    show screen inventory
    
    $ spaceshippos = 1
    
    m "Hm it looks like a prison cell... where I am? And what to do now?"   
    menu:
        "look at the door":
            jump prisondoor
        
        "look around":
            m "There is a bed and a table with a lamp."
            jump prisoncellaround   
        
        "do nothing":
            m "No way, I want to be free!"
            jump prisoncell
            
        "go out of the cell" if sta_prisondoor == True:
            show posanim at Position(xpos = 300, ypos=350, xanchor=0.5, yanchor=0.5):
            play sound "snd/door-open.ogg"
            jump prisoncorridor
        
#PRISON DOOR        
label prisondoor:
    if sta_prisondoor == False:
        play sound "snd/door-locked.ogg"
        m "The door is locked."
        jump prisoncell
    
    else:
        m "The door is open now. I can go out if I want."
        jump prisoncell
            

#PRISON CELL LOOK AROUND            
label prisoncellaround:

    menu:
        "look at the table":
            m "There is the lamp on the table."
            jump prisoncellaround

        "look at the bed":
            m "The bed looks like nobody used it for a long time."
            menu:
                "look under the bed":
                    m "There is a socket."
                    if inv_lcable == True:
                        menu:
                            "use the cable with the socket":
                                $ sta_prisondoor = True
                                #with hpunch   #shake fx
                                play sound "snd/bzz.ogg"
                                with flash
                                
                                "BZZZZZ! You just made a short circuit! The door opens."
                                jump prisoncell
                            "back":
                                jump prisoncellaround
                    else:
                        jump prisoncellaround
                    
                "back":
                    jump prisoncellaround

        "look at the lamp":
            if inv_lcable == False:
                m "I could take this lamp apart, maybe it would be useful."
                menu:
                    "take the lamp apart":
                        $ inv_lcable = True
                        $ inv_lbulb = True
                        play sound "snd/collect.ogg"
                        with flash
                        "You got an electric cable and a bulb!"

                        jump prisoncellaround
                    "back":
                        jump prisoncellaround
                        
            else:
                m "The cable and the bulb are missing now."
                jump prisoncellaround
        
        "back":
            jump prisoncell

#PRISON CORRIDOR
label prisoncorridor:
    show bg prisoncorridorpic behind text at topleft
    m "This is the prison corridor. There 4 doors for the cells and a lift door."
    menu:
        "go to the lift":
            show posanim at Position(xpos = 80, ypos=370, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            jump prisonlift
        "go to cell nr. 01":
            play sound "snd/door-locked.ogg"
            m "This door is closed."
            jump prisoncorridor
        "go to cell nr. 02":
            play sound "snd/door-locked.ogg"
            m "This door is closed."
            jump prisoncorridor
        "go to cell nr. 03":
            play sound "snd/door-locked.ogg"
            m "This door is closed."
            jump prisoncorridor
        "go to cell nr. 04":
            play sound "snd/door-open.ogg"
            jump prisoncell
        

#PRISON LIFT
label prisonlift:
    hide text
    hide ship1
    hide ship2
    hide ship3
    
    show bg prisonliftpic behind text
    

    menu: 
        "03":
            m "I don't think they want to know that I'm escaping right now!"
            jump prisonlift
        "02":
            if prison_lift is not 2:
                play sound "snd/lift.ogg"
                show posanim:
                    linear 2 ypos 210 
                pause 2.5
            $ prison_lift = 2
            show posanim at Position(xpos = 300, ypos=370, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            jump prisonflats
        "01":
            if prison_lift is not 1:
                play sound "snd/lift.ogg"
                show posanim:
                    linear 2 ypos 260 
                pause 2.5
            $ prison_lift = 1
            hide posanim
            play sound "snd/door-open.ogg"
            jump warehouse
        "00":
            if prison_lift is not 0:
                play sound "snd/lift.ogg"
                show posanim:
                    linear 2 ypos 315
                pause 2.5
            $ prison_lift = 0            
            show posanim at Position(xpos = 295, ypos=360, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            stop music fadeout 1.0
            jump spaceport
        "-01":
            if prison_lift is not -1:
                play sound "snd/lift.ogg"
                show posanim:
                    linear 2 ypos 370 
                pause 2.5
            $ prison_lift = -1
            show posanim at Position(xpos = 300, ypos=200, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            jump prisoncorridor
        

    
#PRISON FLATES
label prisonflats:
    
    show bg flatcorridorpic behind text
    m "There are 3 flats, a space suite stock and 4 doors."
    
    menu:
        "go to one flat":
            menu:
                "go to flat 01":
                    play sound "snd/door-locked.ogg"
                    m "The door is closed."
                    jump prisonflats

                "go to flat 02":
                    play sound "snd/door-locked.ogg"
                    m "The door is closed."
                    jump prisonflats
                "go to flat 03":
                    play sound "snd/door-locked.ogg"
                    m "The door is closed."
                    jump prisonflats
                "back":
                    jump prisonflats
            
        "go to one door":
            menu:
                "go to the door left":
                    play sound "snd/door-locked.ogg"
                    m "The door is closed."
                    jump prisonflats
            
                "go to the door up":
                    play sound "snd/door-locked.ogg"
                    m "The door is closed."
                    jump prisonflats
            
                "go to the door right":
                    play sound "snd/door-locked.ogg"
                    m "The door is closed."
                    jump prisonflats
                "back":
                    jump prisonflats
        
        
        "go to the space suits":
            if inv_ssuit == False:
                menu:
                    "take a space suit":
                        $ inv_ssuit = True
                        play sound "snd/collect.ogg"
                        with flash
                        "You got a space suit!"
                        jump prisonflats
                    "back":
                        jump prisonflats
            else:
                m "I've got a space suit already, I don't need another one."
                jump prisonflats
                    
        "go out":
            show posanim at Position(xpos = 80, ypos=210, xanchor=0.5, yanchor=0.5):
            play sound "snd/door-open.ogg"
            jump prisonlift
