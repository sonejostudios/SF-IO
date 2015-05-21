# Betria Colony

label betria:
    hide ship
    hide ship1
    hide ship2
    hide ship3
    hide text
    
    show screen inventory
    
    show bg betria
    #show posanim at Position(xpos = 300, ypos=275, xanchor=0.5, yanchor=0.5):
    
    
    if spaceshipnr == 1:
            show ship1 fscaled at Position(xpos = 347, ypos=225, xanchor=0.5, yanchor=0.5):
    if spaceshipnr == 2:
            show ship2 fscaled at Position(xpos = 347, ypos=225, xanchor=0.5, yanchor=0.5):
    if spaceshipnr == 3:
            show ship3 fscaled at Position(xpos = 347, ypos=225, xanchor=0.5, yanchor=0.5):
            
    
    menu:
        "go to the spaceport":
            jump spaceport
        
        "go to the train station":
            $ trainfrom = 0
            show posanim at Position(xpos = 210, ypos=385, xanchor=0.5, yanchor=0.5)
            jump btrainstation
            
        #"get 100c":
            #$ cash = 100
            #jump betria
            
        "go down":
            show posanim at Position(xpos = 444, ypos=180, xanchor=0.5, yanchor=0.5)
            jump betria1
            
        

label betria1:
    hide ship1
    hide ship2
    hide ship3

    show bg betria1

    
    menu:
        "go up":
            show posanim at Position(xpos = 470, ypos=385, xanchor=0.5, yanchor=0.5)
            jump betria
            
        "go left":
            show posanim at Position(xpos = 520, ypos=215, xanchor=0.5, yanchor=0.5)
            jump betria3
            
        "go down left":
            show posanim at Position(xpos = 140, ypos=185, xanchor=0.5, yanchor=0.5)
            jump betria2b
        
        
        "go down right":
            show posanim at Position(xpos = 448, ypos=185, xanchor=0.5, yanchor=0.5)
            jump betria2
                    



label betria2: #bar place

    show bg betria2
    
    menu:

        "go up":
            show posanim at Position(xpos = 444, ypos=390, xanchor=0.5, yanchor=0.5)
            jump betria1
        "go left":
            show posanim at Position(xpos = 525, ypos=332, xanchor=0.5, yanchor=0.5)
            jump betria4
            
        "go to the bar":
            show posanim at Position(xpos = 295, ypos=185, xanchor=0.5, yanchor=0.5)
            jump betriabar

            


label betria2b:

    show bg betria2
    
    menu:
        "enter into the building":
            m "It's closed."
            jump betria2b
        "go back":
            show posanim at Position(xpos = 120, ypos=390, xanchor=0.5, yanchor=0.5)
            jump betria1
            
            
label betria3:

    show bg betria3
    
    menu:
        "go right":
            show posanim at Position(xpos = 65, ypos=220, xanchor=0.5, yanchor=0.5)
            jump betria1
        "go down":
            show posanim at Position(xpos = 445, ypos=180, xanchor=0.5, yanchor=0.5)
            jump betria4
            
            
label betria4: #warehouse place

    show bg betria4
    
    menu:
            
        "go up":
            show posanim at Position(xpos = 445, ypos=385, xanchor=0.5, yanchor=0.5)
            jump betria3
        
        "go right":
            show posanim at Position(xpos = 65, ypos=320, xanchor=0.5, yanchor=0.5)
            jump betria2
        "go to the warehouse":
            jump bwarehouse
            


            
