
#SOLAR SYSTEM VIEW
label solarsystem:
    hide planetpic
    hide prisonpic
    hide starssmall
    hide starsmid
    hide starsbig
    hide bg
    hide posanim
    hide text
    
    hide screen inventory
    
    
    #show bg solarsystem
    
    show bgcolor
    
    show starssmall nomove
    show starsmid nomove
    show starsbig nomove
    
    

    
#sun    
    show sunpic:
        anchor (0.5,0.5)
        align (0.5,0.5)
        zoom 0.3
        
    image suntxt = Text("{size=16}sun 333{/size}")
    
    show suntxt:
        anchor (-20,0.5)
        pos (0.5,0.5)
       

#planet xy
    show planetpic :
        anchor (0.5,0.5)
        around (0.5, 0.5)
        radius 0.05
        angle 0
        zoom 0.2
        linear 40 clockwise circles 1
        repeat
        
    image plxytxt = Text("{size=16}xy{/size}")

    show plxytxt :
        anchor (-15,0.5)
        around (0.5, 0.5)
        radius 0.05
        angle 0
        linear 40 clockwise circles 1
        repeat
        
        
        
#prison
    show prisonpic :
        anchor (0.5,0.5)
        around (0.5, 0.5)
        radius 0.1
        angle 180
        zoom 0.2
        linear 20 clockwise circles 1
        repeat

    image prisontxt = Text("{size=16}prison{/size}")

    show prisontxt :
        anchor (-15,0.5)
        around (0.5, 0.5)
        radius 0.1
        angle 180
        linear 20 clockwise circles 1
        repeat
        

#planet matar     
    image matarholo = "pics/planetpic2.png"
    
    show matarholo:
        anchor (0.5,0.5)
        around (0.5, 0.5)
        radius 0.15
        angle 90
        zoom 0.3
        rotate 90
        linear 30 clockwise circles 1
        repeat

    image matartxt = Text("{size=16}matar{/size}")

    show matartxt :
        anchor (-15,0.5)
        around (0.5, 0.5)
        radius 0.15
        angle 90
        linear 30 clockwise circles 1
        repeat
        

#planet meteoroid    
    show meteoroidpic :
        anchor (0.5,0.5)
        around (0.5, 0.5)
        radius 0.18
        angle 360
        zoom 0.2
        linear 23 clockwise circles 1
        repeat

    image meteoroidtxt = Text("{size=16}meteoroid 539{/size}")

    show meteoroidtxt :
        anchor (-15,0.5)
        around (0.5, 0.5)
        radius 0.18
        angle 360
        linear 23 clockwise circles 1
        repeat



        

#planet aldabran       
    show aldabranpic :
        anchor (0.5,0.5)
        around (0.5, 0.5)
        radius 0.2
        angle 115
        zoom 0.2
        linear 45 clockwise circles 1
        repeat

    image aldabrantxt = Text("{size=16}aldabran{/size}")

    show aldabrantxt :
        anchor (-20,0.5)
        around (0.5, 0.5)
        radius 0.2
        angle 115
        linear 45 clockwise circles 1
        repeat


#planet betria    
    image betriaholo = "pics/planetpic.png"
    
    show betriaholo :
        anchor (0.5,0.5)
        around (0.5, 0.5)
        radius 0.22
        angle 200
        zoom 0.2
        linear 35 clockwise circles 1
        repeat

    image betriatxt = Text("{size=16}betria{/size}")

    show betriatxt :
        anchor (-15,0.5)
        around (0.5, 0.5)
        radius 0.22
        angle 200
        linear 35 clockwise circles 1
        repeat
        
#planet iss
    show stationpic :
        anchor (0.5,0.5)
        around (0.5, 0.5)
        radius 0.3
        angle 45
        zoom 0.2
        rotate 20
        linear 30 clockwise circles 1
        repeat

    image isstxt = Text("{size=16}iss{/size}")

    show isstxt :
        anchor (-15,0.5)
        around (0.5, 0.5)
        radius 0.3
        angle 45
        linear 30 clockwise circles 1
        repeat
        

#planet polaris    
    image polarisholo = "pics/planet3pic.png"
    
    show polarisholo :
        anchor (0.5,0.5)
        around (0.5, 0.5)
        radius 0.4
        angle 250
        zoom 0.3
        rotate 20
        linear 55 clockwise circles 1
        repeat

    image polaristxt = Text("{size=16}polaris{/size}")

    show polaristxt :
        anchor (-30,0.5)
        around (0.5, 0.5)
        radius 0.4
        angle 250
        linear 55 clockwise circles 1
        repeat





label hologrammenu:
    
    menu:
        "Distances Map":
            jump distancemap
            
        
        "back":
            show posanim at Position(xpos = 360, ypos=230, xanchor=0.5, yanchor=0.5):
            jump polaris


label distancemap:
    hide prisonpic
    hide planetpic
    hide sunpic
    hide aldabranpic
    hide meteoroidpic
    hide stationpic
    hide matarholo
    hide polarisholo
    hide betriaholo
    hide suntxt
    hide plxytxt
    hide prisontxt
    hide matartxt
    hide betriatxt
    hide aldabrantxt
    hide isstxt
    hide polaristxt
    hide meteoroidtxt
    hide distance
    
    hide starssmall
    hide starsmid
    hide starsbig
    
    image distance = "pics/circles.png"
    
    show distance at truecenter
    
    menu:
        "Show Coordinates Data Bank":
            "prison: x320 y370 \nxy: x293 y331 \nsun: x300 y300 \naldabran: x184 y253 \nmeteoroid: x210 y375 \nbetria: x402 y242 \nmatar: x256 y200 \npolaris: x180 y470 \niss: x341 y143"
            menu:
                "Copy Coordinates Data Bank to Terminal":
                    $ coorcopy = 1
                    "Coordinates copied!"
                    "To access them, juste type locate planets in a terminal."
                "back":
                    pass
            jump distancemap
        
        "back":
            hide distance
            jump solarsystem
    
    
    
    
    

