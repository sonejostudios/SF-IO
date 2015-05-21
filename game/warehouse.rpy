# PRISON WAREHOUSE
label warehouse:
    hide ship
    hide ship1
    hide ship2
    hide ship3
    show bg warehouse behind text

    show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
    
    menu:
        "buy":
            jump warehousebuy
        "sell":
            jump warehousesell
        "go out":
            hide text
            show posanim at Position(xpos = 80, ypos=260, xanchor=0.5, yanchor=0.5):
            jump prisonlift
            
            
            
            
label warehousebuy:
            show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
           
            menu:
                "buy rocks" if cash >= 20:
                    $ cash -= 20 
                    $ rocks += 1
                    jump warehousebuy
            
                "buy steel" if cash >= 50:
                    $ cash -= 50 
                    $ steel += 1
                    jump warehousebuy
        
                "buy alu" if cash >= 60:
                    $ cash -= 60 
                    $ alu += 1
                    jump warehousebuy
        
                "buy textile" if cash >= 40:
                    $ cash -= 40 
                    $ textile += 1
                    jump warehousebuy
        
                "buy food" if cash >= 30 :  
                    $ cash -= 30 
                    $ food += 1
                    jump warehousebuy
                    
                "back":
                    jump warehouse
                
label warehousesell:
            show text "{size=16}Cash = [cash] c \n\nRocks = [rocks] kg  ~  Steel = [steel] kg  ~  Aluminium = [alu] kg \n Textile = [textile] kg  ~  Food = [food] kg{/size}" at Position(xpos = 300, xanchor=0.5, ypos=400, yanchor=0.5)
   
            menu:
                "sell rocks" if rocks >= 1:
                    $ cash += 15 
                    $ rocks -= 1
                    jump warehousesell
            
                "sell steel" if steel >= 1:
                    $ cash += 40 
                    $ steel -= 1
                    jump warehousesell
        
                "sell alu" if alu >= 1:
                    $ cash += 50 
                    $ alu -= 1
                    jump warehousesell
        
                "sell textile" if textile >= 1:
                    $ cash += 30 
                    $ textile -= 1
                    jump warehousesell
        
                "sell food" if food >= 1 :  
                    $ cash += 20 
                    $ food -= 1
                    jump warehousesell

                "back":
                    jump warehouse
