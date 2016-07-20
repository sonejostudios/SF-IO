# BETRIA FIELDS

label bfieldsstart:

    hide posanim
    
    
    show bg betriafields at topleft
    
    show posanim:
        xanchor 0.5
        yanchor 0.5
        xpos 300 ypos 285
    

    
    jump bfields
    
    
        
label bfields:
    
    $ musicplaying = renpy.music.get_playing(channel='music')
    if musicplaying != "snd/nature.ogg":
        play music "snd/nature.ogg" loop fadein 0.5
    
    #jump bfields
    
    show posanim:
        xanchor 0.5
        yanchor 0.5
        linear 1 xpos 300 ypos 285
        
    hide bfrobot
    
    
    if fieldstoggle == False:
        $ fieldstoggle = True
        show fieldsj f1 at Position(xpos = 300, ypos=285, xanchor=0.5, yanchor=0.5) behind bg, bf
    
    else:
        $ fieldstoggle = False
        show fieldsj f2 at Position(xpos = 300, ypos=285, xanchor=0.5, yanchor=0.5) behind bg, bf
    
    
    
# terrain
    # train station
    if desertx == 5 and deserty == 0:
        show bf station at Position(xpos = 300, ypos=120, xanchor=0.5, yanchor=0.5) behind bg
        m "At some places they are still some vegetables left... Maybe I could collect them?"
    # rails without train station    
    if desertx != 5 and deserty == 0:
        show bf rails at Position(xpos = 300, ypos=120, xanchor=0.5, yanchor=0.5) behind bg

    # mask down
    if deserty == 10:
        show bfhide2 at Position(xpos = 300, ypos=285, xanchor=0.5, yanchor=0.0) behind bg, bf

    # hide masks    
    if deserty >= 1 and deserty <= 9:
        hide bf
        hide bfhide2
        hide bfhouse
        
    # mask west        
    if desertx == 0:
        show bfhide at Position(xpos = 300, ypos=285, xanchor=1.0, yanchor=0.5) behind bg, bf
    
    # mask east
    if desertx == 10:
        show bfhide at Position(xpos = 300, ypos=285, xanchor=0.0, yanchor=0.5) behind bg, bf
    
    # hide masks
    if desertx >= 1 and desertx <= 9:
        hide bfhide
        hide bfhouse
        
    
    # fields house
    if desertx == 0 and deserty == 0:
        show bfhouse at Position(xpos = 270, ypos=285, xanchor=1.0, yanchor=0.5)
        
        
        
    #robot 1
    if desertx == 0 and deserty == 1 and "r1" in frobots and robotquest != 2:
        show bfrobot at Position(ypos=370, xanchor=0.5, yanchor=0.5) behind bg:
            xpos 400
            linear 3 xpos 520
            linear 3 xpos 400
            repeat
    
    #robot 2        
    if desertx == 6 and deserty == 2 and "r2" in frobots and robotquest != 2:
        show bfrobot at Position(ypos=370, xanchor=0.5, yanchor=0.5) behind bg:
            xpos 400
            linear 3 xpos 520
            linear 3 xpos 400
            repeat
    
    #robot 3        
    if desertx == 5 and deserty == 5 and "r3" in frobots and robotquest != 2:
        show bfrobot at Position(ypos=370, xanchor=0.5, yanchor=0.5) behind bg:
            xpos 400
            linear 3 xpos 520
            linear 3 xpos 400
            repeat

    #robot 4
    if desertx == 9 and deserty == 9 and "r4" in frobots and robotquest != 2:
        show bfrobot at Position(ypos=370, xanchor=0.5, yanchor=0.5) behind bg:
            xpos 400
            linear 3 xpos 520
            linear 3 xpos 400
            repeat
    
    

    #hide text
    #show text "x[desertx], y[deserty]" at left
    
    # food random number
    $ ffood = renpy.random.randint(1, 5)
    
    
    #robot1
    if desertx == 0 and deserty == 1 and "r1" in frobots and robotquest == 1:
        menu:
            "send Robot 1 to field engineer":
                call robotback from _call_robotback
                $ frobots.remove("r1")
                play sound "snd/connected.ogg"
                jump bfieldsmenu
    #robot2            
    if desertx == 6 and deserty == 2 and "r2" in frobots and robotquest == 1:
        menu:
            "send Robot 2 to field engineer":
                call robotback from _call_robotback_1
                $ frobots.remove("r2")
                play sound "snd/connected.ogg"
                jump bfieldsmenu
    #robot3            
    if desertx == 5 and deserty == 5 and "r3" in frobots and robotquest == 1 :
        menu:
            "send Robot 3 to field engineer":
                call robotback from _call_robotback_2
                $ frobots.remove("r3")
                play sound "snd/connected.ogg"
                jump bfieldsmenu
    #robot4
    if desertx == 9 and deserty == 9 and "r4" in frobots and robotquest == 1:
        menu:
            "send Robot 4 to field engineer":
                call robotback from _call_robotback_3
                $ frobots.remove("r4")
                play sound "snd/connected.ogg"
                jump bfieldsmenu
                
    
    
    
    # Food collect
    if ffood == 1 and robotquest != 1:
        m "There are some vegetables left on the field!"
        jump bfieldsmenu
        
            
            
    
    jump bfieldsmenu



