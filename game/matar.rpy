# MATAR
label matar:
    hide ship
    hide ship1
    hide ship2
    hide ship3
    hide text
    
    show bg matarentrance at topleft
    
    menu:
        #"get 100c":
            #$ cash = 100
            #jump matar
            
        "go to the mine shop":
            jump matarshop
            
        "go to the warehouse":
            jump mwarehouse
            
        "go to the lift":
            m "It's closed."
            
        "look behind the mine shop":
            show posanim at Position(xpos = 65, ypos=260, xanchor=0.5, yanchor=0.5)
            jump matarwaste
            
        "go out":
            jump spaceport
    jump matar

label matarwaste:
    m "This is the waste of the mine shop."
    menu:
        "search into the waste":
            if inv_digtool == False:
                m "Hoo there is a mine tool for digging!"
                menu:
                    "take the tool":
                        $ inv_digtool = True
                        with flash
                        "You got a mine tool!"
                        jump matar
                    
                    "back":
                        jump matar
                        
            if issmatarquest == 1:
                m "Hoo there is a nice stone there. It looks like an original matar stone... ?"
                menu:
                    "take the stone":
                        $ inv_mstone = True
                        with flash
                        "You got an original matar stone!"
                        jump matar
                    "back":
                        jump matar
            
            else:
                m "Nothing interesting there..."
                jump matar
        
        "back":
            jump matar
            
            
label matarshop:
    show bg matarshop
    
    show posanim at Position(xpos = 300, ypos=350, xanchor=0.5, yanchor=0.5)
    
    matarshop "Hey, what do you like to buy?\n\nMine Tool = 30c\nOriginal Matar Stone = 50c\nNavigation System = 200c"
    
    menu:
        #"get 100c":
            #$ cash += 100
            #pass
        
        "mine tool" if cash >= 30 and inv_digtool == False:
            $ cash -= 30
            $ inv_digtool = True
            with flash
            "You got a mine tool!"
            pass

            
        "original matar stone"if cash >= 50 and inv_mstone == False:
            $ cash -= 50
            $ inv_mstone = True
            with flash
            "You got an original matar stone!"
            pass
        
        "navigation system"if cash >= 200 and inv_navi == False:
            $ cash -= 200
            $ inv_navi = True
            with flash
            "You got a NaviBack navigation system!"
            pass

            
        "go out":
            show posanim at Position(xpos = 170, ypos=330, xanchor=0.5, yanchor=0.5)
            jump matar
    
    jump matarshop
    
    
    
    
    
    
# MATAR WAREHOUSE
label mwarehouse:
    hide posanim
    show bg matarwh behind text

    show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
    
    menu:
        "buy":
            jump mwarehousebuy
        "sell":
            jump mwarehousesell
        "go out":
            hide text
            show posanim at Position(xpos = 465, ypos=330, xanchor=0.5, yanchor=0.5):
            jump matar
            
            
            
            
label mwarehousebuy:
            show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
           
            menu:
                "buy rocks" if cash >= 10:
                    $ cash -= 10 
                    $ rocks += 1
                    jump mwarehousebuy
            
                "buy steel" if cash >= 30:
                    $ cash -= 30 
                    $ steel += 1
                    jump mwarehousebuy
        
                "buy alu" if cash >= 40:
                    $ cash -= 40 
                    $ alu += 1
                    jump mwarehousebuy
        
                "buy textile" if cash >= 40:
                    $ cash -= 40 
                    $ textile += 1
                    jump mwarehousebuy
        
                "buy food" if cash >= 45 :  
                    $ cash -= 45 
                    $ food += 1
                    jump mwarehousebuy
                    
                "back":
                    jump mwarehouse
                
label mwarehousesell:
            show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
   
            menu:
                "sell rocks" if rocks >= 1:
                    $ cash += 10 
                    $ rocks -= 1
                    jump mwarehousesell
            
                "sell steel" if steel >= 1:
                    $ cash += 30 
                    $ steel -= 1
                    jump mwarehousesell
        
                "sell alu" if alu >= 1:
                    $ cash += 40 
                    $ alu -= 1
                    jump mwarehousesell
        
                "sell textile" if textile >= 1:
                    $ cash += 30 
                    $ textile -= 1
                    jump mwarehousesell
        
                "sell food" if food >= 1 :  
                    $ cash += 40 
                    $ food -= 1
                    jump mwarehousesell

                "back":
                    jump mwarehouse
    
    
    
    
    
