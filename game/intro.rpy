
# Intro
label intro:
    
    stop music fadeout 2.0
    play sound "snd/title.ogg"
    pause 2.0
    play music "snd/spaceship-amb.ogg" loop fadein 3.0
    
    show starssmall d2u behind ship
    show starsmid d2u behind ship
    show starsbig d2u behind ship
    with Dissolve(3.0)
    
    #centered "{cps=20}This is going to be amazing...{/cps}"
    #hide centered
    
    show title at truecenter
    with Dissolve(3.0)
    
    
    

    
    return
    


# FINAL SCENE WON           
label win:
    hide bg
    hide screen clock
    scene bgcolor
    with Dissolve(3.0)
    
    show starssmall d2u behind ship
    show starsmid d2u behind ship
    show starsbig d2u behind ship
    with Dissolve(3.0)
    
    show text (_("CONGRATULATIONS,\nYOU WON THE GAME!\n\nThank you for playing.\n You played [hour] hours, [min] minutes and [sec] secondes!")) at truecenter
    with Dissolve(3.0)
    
    menu:
        "Quit":
            jump credits
        "I'm not done!":
            play music "snd/spaceship.ogg" loop fadein 1.0
            jump spaceship




    

# Credits      
label credits:
    show bgcolor
    hide screen main_menu
    with Dissolve(1.0)
    
    
    
    show starssmall d2u behind ship
    show starsmid d2u behind ship
    show starsbig d2u behind ship
    
    with Dissolve(1.0)
    

    show text (_("SF-IO")) at truecenter
    with Dissolve(1.0)
    pause 2    
    
    show text (_("An\nOld-School\nScience-Fiction\nAdventure\nRPG\nGame")) at truecenter
    with Dissolve(1.0)
    pause 2
    
    show text (_("Created by\nVincent Rateau")) at truecenter
    with Dissolve(1.0)
    pause 2
    
    show text (_("Licensed under\nthe GPL v2")) at truecenter
    with Dissolve(1.0)
    pause 2
    
    show text (_("Sonejo Media Studio")) at truecenter
    with Dissolve(1.0)
    pause 2
    show text (_("www.sonejo.net")) at truecenter
    with Dissolve(1.0)
    pause 2
    
    show text (_("All sounds from Freesound.org (Creative Commons): \n ingeos, black-boe, walter-odington, davidworksonline, \nsergenious, lorenzosu, cgeffex, anton, \nsoulman-90, vhlam, pawsound, noirenex, drminky, \ngmarchisio, iankath, nickrave, trebblofang, lloydevans09, \nlittlebrojay, blueneon, the-very-real-horst, alaskarobotics, \nkaumodaki, sophiehall3535, themusicalnomad, daenerys, pan14, \nviznoman, limitsnap-creations, vumseplutten1709, benagain, daveofdefeat2248, \ngaleku, steshystesh, hoerspielwerkstatt-hef, vegapomme27, \nproaudioninja, anoesj, frankelmedico. \nBar Theme from Jamendo by Marius Joppich (Creative Commons).")) at truecenter
    with Dissolve(1.0)
    pause 4
    
    show text (_("Thanks for playing ;)")) at truecenter
    with Dissolve(1.0)
    pause 2
    
    hide text
    with Dissolve(1.0)
    hide starssmall d2u 
    hide starsmid d2u 
    hide starsbig d2u 

    $ musicplaying = renpy.music.get_playing(channel='music')
    if musicplaying == "snd/bar.ogg":
        play music "snd/spaceport-met.ogg" loop fadein 0.1
        #stop music fadeout 1.0
    
    with Dissolve(1.0)
    pause 1

    jump _invoke_main_menu
