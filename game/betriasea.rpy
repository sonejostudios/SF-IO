# BETRIA SEA

label bseastart:
    #show bgcolor behind waves

    hide posanim
    
    
    show bg betriasea at topleft
    
    show boat at Position(xpos = 300, ypos=285, xanchor=0.5, yanchor=0.5) behind posanim
    
    show posanim at Position(xpos = 300, ypos=285, xanchor=0.5, yanchor=0.5)
    
    jump bsea
    
    
        
label bsea:

    show screen inventory
     
    show waves behind bg


    
    show boat behind bg:
        xanchor 0.5
        yanchor 0.5
        linear 1 xpos 300 ypos 285
    
    show posanim:
        xanchor 0.5
        yanchor 0.5
        linear 1 xpos 300 ypos 285


# terrain
    # coast1 beach
    if desertx == 0 and deserty != 5:
        if betriaseaflip == False:
            show bs coast2 at Position(xpos = 300, ypos=285, xanchor=1.0, yanchor=0.5) behind bg, boat
            $ betriaseaflip = True
            
        else:
            show bs coast3 at Position(xpos = 300, ypos=285, xanchor=1.0, yanchor=0.5) behind bg, boat
            $ betriaseaflip = False
            
    
    
    # beach
    if desertx == 0 and deserty == 5:
        show bs coast1 at Position(xpos = 300, ypos=285, xanchor=1.0, yanchor=0.5) behind bg, boat
        
    # secret cave
    if desertx == 0 and deserty == 10:
        show bs cave at Position(xpos = 300, ypos=285, xanchor=1.0, yanchor=0.5) behind bg, boat
        
        
    # islands
    if desertx == 10 and deserty == 3:
        show islands at Position(xpos = 350, ypos=285, xanchor=0.0, yanchor=0.5) behind bg
    
    else:
        hide islands

        
    
    
    
    if desertx > 0 :
        hide bs
        



    #hide text
    #show text "x[desertx], y[deserty]" at left


    jump bseamenu


label bseamenu:    
    
    menu:
        "go out the boat" if desertx == 0 and deserty == 5:
            hide boat
            hide bs
            show posanim at Position(xpos = 170, ypos=340, xanchor=0.5, yanchor=0.5)
            jump betriacoast1
        
        "enter into the secret cave" if desertx == 0 and deserty == 10:
            jump betriacave
            
        "enter the islands" if desertx == 10 and deserty == 3:
            show posanim at Position(xpos =210, ypos=300, xanchor=0.5, yanchor=0.5)
            jump betriaislands
            
        "show sea map":
            hide screen inventory
            show seamap behind posanim
            show posanim at Position(xpos = (desertx*65)+60, ypos=(deserty*40)+40, xanchor=0.5, yanchor=0.5)
            menu:
                "exit":
                    hide seamap
                    show posanim at Position(xpos = 300, ypos=285, xanchor=0.5, yanchor=0.5)
                    pass
 
        "go north" if deserty >= 1:
                show posanim:
                    linear 1 ypos 165
                show boat behind bg:
                    rotate 0
                    linear 1 ypos 165
                    
                pause 1
                
                $ deserty -= 1
                
                show posanim:
                    ypos 400
                show boat behind bg:
                    rotate 0
                    ypos 400
                    
                pass
            
       
        "go west" if desertx >= 1:
                show posanim:
                    linear 1 xpos 50
                show boat behind bg:
                    rotate 270
                    linear 1 xpos 50
                pause 1
                
                $ desertx -= 1
                
                show posanim:
                    xpos 540
                show boat behind bg:
                    rotate 270
                    xpos 540
                pass
            
       
        "go east"if desertx <= 9:
                show posanim:
                    linear 1 xpos 540
                show boat behind bg:
                    rotate 90
                    linear 1 xpos 540
                   
                pause 1
                
                $ desertx += 1
                
                show posanim:
                    xpos 50
                show boat behind bg:
                    rotate 90
                    xpos 50
                    
                pass
            
        
        "go south" if deserty <= 9:
                show posanim:
                    linear 1 ypos 400
                show boat behind bg:
                    rotate 180
                    linear 1 ypos 400
                pause 1
                
                $ deserty += 1
                
                show posanim:
                    ypos 165
                show boat behind bg:
                    rotate 180
                    ypos 165
                pass
            
    jump bsea
    
    
  
