
#screen clock
screen clock:
    timer 3600.0 repeat True action [SetVariable("min", 0), SetVariable("sec", 0),SetVariable("hour", int(hour) + 1)]
    timer 60.0 repeat True action [SetVariable("sec", 0),SetVariable("min", int(min) + 1)]
    timer 1.0 repeat True action [SetVariable("sec", int(sec) +1)]
    
    #$ runtime = renpy.get_game_runtime()
    
    text "[hour]:[min]:[sec]" size 16 at Position(xpos = 0.98, ypos= 0.03, xanchor = 1.0)
    
    text "[cash] c" size 16 at Position(xpos = 0.98, ypos= 0.065, xanchor = 1.0)



#screen inventory
screen inventory:
    #text "INVENTORY" at Position(xpos = 0, ypos= 0)
    
    if inv_lcable == True:
        add "pics/inv_lcable.png" at Position(xpos=0, ypos=0)
    if inv_lbulb == True:
        add "pics/inv_lbulb.png" at Position(xpos=50, ypos=0)
    if inv_ssuit == True:
        add "pics/inv_ssuit.png" at Position(xpos=100, ypos=0)
    if inv_digtool == True:
        add "pics/inv_digtool.png" at Position(xpos=150, ypos=0)
    if inv_dynamite == True:
        add "pics/inv_dynamite.png" at Position(xpos=200, ypos=0)
    if inv_navi == True:
        add "pics/inv_navi.png" at Position(xpos=250, ypos=0)
    if inv_ticket == True:
        add "pics/inv_ticket.png" at Position(xpos=300, ypos=0)
    if inv_ionet == True:
        add "pics/inv_ionet.png" at Position(xpos=350, ypos=0)
    if inv_mstone == True:
        add "pics/inv_mstone.png" at Position(xpos=400, ypos=0)
    if inv_blakekey == True:
        add "pics/inv_blakekey.png" at Position(xpos=450, ypos=0)
    if inv_seamap == True:
        add "pics/inv_seamap.png" at Position(xpos=500, ypos=0)
        
        
        
#screen setup stars amount
screen starsamount:

    vbox: 
        textbutton "max" action [SetVariable("starsamount", 200)]#, renpy.reload_script()
        textbutton "mid" action [SetVariable("starsamount", 100)]#, renpy.reload_script()
        textbutton "min" action [SetVariable("starsamount", 10)]#, renpy.reload_script()
        text "[starsamount]"
        

