"""
# Game Rules
Rock = 0
paper = 1
scissor = 2

Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.
"""

import random

rock="""
                       888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888 
"""

paper="""
8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88              
"""
scissor=r"""
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.                                                      
                                                                          
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8   
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88             
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88           
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88                                                                      
"""
game_images = [rock, paper, scissor]
print("Hey, welcome to the Rock paper Scissor Game 🎉🔥")
User_Choice=int(input("What's your choice : 0--> Rock, 1 --> paper, 2 --> scissor : "))
print("your's choice is : ", User_Choice)
if User_Choice in range(len(game_images)):
    print(game_images[User_Choice])
else:
    print("your choice is not in the list of choices !")

Computer_Choice = random.randint(0, 2)
print("Computer's Choice is : ")
print(game_images[Computer_Choice])

print("Game result : ")
if  0 <= User_Choice >= 3: 
    print("you typed an invalid number: you lose !")
elif User_Choice ==0 and Computer_Choice == 2 :
    print("you win !🔥🎉")
elif Computer_Choice == 0 and User_Choice == 2:
    print("you lose !")
elif Computer_Choice > User_Choice :
    print("you lost !😔")
elif User_Choice > Computer_Choice :
    print("you Win !")
elif Computer_Choice == User_Choice :
    print("It's a draw ")


