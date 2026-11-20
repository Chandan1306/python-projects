plr1 = input("Player 1 - Enter rock/paper/scissor: ")
plr2 = input("Player 2 - Enter rock/paper/scissor: ")

if plr1 == plr2:
    print("It's a tie")
elif plr1 == "rock":
    if plr2 == "scissor":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif plr1 == "paper":
    if plr2 == "rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif plr1 == "scissor":
    if plr2 == "paper":
        print("Player 1 wins")
    else:
        print("Player 2 wins")