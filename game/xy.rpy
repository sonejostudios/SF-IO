# Planet XY
label xy:
    hide ship
    hide ship1
    hide ship2
    hide ship3
    hide text
    
    show screen inventory
    
    show bg xyentrance
    #show posanim at Position(xpos = 300, ypos=275, xanchor=0.5, yanchor=0.5):
    
    menu:
            
        "use the Terminal":
            $ term1 = "help"
            $ backto = "xy"
            jump terminal
        
        "go to the Bar":
            show posanim at Position(xpos = 297, ypos=380, xanchor=0.5, yanchor=0.5)
            jump xybar
        
        "go to the Warehouse":
            jump xywarehouse
        
        "go to the Lift":
            show posanim at Position(xpos = 0.23, ypos=0.62, xanchor=0.5, yanchor=0.5)
            m "It's out of order."
            jump xy

        #"get 100 c":
        #    $ cash += 100
        #    jump xy
        #"get 0 c":
        #    $ cash = 0
        #    jump xy
            
        "go out":
            jump spaceport


#XY BAR
label xybar:
    show bg xybar
    
    if xybarmanaway == False:
        "There is the barman, a weird guy at the bar and some people sitting at the tables."
    
    if xybarmanaway == True:
        "The barman is away."
    
    
    menu:
    
        "go to the room behind the bar" if xybarmanaway == True:
            show posanim at Position(xpos = 400, ypos=280, xanchor=0.5, yanchor=0.5)
            jump xykitchen
        
      
        "talk to":
            menu:
                "talk to the Barman" if xybarmanaway == False:
                    show posanim at Position(xpos = 0.12, ypos=330, xanchor=0.5, yanchor=0.5)
           
                    jump xybarman
                                   
                "talk to the Weird Guy":
                    jump xybarguy

                "talk to the people at the tables":
                    m "They don't want to talk to me."
                    jump xybar
                "back":
                    jump xybar
          
        "go to the wc":
            m "It's out of order."
            jump xybar
        "go to the Special Room":
            
            if xybarroom == True:
                $ xybarmanaway = False
                jump xyspecialroom
            else:
                barman "You are not allowed to enter there!"
                jump xybar
        "go out":
            $ xybarmanaway = False
            show posanim at Position(xpos = 140, ypos=290, xanchor=0.5, yanchor=0.5):
            jump xy


#xy barman
label xybarman:
    barman "Hey! If you like a drink, it's only 1 cash."
    menu:
        "give the food to the Barman" if food >= 1:
            $ food -= 1
            $ xybarroom = True
            barman "Thank you!"
            $ barmanquest = 2
            barman "If you like you are now allowed to enter into the Special Room... "
            jump xybar
        
        "yes please!":
            if cash == 0:
                barman "Oh oh... you don't have money I see? Do you need a small job?"
                menu:
                    "yes, tell me":
                        barman "Okay. Go and bring me 1 kg of food. Maybe at the Warehouse in the front of the Bar, if not, just have a look at the Prison Warehouse, sometimes they are cheaper. It's at x320, y370 (or just locate prison with a Terminal). Here are 31c for you."
                        $ cash += 31
                        with flash
                        "You've got 31c!"
                        if barmanquest == 0:
                            $ barmanquest = 1
                        barman "Now bring me that food!"
                        jump xybar
                    
                    "are you crazy? no way!":
                        jump xybar
            
            if cash >= 0:
                $ cash -= 1
                with flash
                m "Nice one, thanks!"
                jump xybarman
                
        "no thanks":
            jump xybar
        
        "what about the room behind you?":
            barman "That's private! Nothing interesting for you."
            jump xybar