label bfieldsmenu:    
    #"[frobots]"
    #"[ffood]"
    
    menu:
        #"send Robot 1 to field engineer" if desertx == 0 and deserty == 1 and "r1" in frobots and robotquest == 1:
            #call robotback
            #$ frobots.remove("r1")
            #jump bfieldsmenu
        
        #"send Robot 2 to field engineer" if desertx == 6 and deserty == 2 and "r2" in frobots and robotquest == 1:
            #call robotback
            #$ frobots.remove("r2")
            #jump bfieldsmenu

        #"send Robot 3 to field engineer" if desertx == 5 and deserty == 5 and "r3" in frobots and robotquest == 1 :
            #call robotback
            #$ frobots.remove("r3")
            #jump bfieldsmenu

        #"send Robot 4 to field engineer" if desertx == 9 and deserty == 9 and "r4" in frobots and robotquest == 1:
            #call robotback
            #$ frobots.remove("r4")
            #jump bfieldsmenu
            
        "robots info" if robotquest == 1:
            "Robots in fields: [frobots]\nRobot 1: C0, R1.\nRobot 2: C6, R2.\nRobot 3: C5, R5.\nRobot 4: C9, R9."
            jump bfieldsmenu
            
            
        "collect vegetables" if ffood == 1 and robotquest != 1:
            play sound "snd/dig.ogg"
            pause 1.0
            $ food += 1
            play sound "snd/collect.ogg"
            with flash
            $ ffood = renpy.random.randint(1, 5)
            "You got 1kg of food!\n\nYour food balance is [food] kg."
            jump bfieldsmenu
            
            
        
        "read signs":
            if desertx == 0 and deserty == 0:
                "You are at Field Junction: Column [desertx], Row [deserty].\n\nTo the Train Station:\nFollow the rails to the east."
                jump bfieldsmenu
            if desertx == 5 and deserty == 0:
                "You are at Field Junction: Column [desertx], Row [deserty].\n\nTo the Fields House:\nFollow the rails to the west."
                jump bfieldsmenu
            else:
                "You are at Field Junction: Column [desertx], Row [deserty]."
                jump bfieldsmenu
                
                
                
        "go into the fields house" if desertx == 0 and deserty == 0:
            hide bfhouse
            show posanim at Position(xpos = 450, ypos=285, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            jump bfieldshouse
        
        "go to train station" if desertx == 5 and deserty == 0:
            $ trainfrom = 0
            show posanim at Position(xpos = 210, ypos=385, xanchor=0.5, yanchor=0.5)
            play sound "snd/door-open.ogg"
            hide bf
            hide bfhide2
            hide fieldsj
            jump btrainstation


        
        "go north"if deserty >= 1:
                show posanim:
                    linear 1 ypos 165
                pause 1
                
                $ deserty -= 1
                
                show posanim:
                    ypos 400
                pass
            
       
        "go west" if desertx >= 1:
                show posanim:
                    linear 1 xpos 50
                pause 1
                
                $ desertx -= 1
                
                show posanim:
                    xpos 540
                pass
            
       
        "go east"if desertx <= 9:
                show posanim:
                    linear 1 xpos 540
                pause 1
                
                $ desertx += 1
                
                show posanim:
                    xpos 50
                pass
            
        
        "go south" if deserty <= 9:
                show posanim:
                    linear 1 ypos 400
                pause 1
                
                $ deserty += 1
                
                show posanim:
                    ypos 165
                pass
            
    jump bfields
    
    
    
    
label bfieldshouse:
    show bg bfieldshouse
    
    #play music "snd/spaceship-station.ogg" loop fadein 0.5
    
    "There is not that much, only a field engineer working at some control machines."
    
    menu:
        #"reset robot quest":
            #$ robotquest = 0
            #$ frobots = ["r1","r2","r3","r4"]
            #"robotquest value : [robotquest]"
            #"frobots : [frobots]"
            #pass
            
        "talk to the field engineer" if robotquest != 2:
            if frobots == [] and robotquest == 1:
                menu:
                    "I sent all robots back to you":
                        bfhguy "Nice! I see they are on their way back to me."
                        bfhguy "Here are 250c for you job. Thank you!"
                        $ cash += 250
                        play sound "snd/collect.ogg"
                        with flash
                        $ robotquest = 2
                        "You got 250c!"
                        jump bfieldshouse
            
            if frobots != [] and robotquest == 1:
                bfhguy "Where are my robots? Please find them!"
                pass
            
            else:
                m "Hi!"
                bfhguy "Hey, how are you?"
                bfhguy "Could you do me a favor?"
                bfhguy "I lost the remote control of my 4 harvesting robots. Could you please find them on the fields and send them to me?"
                
                menu:
    
                    
                    "yes, sure" if frobots != []:
                        bfhguy "Thanks!" 
                        $ robotquest = 1
                        bfhguy "Here are some informations about them."
                        bfhguy "I'll wait for you here, come back when you are done."
                        bfhguy "Good luck!"
                        pass
                    "no" if frobots != []:
                        bfhguy "Okay. Ask me again if you change your mind. Bye!"
                        pass
                    
                    
        "talk to the satisfied field engineer" if robotquest == 2 and inv_blakekey == False:
            bfhguy "Thank you for the great job!"
            bfhguy "I've got another job for you if you like."
            m "Okay, go on!"
            bfhguy "The fields irrigation system doesn't work properly."
            bfhguy "Could you please go to the lake in the mountains and activate the pump? Maybe that will help."
            bfhguy "Here is the key of the control cabin."
            $ inv_blakekey = True
            play sound "snd/collect.ogg"
            with flash
            "You got the lake control cabin key!"
            bfhguy "Good luck!"
            pass
        
        "talk to the very satisfied field engineer" if betrialake == 2:
            bfhguy "Thank you for everything!"
            bfhguy "That's for you for the help."
            $ cash += 100
            play sound "snd/collect.ogg"
            with flash
            $ betrialake = 3
            "You got 100c!"

            pass
            
        "talk to the very very satisfied field engineer" if betrialake == 3:
            bfhguy "Thank you for everything!"
            bfhguy "Bye!"
            pass
            
        "look under the control machines" if cash < 10:
            m "Oh there is 10c!"
            m "I will need that money if I want to buy a train ticket to travel back. I take it."
            $ cash += 10
            play sound "snd/collect.ogg"
            with flash
            "You got 10c!"
            pass
                
            
            
        "go out":
            $ desertx = 0
            $ deserty = 0
            play sound "snd/door-open.ogg"
            jump bfieldsstart
    
    jump bfieldshouse
    


# anime robot back
label robotback:
        show bfrobot:
            rotate 45
            linear 4 xpos 0 ypos 0
            
        return
    
