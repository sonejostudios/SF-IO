# METEOROID
label meteoroidlift:
    hide ship
    hide ship1
    hide ship2
    hide ship3
    hide text
    
    show bg mlift
    
    menu:
        "00":
            if mine_lift is not 0:
                play sound "snd/lift.ogg"
                show posanim:
                    linear 2 ypos 170
                $ mine_lift = 0
                pause 2.5
            play sound "snd/door-open.ogg"
            jump spaceport
        "-01":
            if mine_lift is not -1:
                play sound "snd/lift.ogg"
                show posanim:
                    linear 2 ypos 380 
                $ mine_lift = -1
                pause 2.5
            show posanim at Position(xpos = 80, ypos=270, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            jump premmine
            
            
            
            
label premmine:


    if mineexploded == False:
        show bg mmine
        "Here is the entrance of the mine. There is an important sign on the wall with a text..."
        jump mmine
        
    if mineexploded == True:
        show bg mmine2
        "The explosion created a hole. Behind the hole is a steel door."
        jump mmine
    
label mmine: 
    
    menu:

        "dig" if inv_digtool == True: 
            
            $ minerandom = renpy.random.randint(1, 15)
            
            play sound "snd/dig.ogg"
            
            if minerandom == 2:
                play sound "snd/dig.ogg"
                pause 1.0
                play sound "snd/collect.ogg"
                $ rocks += 1
                with flash
                "You've got 1 kg of rocks!\nYour rock balance is now [rocks] kg."
            
            if minerandom == 3:
                play sound "snd/dig.ogg"
                pause 1.0
                play sound "snd/collect.ogg"
                $ steel += 1
                with flash
                "You've got 1 kg of steel!\nYour steel balance is now [steel] kg."
            
            if minerandom == 4:
                play sound "snd/dig.ogg"
                pause 1.0
                play sound "snd/collect.ogg"
                $ alu += 1
                with flash
                "You've got 1 kg of aluminium!\nYour aluminium balance is now [alu] kg."
         
            else:
                pause 1.0
                m "Nothing there... maybe if I try again?"
            jump mmine
            
        
        "use the dynamite" if inv_dynamite == True and mineexploded == False:
            play sound "snd/ignition.ogg"
            $ inv_dynamite = False
            show text "{size=40}3{/size}" at Position(xpos= 268, ypos=305)
            pause 1
            show text "{size=40}2{/size}" at Position(xpos= 268, ypos=305)
            pause 1
            show text "{size=40}1{/size}" at Position(xpos= 268, ypos=305)
            pause 1
            hide text
            play sound "snd/boom.ogg"
            $ mineexploded = True
            with flash
            jump premmine
            
                
                
        "read sign":
            "This mine is closed. Entrance forbidden!\nThis is the property of MATAR MINES. For any questions you can visit us in our head quarters on Matar (planet) at x256 y200 or just locate matar in a Terminal."
            jump mmine
        
        "try digging" if inv_digtool == False:
            m "I don't have any tool to dig there..."
            jump mmine
            
        "go through the steel door" if mineexploded == True:
            show posanim at Position(xpos = 290 , ypos=175, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            jump msbase
                
        "go out":
            $ minerandom = 1
            show posanim at Position(xpos = 80, ypos=380, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            jump meteoroidlift
            
            
label msbase:
    show bg msbase
    
    #show ionet sender
    if io_meteoroid == True:
        show ionetsender at Position(xpos = 135 , ypos=377, xanchor=0.5, yanchor=0.5)
    
    
    menu:
        "copy IO-net on this computer" if inv_ionet == True and io_meteoroid == False:
            call ioinstall from _call_ioinstall

        
        "IO-net info"if io_meteoroid == True:
            call ioinfo from _call_ioinfo
        
        "go out":
            hide ionetsender
            show posanim at Position(xpos = 290 , ypos=375, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            jump premmine
            
    jump msbase
            
    


            

