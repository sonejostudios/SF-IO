#dealerview
label dealerview:
    if spaceshipdir == 1:
        show ship spaceship3u as dealership:
            xanchor 0.5
            yanchor 0.5
            xpos 0.3
            ypos 1.5
            easein 4 ypos 0.5


    if spaceshipdir == 2:
        show ship spaceship3 as dealership:
            xanchor 0.5
            yanchor 0.5
            xpos -0.5
            ypos 0.2
            easein 4 xpos 0.5

        
    if spaceshipdir == 3:
        show ship spaceship3d as dealership:
            xanchor 0.5
            yanchor 0.5
            xpos 0.3
            ypos -0.5
            easein 4 ypos 0.5

        
    if spaceshipdir == 4:
        show ship spaceship3l as dealership:
            xanchor 0.5
            yanchor 0.5
            xpos 1.5
            ypos 0.2
            easein 4 xpos 0.5

    play music "snd/spaceship-hum.ogg" loop fadein 4.0

    pause 4    
    d "Are you sure you want to deal with me?"
    menu:
        "I'm from the Rebel Alliance!" if rebel == True and inv_ionet == False:
            call iogive from _call_iogive
            $ coox = 280
            $ cooy = 120
            pass
            
        "yes!":
            if rebel == False:
                d "I don't trust you for serious business, but you can have a look to my wares."
            else: 
                d "Well, have a look!"
            
            call dwarehouse from _call_dwarehouse
            
            $ coox = 280
            $ cooy = 120
            $ spaceshippos = 0
            pass
            
        "no, thanks":

            $ coox = 280
            $ cooy = 120
            $ spaceshippos = 0
            
            stop music fadeout 1.0
            pause 1
            play music "snd/spaceship.ogg" loop fadein 1.0
            
            pass   

    
    if spaceshipdir == 1:
        show ship spaceship3u as dealership:
            xanchor 0.5
            yanchor 0.5
            xpos 0.3
            ypos 0.5
            ease 4 ypos -1.5


    if spaceshipdir == 2:
        show ship spaceship3 as dealership:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.2
            ease 4 xpos 1.5


        
    if spaceshipdir == 3:
        show ship spaceship3d as dealership:
            xanchor 0.5
            yanchor 0.5
            xpos 0.3
            ypos 0.5
            ease 4 ypos 1.5


        
    if spaceshipdir == 4:
        show ship spaceship3l as dealership:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.2
            ease 4 xpos -0.5
    pause 4
    #hide ship
    hide dealership
    jump spaceshipmenu


label iogive:
    d "I know you were coming. Finally you are here!"
    d "Here, I give you a copy of the IO-net software."
    
    play sound "snd/collect.ogg"
    
    $ inv_ionet = True
    with flash
    "You got the IO-net software!"
    
    d "Good luck with your job!"
    
    stop music fadeout 1.0
    pause 1
    play music "snd/spaceship.ogg" loop fadein 1.0


    return
    
    
    
    

# DEALER WAREHOUSE
label dwarehouse:
    hide posanim
    show bg dealerwh behind text at topleft

    show text (_("{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}")) at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
    
    menu:
        "buy":
            jump dwarehousebuy
        "sell":
            jump dwarehousesell
        "go out":
            hide text
            hide bg
            
            stop music fadeout 1.0
            pause 1
            play music "snd/spaceship.ogg" loop fadein 1.0

            return
            
            
            
            
label dwarehousebuy:
            show text (_("{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}")) at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
           
            menu:
                "buy rocks" if cash >= 15:
                    play sound "snd/collect.ogg"
                    $ cash -= 15 
                    $ rocks += 1
                    jump dwarehousebuy
            
                "buy steel" if cash >= 35:
                    play sound "snd/collect.ogg"
                    $ cash -= 35 
                    $ steel += 1
                    jump dwarehousebuy
        
                "buy alu" if cash >= 45:
                    play sound "snd/collect.ogg"
                    $ cash -= 45 
                    $ alu += 1
                    jump dwarehousebuy
        
                "buy textile" if cash >= 25:
                    play sound "snd/collect.ogg"
                    $ cash -= 25
                    $ textile += 1
                    jump dwarehousebuy
        
                "buy food" if cash >= 30 :
                    play sound "snd/collect.ogg"
                    $ cash -= 30 
                    $ food += 1
                    jump dwarehousebuy
                    
                "back":
                    jump dwarehouse
                
label dwarehousesell:
            show text (_("{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}")) at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
   
            menu:
                "sell rocks" if rocks >= 1:
                    play sound "snd/collect.ogg"
                    $ cash += 10 
                    $ rocks -= 1
                    jump dwarehousesell
            
                "sell steel" if steel >= 1:
                    play sound "snd/collect.ogg"
                    $ cash += 25 
                    $ steel -= 1
                    jump dwarehousesell
        
                "sell alu" if alu >= 1:
                    play sound "snd/collect.ogg"
                    $ cash += 35 
                    $ alu -= 1
                    jump dwarehousesell
        
                "sell textile" if textile >= 1:
                    play sound "snd/collect.ogg"
                    $ cash += 15 
                    $ textile -= 1
                    jump dwarehousesell
        
                "sell food" if food >= 1 :
                    play sound "snd/collect.ogg"
                    $ cash += 25 
                    $ food -= 1
                    jump dwarehousesell

                "back":
                    jump dwarehouse