#BETRIA COLONY BAR 
label betriabar: #bar

    show bg betriabar
    
    "There a group of people at the tables and an old guy at the bar. He looks like he was a cap'tain. At the end of the room at a table there is a guy counting stones."
    
    menu:
        "talk to the people at the tables":
            m "They don't want to talk to me..."
            menu:
                "take a seat at table":
                    show posanim at Position(xpos = 156, ypos=250, xanchor=0.5, yanchor=0.5)
                    "You sit down at a table."
                    jump barattable
                "back":
                    pass
            jump betriabar
            
        
        "talk to the old cap'tain again"if sunrace == 3:
            show posanim at Position(xpos = 425, ypos=250, xanchor=0.5, yanchor=0.5)
            capitain "Well done man. Good luck with the map."
            capitain "Bye!"
            jump betriabar
            
        "talk to the old cap'tain about the race you won" if sunrace == 2:
            show posanim at Position(xpos = 425, ypos=250, xanchor=0.5, yanchor=0.5)
            m "Hey Cap'tain. I won the race! What about the map you talked about?"
            capitain "Yes it's true, you won our race. Well done!"
            capitain "I'm so happy I had a lot of fun. Thank you!"
            capitain "Here as I told you I' tell you an old betria sailor secret."
            capitain "Near the Betria Coast there are some islands. There is a secret base with a door protected by a password key."
            capitain "I figure it out long time ago."
            capitain "The password key is: 2277"
            $ sunrace = 3
            
            jump betriabar
            
            
        "talk to the old cap'tain" if sunrace <= 1:
            show posanim at Position(xpos = 425, ypos=250, xanchor=0.5, yanchor=0.5)
            capitain "No drink, no talk."
            menu:
                "Okay I'll buy you a drink." if cash >= 1:
                    $ cash -= 1
                    with flash
                    capitain "Thank you!"
                    capitain "My name is Henk. I worked as a captain. I was a lot of time on the sea."
                    capitain "The governement said it's not allowed anymore to work there."
                    capitain "Now I'm retired and it's so boring..."
                    capitain "I bought a space ship and I want some action!"
                    capitain "I'm sure your spaceship is so slow you couldn't win a race against me..."
                    capitain "Could you?"
                    menu:
                        "Okay, let's go!":
                            capitain "Nice!"
                            capitain "Let's meet in orbit of the Sun at x300 y300. And be ready hahaha!! "
                            capitain "If you win, I'll tell you a betria sailor secret."
                            m "Okay..."
                            m "And if I loose?"
                            capitain "Haha if if you loose? Hmmm good question. I'll think about that. I just want to have fun anyway."
                            $ sunrace = 1
                            capitain "Let's meet at the Sun!"
                            pass
                            
                            
                        "No I'm not interested.":
                            pass
                    
                    pass
                    
                "No":
                    pass
            jump betriabar
        
        "talk to the stones guy":
            stonesguy "I'm a stone collector. I'm just missing an Original Matar Stone. If you bring me one, I'll will give you a good price."
            stonesguy "Do you have one for me?"
            
            menu:
                "Yes, take it" if inv_mstone == True:
                    m "Here is an Original Matar Stone."
                    stonesguy "Oh it is amazing!"
                    stonesguy "Here I give you a good price for it. 100c!"
                    $ inv_mstone = False
                    $ cash += 100
                    with flash
                    "You got 100c!"
                    stonesguy "Thank you!"
                    m "Bye!"
                    jump betriabar
                "No":
                    jump betriabar

                
                
            
            
        "go out":
            show posanim at Position(xpos = 289, ypos=315, xanchor=0.5, yanchor=0.5)
            jump betria2
            

        
label barattable:
    menu:
        "order a drink" if cash >= 1 and bardrink < 3:
            m "Barman, a drink please!"
            barman "Yes, sure. It's 1c!"
            "The barman brings you a drink."
            $ cash -= 1
            with flash
            m "Thanks!"
            $ bardrink += 1
            barman "You drink balance is [bardrink]."
            barman "Do you want another one?"
            m "Maybe later, thanks!"
            "The barman is going back to the bar."
            "The guys are still talking some weird stuff."
            pass
            
        "another drink please!" if cash >= 1 and bardrink == 3:
            "The barman is coming."
            barman "Your drink balance ist [bardrink] and I'm not allowed to give you more, sorry!"
            m "What??"
            barman "That's the governement, sorry..."
            barman "They are so crazy!"
            m "Yes, I totally agree!"
            "The barman is going back to the bar."
            m "..."
            $ bardrink = 4
            "The guys look scared about something, they talk really quiet..."
            tableguy "... cave... coast.... somewhere... money... secret... wooden box..."
            m "Hmmm... interesting information..."
            pass
            
        "stand up":
            m "Okay nothing interesting."
            $ bardrink = 0
            jump betriabar
            
    jump barattable
            


