# BETRIA MAIN TRAIN STATION            
label btrainstation:
    hide ship1
    hide ship2
    hide ship3
    hide railsl
    hide railsr
    
    
    show bgcolor
    
    if trainstation == 0:
        show bg btrainstation
    
    if trainstation == 1:
        show bg btrainstation1
    
    if trainstation == 2:
        show bg btrainstation2
    
    if trainstation == 3:
        show bg btrainstation3
    
    
    
    #show text "trainstation [trainstation], ticketdest [ticketdest]"
    
    if trainfrom == 0:
        show rails at Position(xpos = 0, ypos=210, xanchor=0.0, yanchor=0.5) behind bg, train
        show train at Position(xpos = 295, ypos=210, xanchor=0.5, yanchor=0.5) behind bg
        
    if trainfrom == 1:
        hide posanim
        
        show rails at Position(xpos = 0, ypos=210, xanchor=0.0, yanchor=0.5) behind bg, train
        
        show train at Position(ypos=210, xanchor=0.5, yanchor=0.5) behind bg:
            xpos 1500
            easein 4 xpos 295
        pause 4
        show posanim at Position(xpos = 180, ypos=290, xanchor=0.5, yanchor=0.5)
        
    if trainfrom == 2:
        hide posanim
        
        show rails at Position(xpos = 0, ypos=210, xanchor=0.0, yanchor=0.5) behind bg, train
        
        show train at Position(ypos=210, xanchor=0.5, yanchor=0.5) behind bg:
            xpos -1000
            easein 4 xpos 295
        pause 4
        show posanim at Position(xpos = 180, ypos=290, xanchor=0.5, yanchor=0.5)
        
    jump trainstationmenu
    
    
#train station menu

label trainstationmenu:
    menu:
        "take the train" :
            if inv_ticket == True:
                if ticketdir == 1: 
                    $ trainfrom = 1
                    hide posanim
                    show train at Position(xpos = 295, ypos=210, xanchor=0.5, yanchor=0.5) behind bg:
                        easeout 4 xpos -1000
                    pause 4
                    jump btrain
    
                if ticketdir == 2:
                    $ trainfrom = 2
                    hide posanim
                    show train at Position(xpos = 295, ypos=210, xanchor=0.5, yanchor=0.5) behind bg:
                        easeout 4 xpos 2000
                    pause 4
                    jump btrain
            else:
                m "The train's door won't open without a valid ticket."
                jump trainstationmenu
                
                
#buy a ticket
        "buy a ticket" if cash >= 10 and inv_ticket == False and firstticket != 2:
            "Ticket Office closed for Holydays. Please try another ticket reseller like Betria Colony Shop on the Industrial Space Station. Use the phone on the wall to call them."
            menu:
                "use the phone":
                    issbetria "Yes?"
                    m "Hello. Just let you know I'm coming to buy a train ticket."
                    issbetria "Oh no problem. I'll wait for you there."
                    $ firstticket = 1
                "back":
                    pass
            jump trainstationmenu
            
        
        "buy a ticket" if cash >= 10 and inv_ticket == False and firstticket == 2:
            traintickets "Where do you want to go? For the next strain station it's 10c please."
            
            if trainstation == 0:
                menu:
                    "to Fields Station":
                        $ cash -= 10
                        $ trainfrom = 1
                        $ ticketdir = 1
                        $ inv_ticket = True
                        $ ticketdest = 1
                        with flash
                        "You got a train ticket to Fields Station!"
                        
                    "to Coast Station":
                        $ cash -= 10
                        $ trainfrom = 2
                        $ ticketdir = 2
                        $ inv_ticket = True
                        $ ticketdest = 3
                        with flash
                        "You got a train ticket to Coast Station!"
                        
                    "back":
                        pass
                jump trainstationmenu
                
            if trainstation == 1:
                menu:
                    "to Mountains Station":
                        $ cash -= 10
                        $ trainfrom = 1
                        $ ticketdir = 1
                        $ inv_ticket = True
                        $ ticketdest = 2
                        with flash
                        "You got a train ticket to Mountains Station!"
                        
                    "to Main Station":
                        $ cash -= 10
                        $ trainfrom = 2
                        $ ticketdir = 2
                        $ inv_ticket = True
                        $ ticketdest = 0
                        with flash
                        "You got a train ticket to Main Station!"
                        
                    "back":
                        pass
                jump trainstationmenu
                
            if trainstation == 2:
                menu:
                    "to Fields Station":
                        $ cash -= 10
                        $ trainfrom = 2
                        $ ticketdir = 2
                        $ inv_ticket = True
                        $ ticketdest = 1
                        with flash
                        "You got a train ticket to Fields Station!"
                    "back":
                        pass
                jump trainstationmenu
                
            if trainstation == 3:
                menu:
                    "to Main Station":
                        $ cash -= 10
                        $ trainfrom = 1
                        $ ticketdir = 1
                        $ inv_ticket = True
                        $ ticketdest = 0
                        with flash
                        "You got a train ticket to Main Station!"
                    "back":
                        pass
                jump trainstationmenu
                        
            jump trainstationmenu
        
        "go out":
            
            if trainstation == 0:
                $ trainfrom = 0
                show posanim at Position(xpos = 150, ypos=225, xanchor=0.5, yanchor=0.5)
                hide train
                hide rails
                jump betria
            
            if trainstation == 1: # fields
                hide train
                hide rails
                
                $ desertx = 5
                $ deserty = 0
                
                jump bfieldsstart
                
            if trainstation == 2: # mountains
                hide train
                hide rails
                show posanim at Position(xpos = 238, ypos=310, xanchor=0.5, yanchor=0.5)
                jump betriamount1
                
            if trainstation == 3: # coast
                hide train
                hide rails
                show posanim at Position(xpos = 345, ypos=310, xanchor=0.5, yanchor=0.5)
                jump betriacoast
                
            else:
                jump trainstationmenu



