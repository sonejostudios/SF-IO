
#SPACESHIP RACE

label racestart:
    hide bg sunorbit

    #Directions
    if spaceshipdir == 1:
        show starssmall u2d behind ship
        show starsmid u2d behind ship
        show starsbig u2d behind ship
        
        show ship spaceship2u as capship at Position(xpos = 0.3, ypos=240, xanchor=0.5, yanchor=0.5)
        
        if spaceshipnr == 1:
            show ship spaceship1u at truecenter
        if spaceshipnr == 2:
            show ship spaceship2u at truecenter
        if spaceshipnr == 3:
            show ship spaceship3u at truecenter

    
    if spaceshipdir == 2:
        show starssmall rl behind ship
        show starsmid rl behind ship
        show starsbig rl behind ship
        
        show ship spaceship2 as capship at Position(xpos = 400, ypos=100, xanchor=0.5, yanchor=0.5)
        
        if spaceshipnr == 1:
            show ship spaceship1 at truecenter
        if spaceshipnr == 2:
            show ship spaceship2 at truecenter
        if spaceshipnr == 3:
            show ship spaceship3 at truecenter
 
            
    if spaceshipdir == 3:
        show starssmall d2u behind ship
        show starsmid d2u behind ship
        show starsbig d2u behind ship
        
        show ship spaceship2d as capship at Position(xpos = 0.3, ypos=240, xanchor=0.5, yanchor=0.5)
        
        if spaceshipnr == 1:
            show ship spaceship1d at truecenter
        if spaceshipnr == 2:
            show ship spaceship2d at truecenter
        if spaceshipnr == 3:
            show ship spaceship3d at truecenter
    
    
    if spaceshipdir == 4:
        show starssmall lr behind ship
        show starsmid lr behind ship
        show starsbig lr behind ship
        
        show ship spaceship2l as capship at Position(xpos = 400, ypos=100, xanchor=0.5, yanchor=0.5)
        
        if spaceshipnr == 1:
            show ship spaceship1l at truecenter
        if spaceshipnr == 2:
            show ship spaceship2l at truecenter
        if spaceshipnr == 3:
            show ship spaceship3l at truecenter
            
    
    stop music fadeout 1.0
    capitain "Are you ready?"
    play music "snd/spaceship-hum.ogg" loop fadein 1.0
    
    menu:
        #"get ship 1":
            #$ spaceshipnr = 1
            #jump racestart
        #"get ship 2":
           #$ spaceshipnr = 2
            #jump racestart
        #"get ship 3":
            #$ spaceshipnr = 3
            #jump racestart
            
        "Let's go!":
            play sound "snd/race.ogg" 
            
            show text "{size=50}3{/size}" at Position(xpos = 0.5, ypos=0.9, xanchor=0.5, yanchor=0.5)
            pause 1
            show text "{size=50}2{/size}" at Position(xpos = 0.5, ypos=0.9, xanchor=0.5, yanchor=0.5)
            pause 1
            show text "{size=50}1{/size}" at Position(xpos = 0.5, ypos=0.9, xanchor=0.5, yanchor=0.5)
            pause 1
            show text (_("{size=50}GO!{/size}")) at Position(xpos = 0.5, ypos=0.9, xanchor=0.5, yanchor=0.5)
            jump race
        
        "No sorry...":
            stop music fadeout 1
            capitain "Haha I knew that..."

            play music "snd/spaceship.ogg" loop fadein 1
            hide capship
            jump orbitview
            
    



#RACE !!!
label race:
    hide posanim
    hide targetpos
    hide bg
    

    play sound "snd/hyperspace.ogg"
    


    #Directions stars and spaceship
    if spaceshipdir == 1:
        show starssmall hsu2d behind ship
        show starsmid hsu2d behind ship
        show starsbig hsu2d behind ship
        
        if spaceshipnr == 1:
            show ship spaceship1u at truecenter
            with flash
            show ship spaceship2u as capship:
                xpos 0.3
                ypos 240
                easeout 5 ypos -200
            
            
        if spaceshipnr == 2:
            show ship spaceship2u at truecenter
            with flash
            show ship spaceship2u as capship:
                xpos 0.3
                ypos 240
                easeout 5 ypos -200
        
        if spaceshipnr == 3:
            show ship spaceship3u at truecenter
            with flash
            show ship spaceship2u as capship:
                xpos 0.3
                ypos 240
                easeout 5 ypos 1000
   
    
    if spaceshipdir == 2:
        show starssmall hsrl behind ship
        show starsmid hsrl behind ship
        show starsbig hsrl behind ship
        
        if spaceshipnr == 1:
            show ship spaceship1 at truecenter
            with flash
            show ship spaceship2 as capship:
                xpos 400
                ypos 100
                easeout 5 xpos 1000
                
        if spaceshipnr == 2:
            show ship spaceship2 at truecenter
            with flash
            show ship spaceship2 as capship:
                xpos 400
                ypos 100
                easeout 5 xpos 1000
                
        if spaceshipnr == 3:
            show ship spaceship3 at truecenter
            with flash
            show ship spaceship2 as capship:
                xpos 400
                ypos 100
                easeout 5 xpos -200
        
        
    if spaceshipdir == 3:
        show starssmall hsd2u behind ship
        show starsmid hsd2u behind ship 
        show starsbig hsd2u behind ship 
        
        if spaceshipnr == 1:
            show ship spaceship1d at truecenter
            with flash
            show ship spaceship2d as capship:
                xpos 0.3
                ypos 240
                easeout 5 ypos 1000
                
        if spaceshipnr == 2:
            show ship spaceship2d at truecenter
            with flash
            show ship spaceship2d as capship:
                xpos 0.3
                ypos 240
                easeout 5 ypos 1000
                
        if spaceshipnr == 3:
            show ship spaceship3d at truecenter
            with flash
            show ship spaceship2d as capship:
                xpos 0.3
                ypos 240
                easeout 5 ypos -200
    
    
    if spaceshipdir == 4:
        show starssmall hslr behind ship 
        show starsmid hslr behind ship 
        show starsbig hslr behind ship
        
        if spaceshipnr == 1:
            show ship spaceship1l at truecenter
            with flash
            show ship spaceship2l as capship:
                xpos 400
                ypos 100
                easeout 5 xpos -200
                
        if spaceshipnr == 2:
            show ship spaceship2l at truecenter
            with flash
            show ship spaceship2l as capship:
                xpos 400
                ypos 100
                easeout 5 xpos -200
                
        if spaceshipnr == 3:
            show ship spaceship3l at truecenter
            with flash
            show ship spaceship2l as capship:
                xpos 400
                ypos 100
                easeout 5 xpos 1000

    
    pause 0.5
    hide text
    with dissolve

    
    pause 5
    play sound "snd/scan.ogg"
    play music "snd/spaceship.ogg" loop fadein 0.5
    
    with flash
    
    if spaceshipnr == 1:
        play sound "snd/beep.ogg" 
        capitain "Hahaha you lost the race! I knew that!"
        pass
        
    if spaceshipnr == 2:
        play sound "snd/beep.ogg" 
        capitain "Hahaha you lost the race! I knew that!"
        pass
        
    if spaceshipnr == 3:
        $ sunrace = 2
        play sound "snd/connected.ogg" 
        capitain "You won man! Well done. Let's meet again in Betria at the Colony Bar."
        m "Okay, see you!"
        pass
        
    hide starssmall hs
    hide starsmid hs
    hide starsbig hs
    hide bg
    hide ship
    hide capship
    
    jump spaceship
