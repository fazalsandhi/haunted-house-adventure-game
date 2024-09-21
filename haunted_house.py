print('''
        ______________
       /_|[][][][][]_|\\
     (      Haunted    )
     (      House      )
      \|[][][][][][][]|/
       ~~~~~~~~~~~~~~~~
''')
print("Welcome to the Haunted House!")
print("Your mission is to escape the haunted house safely.")

# First choice: Enter or Run Away
choice1 = input("Do you want to 'enter' the house or 'run away'? ").lower()

if choice1 == "enter":
    print('''
        You step inside the eerie house, the door creaks behind you...
              ____________
             |  ________  |
             | |        | |
             | |  o  o  | |
             | |    ^   | |
             | |   '-'  | |
             | |________| |
             |____________|
    ''')
    
    # Second choice: Go Upstairs or Stay Downstairs
    choice2 = input("You see a staircase. Do you want to go 'upstairs' or 'stay downstairs'? ").lower()
    
    if choice2 == "upstairs":
        print('''
        You carefully walk up the stairs...
              _____||_____
             /            \\
            /______________\\
           |    ________    |
           |   |        |   |
           |   |        |   |
        ''')
        
        # Third choice: Check the attic or the bedroom
        choice3 = input("You hear noises. Do you want to check the 'attic' or the 'bedroom'? ").lower()
        if choice3 == "attic":
            print('''
            You found an old chest in the attic and opened it...
              ________
             /  _____  \\
            |  |     |  |
            |__|_____|__|
            You found a hidden treasure! You Win!
            ''')
        elif choice3 == "bedroom":
            print('''
            You enter the bedroom and...
                _________
               |         |
               |  GHOST  |
               |_________|
            A ghost appeared and scared you to death! Game Over.
            ''')
        else:
            print("You wandered aimlessly and got lost. Game Over.")
            
    elif choice2 == "stay downstairs":
        print('''
        You decide to explore the ground floor...
              ________
             |        |
             |        |
             |________|
        ''')
        
        # Fourth choice: Investigate the basement or the kitchen
        choice4 = input("You hear a noise coming from the 'basement' or the 'kitchen'. Where do you go? ").lower()
        if choice4 == "basement":
            print('''
            You descend into the dark basement...
              ___________
             | Basement  |
             |   Door    |
             |___________|
            You got trapped in the basement forever. Game Over.
            ''')
        elif choice4 == "kitchen":
            print('''
            You found a hidden exit in the kitchen!
              _________
             |  EXIT   |
             |_________|
            You escape the haunted house. You Win!
            ''')
        else:
            print("You hesitated and got caught by ghosts. Game Over.")
    
    else:
        print("You stood still and a ghost caught you. Game Over.")

else:
    print("You ran away safely. Maybe next time you'll be braver!")