label xybarguy:
    barguy "please buy me a drink..."
    menu:
        "I copied the hologram data already." if coorcopy == 1:
            barguy "Ah really?"
            m "Yes, you can access it easily with terminal under the command locate planets."
            barguy "Very good. Just wait a minute I'll have a look. "
            "The weird guy is going out the bar."
            "The weird guy comes back."
            barguy "Well done! Here is a little gift for you."
            
            $ cash += 200
            with flash
            "You've got 200c!"
            
            barguy "Thank you!"            
            $ coorcopy = 2
            
            jump bgstory
            
        
        "yes, sure!" if cash >= 1 and barmanquest != 1:
            $ cash -= 1
            with flash
            barguy "Thanks!"
            if coorcopy == 0:
                barguy "I will tell you a secret..."
                barguy "I worked as a scientist at the Research Station on Polaris. We had a research program about our solar system." 
                barguy "There is a huge hologram with all the planets we colonized in the past. It could be interesting for you if you plan to travel around."
                barguy "If you want to go there, just type locate polaris in a terminal to get the coordinates."
                barguy "You need to know, there are really strong winds and you will need a good space ship to land on the spaceport."
                barguy "If you go there, please copy all the hologram data to the terminal. So all my researches would be accessible again."
                barguy "See you!"
            
            jump xybar
            
        "not yet":
            jump xybar
        
        "tell me your story again" if coorcopy == 2:
            jump bgstory
            
            
label bgstory:
            barguy "I see you are a great person and I trust you know."
            barguy "Have you heard about the IO-net?"
            barguy "If not, go to the special room and talk to the guy in he corner."
            barguy "Anyway, I trust you now and I'm sure you could help us."
            barguy "Please go to Betria and talk to my friend. You can meet him in the train in the Wagon 3."
            
            #$ trainguythere = True
            
            barguy "He will tell you what you can do to help us."
            barguy "See you soon. Bye!"
            
            jump xybar
            



label xyspecialroom:
    show bg xybarsr
    show posanim at Position(xpos = 180, ypos=280, xanchor=0.5, yanchor=0.5)
    "There are some people at the tables. There is an engineer and an old guy... he looks like a mine worker. In the dark corner there is a mysterious guy..."
    
    menu:
        "talk to the engineer":
            engineer "Do you need a new space ship? Just have a look at the space ship factory on the Industrial Space Station. It is located at x341 y143. Or just locate iss in a Terminal."
            jump xyspecialroom
            
        "talk to the old mine worker":
            oldminer "I'm an old mine worker... "
            oldminer "I worked with the Barman, he was our dynamite expert. But now he finally figures out his dream job with the Bar. He seems to be really happy now."
            oldminer "Anyway."
            oldminer "..."
            oldminer "We worked in the mine on the Meteoroid 539 but they closed the mine..."
            oldminer "I heard they found a secret base there..."
            oldminer "I don't know where is the entrance of this secret base, but maybe with some dynamite..hehe..."
            oldminer "Whatever."
            oldminer "Are you looking for a job?? Go to the abandonned mine on that meteoroid. It is located at x210 y375. Or just locate meteoroid in a Terminal."
            oldminer "They are still some stuff to get there... good luck!"
            jump xyspecialroom
            
        "talk to the mysterious guy":
            jump xymystguy
            
        
            
        "go out":
            show posanim at Position(xpos = 380, ypos=280, xanchor=0.5, yanchor=0.5)
            jump xybar
    



#MYSTERIOUS GUY

