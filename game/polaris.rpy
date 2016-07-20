# polaris

label polaris:
    hide ship
    hide ship1
    hide ship2
    hide ship3
    hide starssmall
    hide starsmid
    hide starsbig
    hide text
    hide prisonpic
    hide planetpic
    hide sunpic
    hide aldabranpic
    hide meteoroidpic
    hide stationpic
    hide matarholo
    hide polarisholo
    hide betriaholo
    hide distance
    hide suntxt
    hide plxytxt
    hide prisontxt
    hide matartxt
    hide betriatxt
    hide aldabrantxt
    hide isstxt
    hide polaristxt
    hide meteoroidtxt

    
    show bg polaris behind posanim at topleft
    
    show screen inventory
    
    #show ionet sender
    if io_pol == True:
        show ionetsender at Position(xpos = 70 , ypos=377, xanchor=0.5, yanchor=0.5)
    
    
    menu:
        "copy IO-net on this computer" if inv_ionet == True and io_pol == False:
            call ioinstall from _call_ioinstall_4

        
        "IO-net info"if io_pol == True:
            call ioinfo from _call_ioinfo_4
            
        "look at the Hologram":
            #play sound "snd/scan.ogg"
            hide ionetsender
            jump solarsystem


        "use the Terminal":
            $ term1 = "help"
            $ backto = "polaris"
            hide ionetsender
            jump terminal
        
        "look at the Computers" if inv_ionet == False:
            m "They are turned off."
            jump polaris
            
        "go out":
            hide ionetsender
            jump spaceport
    
    jump polaris
            

        


