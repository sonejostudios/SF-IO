# ALDABRAN
label aldabran:
    hide ship
    hide ship1
    hide ship2
    hide ship3
    hide text
    hide posanim
    
    
    show bg aldabran at topleft
    
    show posanim:
        xanchor 0.5
        yanchor 0.5
        xpos 300 ypos 285
    
    jump aldabrandesert
    
    
        
label aldabrandesert:
    hide ship1
    hide ship2
    hide ship3
    
    show posanim:
        xanchor 0.5
        yanchor 0.5
        linear 1 xpos 300 ypos 285
    

#Navi

    hide naviarrow
    hide navi
    
    if navi_on == True:    
        show navi at Position(xpos = 81, ypos=370, xanchor=0.5, yanchor=0.5):
        
        if desertx > 5:
            show naviarrow at Position(xpos = 81, ypos=370, xanchor=0.4, yanchor=0.5):
                rotate 270
        if desertx < 5:
            show naviarrow at Position(xpos = 81, ypos=370, xanchor=0.4, yanchor=0.5):
                rotate 90
        if deserty > 5:
            show naviarrow at Position(xpos = 81, ypos=370, xanchor=0.4, yanchor=0.5):
                rotate 0
        if deserty < 5:
            show naviarrow at Position(xpos = 81, ypos=370, xanchor=0.4, yanchor=0.5):
                rotate 180
                
        if desertx > 5 and deserty > 5:
            show naviarrow at Position(xpos = 81, ypos=370, xanchor=0.4, yanchor=0.5):
                rotate 315
        if desertx > 5 and deserty < 5:
            show naviarrow at Position(xpos = 81, ypos=370, xanchor=0.4, yanchor=0.5):
                rotate 225
        if desertx < 5 and deserty > 5:
            show naviarrow at Position(xpos = 81, ypos=370, xanchor=0.4, yanchor=0.5):
                rotate 45
        if desertx < 5 and deserty < 5:
            show naviarrow at Position(xpos = 81, ypos=370, xanchor=0.4, yanchor=0.5):
                rotate 135
            
            

    
# Spaceship

    if desertx == 5 and deserty == 5:
        hide naviarrow
        
        if spaceshipnr == 1:
            show ship1 fscaled2 at Position(xpos = 150, ypos=210, xanchor=0.5, yanchor=0.5):
                rotate 90
        if spaceshipnr == 2:
            show ship2 fscaled2 at Position(xpos = 450, ypos=210, xanchor=0.5, yanchor=0.5):
                rotate 90
        if spaceshipnr == 3:
            show ship3 fscaled2 at Position(xpos = 150, ypos=210, xanchor=0.5, yanchor=0.5):
                rotate 90
        
    
