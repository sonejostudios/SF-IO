# ISS
label iss:
    hide ship
    hide ship1
    hide ship2
    hide ship3
    hide text
    
    show bg isshall
    show posanim at Position(xpos = 300, ypos=275, xanchor=0.5, yanchor=0.5)
    
    menu:
        #"get 500c":
            #$ cash += 500
            #jump iss
            
        "go to the Spaceport":
            play sound "snd/door-open.ogg"
            jump spaceport
        "go to the Spaceship Factory":
            play sound "snd/door-open.ogg"
            play audio "snd/scan.ogg"
            $ stationshipnr = 1
            jump stationshop
        "go to the Warehouse":
            play sound "snd/door-open.ogg"
            jump isswarehouse
        "go down":
            play sound "snd/door-open.ogg"
            jump issexpo
            

# ISS Spaceship Factory
label stationshop:
    hide posanim
    hide ship
    hide ship1
    hide ship2
    hide ship3
    hide posanim

    show bg stationshop behind text
    
 
    if stationshipnr == 4:
        $ stationshipnr = 1
        jump stationshop
    
    if stationshipnr == 0:
        $ stationshipnr = 3
        jump stationshop


    show text (_("{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}")) at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
       

    #ship 1
    if stationshipnr == 1:
        show ship spaceship1  at Position(xpos = 300, ypos=0.5, xanchor=0.5, yanchor=0.5) behind bg:
            xpos -200
            easein 1 xpos 300
        pause 1
        "Ship [stationshipnr] \nModel: SD-02\nPrice: 400c"


    #ship 2   
    if stationshipnr == 2:
        show ship spaceship2  at Position(xpos = 300, ypos=0.5, xanchor=0.5, yanchor=0.5) behind bg:
            xpos -200
            easein 1 xpos 300
        pause 1
        "Ship [stationshipnr] \nModel: IO-1\nPrice: 500c"
        
    #ship 3    
    if stationshipnr == 3:
        show ship spaceship3  at Position(xpos = 300, ypos=0.5, xanchor=0.5, yanchor=0.5) behind bg:
            xpos -200
            easein 1 xpos 300
        pause 1
        "Ship [stationshipnr] \nModel: SF-3\nPrice: 4000c"



    
    menu:
        "buy SD-02" if stationshipnr == 1 and cash >= 400 and spaceshipnr != 1:
            $ cash -= 400
            $ spaceshipnr = 1
            play sound "snd/collect.ogg"
            with flash
            "Congratulations, you've got a new Space Ship!"
            jump spaceport
            
        "buy IO-1" if stationshipnr == 2 and cash >= 500 and spaceshipnr != 2:
            $ cash -= 500
            $ spaceshipnr = 2
            play sound "snd/collect.ogg"
            with flash
            "Congratulations, you've got a new Space Ship!"
            jump spaceport
            
        "buy SF-3" if stationshipnr == 3 and cash >= 4000 and spaceshipnr != 3:
            $ cash -= 4000
            $ spaceshipnr = 3
            play sound "snd/collect.ogg"
            with flash
            "Congratulations, you've got a new Space Ship!"
            jump spaceport
            

        
        "show next ship":
            show ship behind bg:
                xpos 300
                easeout 1 xpos 750
            #play sound "snd/beep.ogg"
            pause 1
            play sound "snd/scan.ogg"
            $ stationshipnr += 1
            jump stationshop
        
        
        "go out":
            play sound "snd/door-open.ogg"
            jump iss
            
            

            
            

# ISS WAREHOUSE
label isswarehouse:
    hide posanim
    show bg isswh behind text

    show text (_("{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}")) at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
    
    menu:
        "buy":
            jump isswarehousebuy
        "sell":
            jump isswarehousesell
        "go out":
            hide text
            #show posanim at Position(xpos = 80, ypos=260, xanchor=0.5, yanchor=0.5):
            play sound "snd/door-open.ogg"
            jump iss
            
            
            
            
label isswarehousebuy:
            show text (_("{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}")) at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
           
            menu:
                "buy rocks" if cash >= 20:
                    play sound "snd/collect.ogg"
                    $ cash -= 20 
                    $ rocks += 1
                    jump isswarehousebuy
            
                "buy steel" if cash >= 70:
                    play sound "snd/collect.ogg"
                    $ cash -= 70 
                    $ steel += 1
                    jump isswarehousebuy
        
                "buy alu" if cash >= 80:
                    play sound "snd/collect.ogg"
                    $ cash -= 80 
                    $ alu += 1
                    jump isswarehousebuy
        
                "buy textile" if cash >= 40:
                    play sound "snd/collect.ogg"
                    $ cash -= 40 
                    $ textile += 1
                    jump isswarehousebuy
        
                "buy food" if cash >= 35 :
                    play sound "snd/collect.ogg"
                    $ cash -= 35 
                    $ food += 1
                    jump isswarehousebuy
                    
                "back":
                    jump isswarehouse
                
