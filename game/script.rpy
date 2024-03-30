define vord = Character("Vord", color="#ff0000")
define dragon = Character("Dragon", color="#008000")
 
image bg_village = "tavern vord.jpg"
image cave_empty = "cave entrance.jpg"
image cave_dragon = "dragon_attack1.jpg"
image dragon_attack1 = "dragon_attack1.jpg" 
image dragon_attack2 = "dragon_attack2.jpg"
image dragon_attack3 = "dragon_attack3.jpg"
image dragon_attack4 = "dragon_attack4.jpg"
image dragon_attack5 = "dragon_attack5.png"
image dragon_attack6 = "dragon_attack6.png"
image dragon_attack7 = "dragon_attack7.jpg"
image dragon_attack8 = "dragon_attack8.jpg"
image dragon_attack9 = "dragon_attack9.jpg"
image dragon_attack10 = "dragon_attack10.jpg"
image dragon_defeat = "dragon defeat.jpg"


init python:
    player_health = 100
    monster_health = 50
    answered_correctly = False

# ------------------------
# SCENE 1: Vord's Welcome
# ------------------------
label start:
    play music "vord tavern.mp3"
    scene bg_village
    show vord abi at left
    vord "Welcome to Vordred's Tavern."
    menu:
        "Yes!":
            jump explore
        "Not yet.":
            vord "Very well. Return when you are prepared."
            return              
label explore:
    vord "Excellent! Your journey begins. Explore our lands, but beware... a fearsome dragon slumbers in a nearby cave."
    
# ------------------------
# SCENE 2: Exploration and the Cave
# ------------------------
    
    scene cave_empty
    "...Exploration..." 
    vord "This cave looks dangerous. Let's proceed with caution."
    
    "You stumble upon a dark cave entrance. A faint snore echoes from within."
    scene dragon_attack1
    

# ------------------------
# SCENE 3: Dragon Encounter
# ------------------------ 
    call combat_loop from _call_combat_loop


label combat_loop:
    while player_health > 0 and monster_health > 0:
        "Player Health: [player_health]"
        "Monster Health: [monster_health]"

        menu:
            "Attack":
                call quiz_and_attack from _call_quiz_and_attack
            "Flee":
                "You flee from the monster. Coward!"
                $ renpy.quit()

        if not answered_correctly:  
            call monster_attack from _call_monster_attack


label monster_attack:
    $ damage = renpy.random.randint(8, 16)
    $ player_health -= damage
    "The monster attacks you, dealing [damage] damage!"
    "Your Health: [player_health]"
    "Monster's Health: [monster_health]"
    if player_health <= 0:
        "You were defeated by the monster!"
        $ renpy.quit()
    elif monster_health <=0:
        "You defeated the monster!"
        $ renpy.quit()
        
label quiz_and_attack:
    $ damage = renpy.random.randint(5, 15) 

    if not answered_correctly:
        jump ask_question
    else:
        jump next_question

label ask_question:
    # Choose a random question to ask
    $ question_number = renpy.random.randint(1, 10)

    if question_number == 1:
        jump question1
    elif question_number == 2:
        jump question2
    elif question_number == 3:
        jump question3
    elif question_number == 4:
        jump question4
    elif question_number == 5:
        jump question5
    elif question_number == 6:
        jump question6
    elif question_number == 7:
        jump question7
    elif question_number == 8:
        jump question8
    elif question_number == 9:
        jump question9
    else:
        jump question10

label next_question:
    # Increment question number and reset answered_correctly
    $ question_number += 1
    $ answered_correctly = False

    if question_number > 10:
        jump ask_question

    if question_number == 1:
        jump question1
    elif question_number == 2:
        jump question2
    elif question_number == 3:
        jump question3
    elif question_number == 4:
        jump question4
    elif question_number == 5:
        jump question5
    elif question_number == 6:
        jump question6
    elif question_number == 7:
        jump question7
    elif question_number == 8:
        jump question8
    elif question_number == 9:
        jump question9
    else:
        jump question3