label xymystguy:
    mystguy "I need a drink."
    menu:
        "okay":
            m "Barman! A drink please!"
            "The barman is coming."
            barman "What kind of drink would you like?"
            menu:
                "two normal drinks":
                    barman "Just a minute..."
                    "The barman is going out the Special Room."
                    "The barman comes back with the drinks."
                    barman "It costs 2 c."
                    mystguy "Wait, I'll pay."
                    m "Thanks."
                    mystguy "Cheers!"
                    with flash
                    mystguy "I will tell you a real dramatic story."
                    mystguy "..."
                    mystguy "IO-net was a project to create a free network for everybody do share ideas and knowledge. It worked quite good until a group of scientists which was close to figure out a new source of free energy started to share information about it."
                    mystguy "As soon as the governement heard about that, they started to be really annoying because they were scary to loose there power. They put all important scientists and freedom activists in prison, they turned off the IO-net and destroyed all the copies of the IO-net sofware."
                    mystguy "They don't want us to be free and they are trying to control everything. I think they want to figure out this new free energy and sell it to us later on."
                    mystguy "The situation is really difficult because all the important people with information were cought by the governement and nobody out there knows where are all the IO-net computers."
                    mystguy "If somebody could reactivate all the IO-net computers it would be possible to figure out the new free energy before the governement. So we could stop them and build our own free and open-minded world!"
                    mystguy "If you have any idea how to solve this problem, please do!"
                    mystguy "Bye!"
                    
                    jump xyspecialroom
                    
                "two plasma XXL special drinks":
                    barman "Mhhh I don't know if I still have some... wait a minute, I'll have a look to our storage outside the bar."
                    $ xybarmanaway = True
                    "The barman is going out."
                    menu:
                        "wait":
                            "The barman is coming back."
                            barman "Sorry I don't have plasma XXL special drinks anymore."
                            "The barman is going back to the bar."
                            $ xybarmanaway = False
                            jump xyspecialroom
                        
                        "go out":
                            show posanim at Position(xpos = 380, ypos=280, xanchor=0.5, yanchor=0.5)
                            jump xybar
                
                "nothing, thanks":
                    jump xyspecialroom
                    
        "no":
            m "No, sorry, maybe later..."
            mystguy "No drink, no information. Ciao!"
            jump xyspecialroom


# Kitchen
label xykitchen:

    show bg xykitchen
    
    m "Here is the kitchen... haha! there are dynamite packs on the floor! Interesting... There is also a paper with some stuff written on it."
    
    menu:
        "read paper":
            m "The paper is old and it is difficult read it!"
            "...Rebel Alliance... special wares... Space Dealer... x280 y120..."
            m "Aha, interesting! Maybe I should have a look."
            jump xykitchen
            
        "take dynamite":
            if inv_dynamite == False:
                $ inv_dynamite = True
                with flash
                "You got dynamite!"
                jump xykitchen
            else:
                m "I took dynamite already."
                jump xykitchen
            
        "go out":
            show posanim at Position(xpos = 0.12, ypos=330, xanchor=0.5, yanchor=0.5)
            jump xybar





# XY WAREHOUSE
label xywarehouse:
    hide posanim
    show bg xywh behind lcable, lbulb, ssuit, text

    show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
    
    menu:
        "buy":
            jump xywarehousebuy
        "sell":
            jump xywarehousesell
        "go out":
            hide text
            show posanim at Position(xpos = 458, ypos=260, xanchor=0.5, yanchor=0.5):
            jump xy
            
            
            
            
label xywarehousebuy:
            show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
           
            menu:
                "buy rocks" if cash >= 13:
                    $ cash -= 13 
                    $ rocks += 1
                    jump xywarehousebuy
            
                "buy steel" if cash >= 50:
                    $ cash -= 50 
                    $ steel += 1
                    jump xywarehousebuy
        
                "buy alu" if cash >= 60:
                    $ cash -= 60 
                    $ alu += 1
                    jump xywarehousebuy
        
                "buy textile" if cash >= 40:
                    $ cash -= 40 
                    $ textile += 1
                    jump xywarehousebuy
        
                "buy food" if cash >= 32 :  
                    $ cash -= 32 
                    $ food += 1
                    jump xywarehousebuy
                    
                "back":
                    jump xywarehouse
                
label xywarehousesell:
            show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
   
            menu:
                "sell rocks" if rocks >= 1:
                    $ cash += 10 
                    $ rocks -= 1
                    jump xywarehousesell
            
                "sell steel" if steel >= 1:
                    $ cash += 40 
                    $ steel -= 1
                    jump xywarehousesell
        
                "sell alu" if alu >= 1:
                    $ cash += 50 
                    $ alu -= 1
                    jump xywarehousesell
        
                "sell textile" if textile >= 1:
                    $ cash += 30 
                    $ textile -= 1
                    jump xywarehousesell
        
                "sell food" if food >= 1 :  
                    $ cash += 32 
                    $ food -= 1
                    jump xywarehousesell

                "back":
                    jump xywarehouse