label isswarehousesell:
            show text (_("{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}")) at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
   
            menu:
                "sell rocks" if rocks >= 1:
                    play sound "snd/collect.ogg"
                    $ cash += 13 
                    $ rocks -= 1
                    jump isswarehousesell
            
                "sell steel" if steel >= 1:
                    play sound "snd/collect.ogg"
                    $ cash += 60 
                    $ steel -= 1
                    jump isswarehousesell
        
                "sell alu" if alu >= 1:
                    play sound "snd/collect.ogg"
                    $ cash += 70 
                    $ alu -= 1
                    jump isswarehousesell
        
                "sell textile" if textile >= 1:
                    play sound "snd/collect.ogg"
                    $ cash += 30 
                    $ textile -= 1
                    jump isswarehousesell
        
                "sell food" if food >= 1 :
                    play sound "snd/collect.ogg"
                    $ cash += 35 
                    $ food -= 1
                    jump isswarehousesell

                "back":
                    jump isswarehouse



# ISS EXPO
label issexpo:
    
    show bg issexpo at topleft
    
    show posanim at Position(xpos = 300, ypos=175, xanchor=0.5, yanchor=0.5)
    
    m "This look like an exposition where I can get some interesting information!"
    
    menu:
        "talk to Matar Mines worker":
            issmatar "Hello. How can I help?"
            
            menu:
                "Here is the original matar stone!" if inv_mstone == True and issmatarquest != 2:
                    issmatar "Let me see..."
                    $ inv_mstone = False
                    issmatar "Ohh very nice one!!"
                    issmatar "Thank you very much."
                    issmatar "Here is your money for the job. Thank you!"
                    $ issmatarquest = 2
                    play sound "snd/collect.ogg"
                    $ cash += 150
                    with flash
                    "You got 150c !"
                    pass
                    
                
                "I'd like to visit the mines on Matar":
                    issmatar "Sure!"
                    issmatar "I will announce you, then you can go there anytime."
                    issmatar "Just give your visitor number before landing."
                    issmatar "Your visitor number is: M1234"
                    
                    $ matarlanding = True
                    
                    m "Okay, thanks you!"
                    pass
                    
                    
                "Do you have a job for me?":
                    issmatar "Yes, could be... let me think..."
                    issmatar "...I'm looking for someone who can bring me an original matar stone for the shop." 
                    issmatar "I have to stay here and can't leave. Would you like to do that??"
                    menu:
                        "Yes" if issmatarquest != 2:
                            issmatar "Nice. I'll wait for you here. Good luck!"
                            $ issmatarquest = 1
                            pass
                            
                        "No, sorry":   
                            issmatar "Okay, no problem. See you."
                            pass
            pass
        
        
        "look at the Betria Colony office" if firstticket == 0:
            m "There is nobody."
            m "But a huge poster about the Betria Colony!"
            "BETRIA and its Colony\n\nDo you want to have nice holidays?\nCome to the Betria Planet!\nYou will discover many amazing things! The Colony, the Fields, the Mountains, the Sea, the Train, and many more!\nTo come to us just find the fastest way to x402 y242, or just locate betria in the Terminal!\nIf you need a ticket to travel around betria, just ask us.\nSee you soon on Betria!"
            pass

            
        "talk to the Betria Colony people" if firstticket >= 1:            
            issbetria "Hello! How can I help you?"
            if inv_ticket == False:
                m "I would like to visit the Betria Fields. Can I buy a train ticket?"
                issbetria "Sure! I's only 50c special offer for the Betria Fields!"
                issbetria "Do you want to buy it?"
                menu:
                    "yes please!" if cash >= 50:
                        $ cash -= 50
                        $ inv_ticket = True
                        $ ticketdir = 1
                        $ ticketdest = 1
                        $ firstticket = 2
                        play sound "snd/collect.ogg"
                        with flash
                        "You got a train ticket to Betria's Fields!"
                        pass
                    "no, thanks.":
                        pass
                pass
            
            else:
                m"I'm fine, thanks."
                pass
        
        "go out":
            play sound "snd/door-open.ogg"
            jump iss
    
    jump issexpo
    
    
    
    
