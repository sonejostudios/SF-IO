

label intro:
   
    show starssmall d2u behind ship
    show starsmid d2u behind ship
    show starsbig d2u behind ship
    with Dissolve(3.0)
    
    #centered "{cps=20}This is going to be amazing...{/cps}"
    #hide centered
 
    show title at truecenter
    with Dissolve(3.0)

    
    return
    
    

# Credits      
label credits:
    show bgcolor
    hide screen main_menu
    with Dissolve(1.0)
    
    
    
    show starssmall d2u behind ship
    show starsmid d2u behind ship
    show starsbig d2u behind ship
    
    with Dissolve(1.0)
    

    show text "SF-IO" at truecenter
    with Dissolve(1.0)
    pause 2    
    show text "An\nOld-School\nScience-Fiction\nAdventure\nRPG\nGame" at truecenter
    with Dissolve(1.0)
    pause 2
    show text "Created by\nVincent Rateau" at truecenter
    with Dissolve(1.0)
    pause 2
    show text "Licensed under\nthe GPL v2" at truecenter
    with Dissolve(1.0)
    pause 2
    show text "Sonejo Media Studio" at truecenter
    with Dissolve(1.0)
    pause 2
    show text "www.sonejo.net" at truecenter
    with Dissolve(1.0)
    pause 2
    show text "Thanks for playing ;)" at truecenter
    with Dissolve(1.0)
    pause 2
    hide text
    with Dissolve(1.0)
    hide starssmall d2u 
    hide starsmid d2u 
    hide starsbig d2u 
    with Dissolve(1.0) 
    pause 1

    jump _invoke_main_menu
