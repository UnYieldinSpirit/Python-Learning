# Create a quick choose your adventure treasure game
print("Welcome to Treasure Island. Your goal is to find the treasure.")

user_input = input("Would you like to go left or right?: ")
if user_input == "left":
    user_input = input("You walk for ten minutes and see a cave entrance. Do you 'enter' or 'turn back'?: ").lower()
    if user_input == "enter":
        user_input = input("You enter the cave system where spiders the size of cars begin to chase you.\nAs you run away, you see a pool of water a spot behind a rock.\nDo you 'hide' or do you 'dive' into the water?: ").lower()
        if user_input == "dive":
            user_input = input("You swim to the bottom of the pool and fall out the bottom into a room.\nThere is a door. Do you try to 'open' the door or 'call' for help?: ").lower()
        else:
            print("The spiders eat you because you didn't hide well.\nGame Over")
            if user_input == "open":
                print("You open the door...\nAs the door slowly opens, you see a mountain of teasure! More than you can carry!\n YOU FOUND THE TREASURE!")
            else:
                print("You use your walkie-talkie, but it alerts the nearby militia of your location. They raid the area and dispose of you.\nGame Over")
    else:
        print("You turn around and see Jason Vorhees standing behind you. I don't have to tell you the rest. You lost\nGame Over")
else:
    print("You take the right path, but it wasn't the RIGHT path. Because you trip on an above ground root causing you to fall. You smack your head on a rock and die.\nGame Over")