label betriamount1: # train station

    show bg betriamount1
    
    menu:
        "go to train station":
            $ trainfrom = 0
            show posanim at Position(xpos = 210, ypos=380, xanchor=0.5, yanchor=0.5)
            jump btrainstation
        
        "go to the village":
            show posanim at Position(xpos = 235, ypos=185, xanchor=0.5, yanchor=0.5)
            jump betriamount2
            
            
label betriamount2: #village

    show bg betriamount2
    
    "There are some people around the village."
    
    menu:
        "talk to the construction guy":
            m "Hi!"
            menu:
                "Here is some dynamite" if inv_dynamite == True:
                    consguy "Oh nice! So I could finish the road tomorrow."
                    consguy "Here are 150c for the job. Thanks!"
                    $ cash += 150
                    $ inv_dynamite = False
                    with flash
                    "You got 150c!"
                    jump betriamount2
                    
                "What are you doing here?":
                    consguy "I'm working on the road construction site. We want to build a new road to the mountains, the fields and the city."
                    consguy "A huge stone fell on the new road and we need to move it..."
                    consguy "Maybe with some dynamite... Are you looking for a job? Please bring me dynamite, I'll give you 200c!"
                    m "Okay I'll do that if I find some."
                    m "See you!"
                    jump betriamount2
    
                

        "talk to the guy at the house" if inv_seamap == False:
            mountguy "Hello. Are you interested in antique stuff?"
            m "Maybe. Let me see."
            mountguy "I found this old sea map a couple of days ago."
            mountguy " Do you need it?"
            show seamap at topleft
            with dissolve
            pause 1
            hide seamap
            with dissolve
            m "Wow, it's very interesting! Yes, maybe I could need it."
            
            mountguy "Okay, I would give it to you for 200c only. Special price!"
            m "What?"
            menu:
                "okay, go for 200c" if cash >= 200:
                     $ inv_seamap = True
                     $ cash -= 200
                     with flash
                     "You got a sea map!"
                     jump betriamount2
                
                "no, thanks":
                    mountguy "Okay. Bye!"
                    jump betriamount2
                    
        "talk to the guy at the house again" if inv_seamap == True:
            mountguy "Hello. That was a good deal with you! Anytime again!"
            m "Yes. I'm happy with the sea map. Thanks!"
            jump betriamount2        
            
        
                    
            
        "go up":
            show posanim at Position(xpos = 248, ypos=385, xanchor=0.5, yanchor=0.5)
            jump betriamount1
            
        "go down":
            show posanim at Position(xpos = 230, ypos=185, xanchor=0.5, yanchor=0.5)
            jump betriamount3
            
            

label betriamount3: #"stairs" to lake

    show bg betriamount3
    
    if cash < 10:
        m "Oh there is 10c!"
        m "I will need that money if I want to buy a train ticket. I should take it."

        
    
    menu:
        "take the 10c" if cash < 10:
            $ cash += 10
            with flash
            "You got 10c!"
            jump betriamount3
            
        "go to the village":
            show posanim at Position(xpos = 265, ypos=385, xanchor=0.5, yanchor=0.5)
            jump betriamount2
            
        "go to the lake":
            show posanim at Position(xpos = 70, ypos=292, xanchor=0.5, yanchor=0.5)
            jump betriamountlake
            
            