#IN TRAIN            
label btrain:
    hide rails

    show bgcolor
    
    $ inv_ticket = False
    

    if trainfrom == 1:
        show railsl at Position(xpos = 0, ypos=285, xanchor=0.0, yanchor=0.5) behind bg, train
    if trainfrom == 2:
        show railsr at Position(xpos = 0, ypos=285, xanchor=0.0, yanchor=0.5) behind bg, train
    
    
    
    if trainw == 0:
        show train at Position(xpos = 985, ypos=285, xanchor=0.5, yanchor=0.5) behind bg:
            ypos 285
            linear 1 ypos 287
            linear 1 ypos 283
            repeat
                            
    if trainw == 1:
        show train at Position(xpos = 880, ypos=285, xanchor=0.5, yanchor=0.5) behind bg:
            ypos 285
            linear 1 ypos 287
            linear 1 ypos 283
            repeat
    if trainw == 2:
        show train at Position(xpos = 560, ypos=285, xanchor=0.5, yanchor=0.5) behind bg:   
            ypos 285
            linear 1 ypos 287
            linear 1 ypos 283
            repeat
    if trainw == 3:
        show train at Position(xpos = 450, ypos=285, xanchor=0.5, yanchor=0.5) behind bg:
            ypos 285
            linear 1 ypos 287
            linear 1 ypos 283
            repeat
    if trainw == 4:
        show train at Position(xpos = 130, ypos=285, xanchor=0.5, yanchor=0.5) behind bg:
            ypos 285
            linear 1 ypos 287
            linear 1 ypos 283
            repeat


    if trainw == 5:
        show train at Position(xpos = 20, ypos=285, xanchor=0.5, yanchor=0.5) behind bg:
            ypos 285
            linear 1 ypos 287
            linear 1 ypos 283
            repeat
        if trainguythere == True:
            trainguy "Pssst..."    
            menu:
                "yes":
                    trainguy "My friend from Xy told me you are coming."
                    trainguy "I will tell you something..."
                    trainguy "But it's not safe here. Follow me."
                    $ trainw = 7
                    pass
                "sorry I don't want to talk":
                    $ trainw = 4
                    pass
            jump btrain
        else:
            pass

        
    if trainw == 6:
        show train at Position(xpos = -300, ypos=285, xanchor=0.5, yanchor=0.5) behind bg:
            ypos 285
            linear 1 ypos 287
            linear 1 ypos 283
            repeat

        
    if trainw == 7:
        show train at Position(xpos = -410, ypos=285, xanchor=0.5, yanchor=0.5) behind bg:
            ypos 285
            linear 1 ypos 287
            linear 1 ypos 283
            repeat
            
        
        if rebel == True:
            trainguy "Welcome back."
        
        if rebel == False:
            trainguy "Are you looking for a serious job?"    
            m "yes"
            trainguy "My friend from Xy told me I can trust you."
            trainguy "We are the Rebel Alliance, we are a secret underground movement against the corrupt governement."
            trainguy "I'm sure you've heard about IO-net Network already."
            trainguy "We were the people behind the IO-net and the new free energy."
            trainguy "As the governement tried to catch us we copied all the information in the IO-net."
            trainguy "Now we want to rebuild it and get access to the new free energy before the governement."
            trainguy "And stop them doing their crazy control dictature!"
        
            trainguy "Do you want to join us?"
            menu:
                "yes":
                    $ rebel = True
                    with flash
                    "You joined the Rebel Alliance!"
                    trainguy "So I'll tell you your job in this case."
                    pass
                    
                "no":
                    $ trainw = 6
                    jump btrain
        
        
        
        trainguy "We need to re-install IO-net in this solar system."
        trainguy "Please find each big computer and copy the IO-net sofware on it. It will create a IO-node."
        trainguy "When we have enought nodes for a basic network, we can start it!"
        trainguy "You will need the IO-net Software for that. There is only one copy left."
        trainguy "Go to the space dealer at x280, y120. I will tell him you are coming. He will give you the copy."
        trainguy "Good luck!"


        $ trainw = 6
        jump btrain
    

    
    show bg btrain
    
    #show text " wagon [trainw]" at truecenter
    
    
    show posanim at Position(xpos = 290, ypos=285, xanchor=0.5, yanchor=0.5):
        ypos 285
        linear 1 ypos 287
        linear 1 ypos 283
        repeat
    
    menu:
        "go left" if trainw != 0:
            if trainw == 1:
                m "It's closed."
            else:
                $ trainw -= 1
            jump btrain
        
        "go right" if trainw != 7:
            if trainw == 6:
                m "It's closed."
            else:
                $ trainw += 1
            jump btrain
        
        "wait":
            $ trainw = 3
            $ trainstation = ticketdest
            pause 1.5
            m "I thing we are coming soon..."
            hide railsl
            hide train
            
            jump btrainstation


