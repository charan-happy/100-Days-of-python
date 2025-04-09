print("""                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
""")

print("Welcome to the Treasure Island ! ")

print("your mission is to find the treasure ")

Initial_Direction=input('you\'re at the cross-road, where you wanted to go ? "Right" or "Left" : ').lower()

if Initial_Direction == "left" :
    print("oh good choice, let's move on ...")
    second_choice = input("Do you wanted to swim or wait ? ").lower()
        
    if second_choice == "Wait" :
        Door_choice = input("let's select door of your choice (Either blue or green or yellow) : ").lower()
        if Door_choice == "yellow":
            print("Congratulations 🎉🎉💰💰🔥 yahoo, you find the treasure !")   
        else :
            print("you choose wrong door ! 😊😊 Better luck next time !") 
    else :
        print("your choice is not in the list")
else:
    print("You entered wrong input, Better luck next time !, you fallen in pool😆")