label betriamountlake: #lake

    show bg betriamountlake
    
    if betrialake == 0:
        show betrialake at Position(xpos = 340, ypos=280, xanchor=0.5, yanchor=0.5)
    
    if betrialake == 1:    
            show betrialake at Position(xpos = 340, ypos=280, xanchor=0.5, yanchor=0.5):
                linear 5 zoom 0.3
            pause 5
            $ betrialake = 2
            m "Aha! There is a secret door in the lake..."
            jump betriamountlake
    
    if betrialake == 2:
            show betrialake at Position(xpos = 340, ypos=280, xanchor=0.5, yanchor=0.5):
                zoom 0.3
    
    
    menu:
        "open secret door and enter" if betrialake >= 2:
            hide betrialake
            show posanim at Position(xpos = 290 , ypos=175, xanchor=0.5, yanchor=0.5)
            jump bsbase
            
        
        "go to control cabin":
            if inv_blakekey == True:
                hide betrialake
                show posanim at Position(xpos = 295, ypos=230, xanchor=0.5, yanchor=0.5)
                jump betrialakecontrol
            else:
                m "It's closed. There is a plate with some information."
                "Property of the Fields Company. No entry. For any questions please visit us at the Fields House.\nHow to go there? We are at Column 0 Row 0 in the Fields. Or just go out the Fields Train Station and follow the rails to the west to the Fields House."
            jump betriamountlake
                
            
        "go out":
            hide betrialake
            show posanim at Position(xpos = 520, ypos=295, xanchor=0.5, yanchor=0.5)
            jump betriamount3



label betrialakecontrol: #lake control cabin

    show bg betrialakecontrol
    
    menu:
        "start pumps"if betrialake == 0:
            $ betrialake = 1
            show posanim at Position(xpos = 111, ypos=315, xanchor=0.5, yanchor=0.5)
            jump betriamountlake
        
        "go out":
            show posanim at Position(xpos = 111, ypos=315, xanchor=0.5, yanchor=0.5)
            jump betriamountlake
            
            
label bsbase:
    show bg betrialakesbase
    
    #show ionet sender
    if io_blake == True:
        show ionetsender at Position(xpos = 135 , ypos=377, xanchor=0.5, yanchor=0.5)
    
    
    menu:
        "copy IO-net on this computer" if inv_ionet == True and io_blake == False:
            call ioinstall

        
        "IO-net info" if io_blake == True:
            call ioinfo
        
        "go out":
            hide ionetsender
            show posanim at Position(xpos = 243 , ypos=303, xanchor=0.5, yanchor=0.5)
            jump betriamountlake
            
    jump bsbase
    
 
    
# BETRIA WAREHOUSE
label bwarehouse:
    hide posanim
    show bg betriawh behind text

    show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
    
    menu:
        "buy":
            jump bwarehousebuy
        "sell":
            jump bwarehousesell
        "go out":
            hide text
            show posanim at Position(xpos = 455, ypos=330, xanchor=0.5, yanchor=0.5):
            jump betria4
            
            
            
            
label bwarehousebuy:
            show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
           
            menu:
                "buy rocks" if cash >= 20:
                    $ cash -= 20 
                    $ rocks += 1
                    jump bwarehousebuy
            
                "buy steel" if cash >= 40:
                    $ cash -= 40 
                    $ steel += 1
                    jump bwarehousebuy
        
                "buy alu" if cash >= 50:
                    $ cash -= 50 
                    $ alu += 1
                    jump bwarehousebuy
        
                "buy textile" if cash >= 30:
                    $ cash -= 30 
                    $ textile += 1
                    jump bwarehousebuy
        
                "buy food" if cash >= 15 :  
                    $ cash -= 15 
                    $ food += 1
                    jump bwarehousebuy
                    
                "back":
                    jump bwarehouse
                
label bwarehousesell:
            show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
   
            menu:
                "sell rocks" if rocks >= 1:
                    $ cash += 15 
                    $ rocks -= 1
                    jump bwarehousesell
            
                "sell steel" if steel >= 1:
                    $ cash += 30 
                    $ steel -= 1
                    jump bwarehousesell
        
                "sell alu" if alu >= 1:
                    $ cash += 40 
                    $ alu -= 1
                    jump bwarehousesell
        
                "sell textile" if textile >= 1:
                    $ cash += 20 
                    $ textile -= 1
                    jump bwarehousesell
        
                "sell food" if food >= 1 :  
                    $ cash += 10 
                    $ food -= 1
                    jump bwarehousesell

                "back":
                    jump bwarehouse
            