# terrain
    hide al_ter1
    hide al_ter2
    hide al_ter3
    hide al_ter4
    hide al_sship
    hide text

    if desertx == 4 and deserty == 5:
        show al_ter1 at Position(xpos = 100, ypos=210, xanchor=0.5, yanchor=0.5):
    
    if desertx == 6 and deserty == 5:
        show al_ter2 at Position(xpos = 460, ypos=210, xanchor=0.5, yanchor=0.5):
    
    if desertx == 5 and deserty == 4:
        show al_ter3 at Position(xpos = 200, ypos=360, xanchor=0.5, yanchor=0.5):
    
    if desertx == 5 and deserty == 6:
        show al_ter4 at Position(xpos = 450, ypos=360, xanchor=0.5, yanchor=0.5):



    if desertx == 7 and deserty == 8:
        show al_ter3 at Position(xpos = 100, ypos=210, xanchor=0.5, yanchor=0.5):
            rotate 45
    
    if desertx == 2 and deserty == 1:
        show al_ter2 at Position(xpos = 460, ypos=210, xanchor=0.5, yanchor=0.5):
            rotate 240
    
    if desertx == 3 and deserty == 3:
        show al_ter3 at Position(xpos = 200, ypos=360, xanchor=0.5, yanchor=0.5):
            rotate 78
    
    if desertx == 5 and deserty == 10:
        show al_ter4 at Position(xpos = 450, ypos=360, xanchor=0.5, yanchor=0.5):
            rotate 320
        
    if desertx == 9 and deserty == 9:
        show al_ter1 at Position(xpos = 100, ypos=210, xanchor=0.5, yanchor=0.5):
            rotate 80
    
    if desertx == 7 and deserty == 2:
        show al_ter2 at Position(xpos = 460, ypos=210, xanchor=0.5, yanchor=0.5):
            rotate 120
    
    if desertx == 8 and deserty == 3:
        show al_ter3 at Position(xpos = 200, ypos=360, xanchor=0.5, yanchor=0.5):
            rotate 190
    
    if desertx == 0 and deserty == 5:
        show al_ter4 at Position(xpos = 450, ypos=360, xanchor=0.5, yanchor=0.5):
            rotate 40
            
    if desertx == 0 and deserty == 6:
        show al_ter1 at Position(xpos = 100, ypos=210, xanchor=0.5, yanchor=0.5):
            rotate 100
    
    if desertx == 0 and deserty == 2:
        show al_ter2 at Position(xpos = 460, ypos=210, xanchor=0.5, yanchor=0.5):
            rotate 140
    
    if desertx == 8 and deserty == 0:
        show al_ter3 at Position(xpos = 200, ypos=360, xanchor=0.5, yanchor=0.5):
            rotate 190
    
    if desertx == 5 and deserty == 9:
        show al_ter2 at Position(xpos = 450, ypos=360, xanchor=0.5, yanchor=0.5):
            rotate 20

    # spaceship wreck
    if desertx == 9 and deserty == 7:
        show al_sship at Position(xpos = 450, ypos=230, xanchor=0.5, yanchor=0.5) behind posanim
    
    
    
    

    #show text "x[desertx], y[deserty]" at left
    
    menu:
        "take off" if desertx == 5 and deserty == 5 :
            hide ship1
            hide ship2
            hide ship3
            hide naviarrow
            hide navi
            hide al_ter1
            hide al_ter2
            hide al_ter3
            hide al_ter4
            $ navi_on = False
            jump takeoff
        
        "use navigation system" if inv_navi == True and navi_on == False:
            $ navi_on = True
            pass
        
        "enter spaceship wreck" if desertx == 9 and deserty == 7 :
            hide al_sship
            hide navi
            hide naviarrow
            jump alswreck
        
        "go north"if deserty >= 0:
            if navi_on == False:
                m "I won't go into the desert without using a proper navigation system!"
            else:
                show posanim:
                    linear 1 ypos 165
                pause 1
                
                $ deserty -= 1
                
                show posanim:
                    ypos 400
                pass
            
        "go west" if desertx >= 0:
            if navi_on == False:
                m "I won't go into the desert without using a proper navigation system!"
            else:
                show posanim:
                    linear 1 xpos 50
                pause 1
                
                $ desertx -= 1
                
                show posanim:
                    xpos 540
                pass
            
        "go east"if desertx <= 10:
            if navi_on == False:
                m "I won't go into the desert without using a proper navigation system!"
            else:
                show posanim:
                    linear 1 xpos 540
                pause 1
                
                $ desertx += 1
                
                show posanim:
                    xpos 50
                pass
            
        "go south" if deserty <= 10:
        
            if navi_on == False:
                m "I won't go into the desert without using a proper navigation system!"
            else:
                show posanim:
                    linear 1 ypos 400
                pause 1
                
                $ deserty += 1
                
                show posanim:
                    ypos 165
                pass
            
    jump aldabrandesert
    

label alswreck:

    show bg alswreck
    
    show posanim at Position(xpos = 290 , ypos=175, xanchor=0.5, yanchor=0.5)

    #show ionet sender
    if io_alswreck == True:
        show ionetsender at Position(xpos = 135 , ypos=377, xanchor=0.5, yanchor=0.5)
    
    
    menu:
        "copy IO-net on this computer" if inv_ionet == True and io_alswreck == False:
            call ioinstall from _call_ioinstall_1

        
        "IO-net info" if io_alswreck == True:
            call ioinfo from _call_ioinfo_1
        
        "go out":
            hide ionetsender
            #show posanim at Position(xpos = 243 , ypos=303, xanchor=0.5, yanchor=0.5)
            
            $ desertx = 9
            $ deserty = 7
            
            jump aldabran
            
    jump alswreck
    
    
    
    
    