label question1:

    $ question = "Which of the following is considered the brain of a computer?" #Q1
    "Quiz Question: [question]"
    menu:
        "GPU":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_1
        "CPU": #RIGHT ANSWER
            "Correct!"
            scene dragon_attack2
            dragon "Argh! There's no way you deal such damage!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_2
        "Cooler":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_3
        "Motherboard":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_4

label question2:

    $ question = "What type of software is designed to manage and control the core operations of a computer?" #Q2
    "Quiz Question: [question]"
    menu:
        "Linux":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_5
        "MacOS":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_6
        "Operating System": #RIGHT ANSWER
            "Correct!"
            scene dragon_attack3
            dragon "ARGH! You were much stronger than I have expected!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_7
        "Neptune":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_8

label question3:

    $ question = "Which device is used to connect multiple computers and devices together in a network?" #Q3
    "Quiz Question: [question]"
    menu:
        "Router":
            "Correct!" #RIGHT ANSWER
            scene dragon_attack4
            dragon "GAAAH! A lucky strike!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_9
        "Toaster":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_10
        "Oven":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_11
        "Tray":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_12

label question4:

    $ question = "Which of the following is a high-level programming language often used for web development?" #Q4
    "Quiz Question: [question]"
    menu:
        "HTML":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_13
        "CSS":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_14
        "PHP":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_15
        "Javascript": #RIGHT ANSWER
            "Correct!"
            scene dragon_attack5
            dragon "ARGH! How can you deal such damage?!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_16

label question5:

    $ question = "Which unit of measurement is the smallest?" #Q5
    "Quiz Question: [question]"
    menu:
        "Gigabyte":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_17
        "Petabyte":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_18
        "Kilobyte": #RIGHT ANSWER
            "Correct!"
            scene dragon_attack6
            dragon "ARGH! How could you?!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_19
        "Megabyte":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_20

label question6:

    $ question = "Which of these is a common image file format?" #Q6
    "Quiz Question: [question]"
    menu:
        ".docx":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_21
        ".exe":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_22
        ".zip":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_23
        ".jpeg": #RIGHT ANSWER
            "Correct!"
            scene dragon_attack7
            dragon "Ah! It might kill me!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_24

label question7:

    $ question = "Which device is primarily used to provide visual output from a computer?" #Q7
    "Quiz Question: [question]"
    menu:
        "Printer":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_25
        "Monitor": #RIGHT ANSWER
            "Correct!"
            scene dragon_attack8
            dragon "Urgh! You deal a lot of damage!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_26
        "Microphone":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_27
        "Webcam":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_28

label question8:

    $ question = "What is the term used for storing and accessing data over the internet instead of on your local computer?" #Q8
    "Quiz Question: [question]"
    menu:
        "Cloud Computer": #RIGHT ANSWER
            "Correct!"
            scene dragon_attack9
            dragon "ARGH! You have made me angry!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_29
        "NAS":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_30
        "Edge":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_31
        "Google Chrome":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_32

label question9:

    $ question = "What is the first step you would usually take when a program on your computer freezes?" #Q9
    "Quiz Question: [question]"
    menu:
        "Unplug the cable":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_33
        "Turn off the computer abruptly":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_34
        "Wait for the program to suddenly fix itself":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_35
        "Restart your Computer": #Correct Answer
            "Correct!"
            scene dragon_attack10
            dragon "AH! NO!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_36

label question10:
    $ question = "What is a common tool used to protect your computer from malicious software?"
    "Quiz Question: [question]"
    menu:
        "Windows Defender":
            "Correct!"
            scene dragon_attack10
            dragon "ARGH! I don't believe it!"
            $ monster_health -= damage
            "You attack the monster, dealing [damage] damage!"
            $ answered_correctly = True
            call monster_attack from _call_monster_attack_37
        "Keyboard":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_38
        "Wire":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_39
        "Patch Cable":
            "Incorrect!"
            "The monster counterattacks!"
            call monster_attack from _call_monster_attack_40