label betriacoast:
    show bgcolor behind bg
    hide waves

    show bg betriacoast at topleft
    
    menu:
        "go to train sation":
            $ trainfrom = 0
            show posanim at Position(xpos = 210, ypos=380, xanchor=0.5, yanchor=0.5)
            jump btrainstation
        
        "go to the beach":
            show posanim at Position(xpos = 65, ypos=287, xanchor=0.5, yanchor=0.5)
            jump betriacoast1
            
            
label betriacoast1: # beach
    show bgcolor behind bg
    
    show waves at Position(ypos=285, xanchor=0.5, yanchor=0.5) behind bg, boat, bs:
        xpos 300
        linear 1 xpos 305
        linear 1 xpos 300
        repeat

    show bg betriacoast1 at topleft
    
    show bs coast1 at Position(xpos = 300, ypos=285, xanchor=1.0, yanchor=0.5) behind bg, boat
    
    if cash < 10:
        m "Oh there is 10c!"
        m "I will need that money if I want to buy a train ticket. I should take it."

    menu:
        "take the 10c" if cash < 10:
            $ cash += 10
            with flash
            "You got 10c!"
            jump betriacoast1
            
        "try the boat" if inv_seamap == False:
            m "I won't try without a proper sea map."
            jump betriacoast1
            
        "use the boat" if inv_seamap == True:
            $ desertx = 0
            $ deserty = 5
            jump bseastart
        
            
        "go to train station":
            hide bs 
            hide waves
            show posanim at Position(xpos = 525, ypos=380, xanchor=0.5, yanchor=0.5)
            jump betriacoast

    

label betriacave:
    show bg betriascave at topleft
    
    #show posanim at Position(xpos = 300, ypos=285, xanchor=0.5, yanchor=0.5)
    show posanim at Position(xpos = 435, ypos=290, xanchor=0.5, yanchor=0.5)
    
    
    menu:
        "go out the boat":
            show posanim at Position(xpos = 300, ypos=285, xanchor=0.5, yanchor=0.5)
            
            if treasure == False:
                m "There is a big wooden box close to the wall..."
            else:
                m "Although this cave is quite nice I have nothing to do there anymore."
            
            menu:
                "open the box" if treasure == False:
                    show posanim at Position(xpos = 178, ypos=260, xanchor=0.5, yanchor=0.5)
                    m "Oh that's a treasure! I'm rich!!"
                    $ cash +=500
                    with flash
                    $ treasure = True
                    "You got 500c!"
                    pass
            pass
            
    
        "go out":
            show boat behind bg:
                xanchor 0.5
                yanchor 0.5
                rotate 90
                xpos 300 ypos 285
                
                
            $ desertx = 0
            $ deserty = 10
            jump bseastart
            
            
    menu:
        "go back to the boat":
            jump betriacave
            
            
label betriaislands:
    show bg betriaislands at topleft
    hide islands
    hide boat
    
    $ onislands = True
    
    menu:
                
        "enter the barn":
            "Please enter the password key:"
            menu:
                "2277" if sunrace == 3:
                    show posanim at Position(xpos = 140 , ypos=265, xanchor=0.5, yanchor=0.5)
                    jump bislandsbase
                "I don't know...":
                    jump betriaislands

            
        "use the boat":
            $ onislands = False
            $ desertx = 10
            $ deserty = 3
            jump bseastart
            
    
    
    
    
label bislandsbase:
    show bg bislandsbase at topleft
    
    #show ionet sender
    if io_bislands == True:
        show ionetsender at Position(xpos = 135 , ypos=377, xanchor=0.5, yanchor=0.5)
    
    
    menu:
        "copy IO-net on this computer" if inv_ionet == True and io_bislands == False:
            call ioinstall

        
        "IO-net info" if io_bislands == True:
            call ioinfo
        
        "go out":
            hide ionetsender
            show posanim at Position(xpos = 340 , ypos=310, xanchor=0.5, yanchor=0.5)
            jump betriaislands
            
    jump bislandsbase
    

