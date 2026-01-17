import random


snake = {17: 7, 32: 15, 54: 34, 62: 45, 92: 32}
ladder = {5: 25, 31: 42, 51: 67, 32: 90, 45: 88}


player_pos =0
com_pos = 0


player_started = False
com_started = False


turn = 0
while True:
    turn += 1
    print("\n---------------------------------------")

    
    if turn % 2 == 0:
        input("🎲 Press Enter to roll the dice for Player....")
        roll = random.randint(1, 6)
        print(f"Player rolled: {roll}")

        if not player_started:
            if roll == 6:
                player_started = True
                player_pos = 6
                print(" Player's game started at 6!")
                turn -= 1
            else:
                print(" Player needs to roll a 6 to start.")
                continue
        else:
            player_pos += roll

            if player_pos > 100:
                player_pos -= roll  
                print("Move exceeds 100, not counted.")
            else:
                
                if player_pos in snake:
                    print(f"🐍 Snake bit Player at {player_pos}")
                    player_pos = snake[player_pos]
                    print(f"⬇️ Player moved down to {player_pos}")

                elif player_pos in ladder:
                    print(f"🪜 Player climbed ladder from {player_pos}")
                    player_pos = ladder[player_pos]
                    print(f"⬆️ Player moved up to {player_pos}")

                print(f" Player's position: {player_pos}")

                
                if player_pos == com_pos:
                    print("Computer is out! Goes back to 0.")
                    com_pos = 0

                
                if player_pos == 100:
                    print("🏆 Congratulations! Player wins! 🤩")
                    break

                if roll == 6:
                    print("Player gets another turn!")
                    turn -= 1  


    else:
        input("🎲 Press Enter to roll the dice for Computer...")
        roll = random.randint(1, 6)
        print(f"Computer rolled: {roll}")

        if not com_started:
            if roll == 6:
                com_started = True
                com_pos = 6
                print("Computer's game started at 6!")
                turn -= 1
            else:
                print(" Computer needs to roll a 6 to start.")
                continue
        else:
            com_pos += roll

            if com_pos > 100:
                com_pos -= roll
                print("Move exceeds 100, not counted.")
            else:
                if com_pos in snake:
                    print(f"🐍 Snake bit Computer at {com_pos}")
                    com_pos = snake[com_pos]
                    print(f"⬇️ Computer moved down to {com_pos}")

                elif com_pos in ladder:
                    print(f"Computer climbed ladder from {com_pos}")
                    com_pos = ladder[com_pos]
                    print(f"⬆️ Computer moved up to {com_pos}")

                print(f"🎯 Computer's position: {com_pos}")

                if com_pos == player_pos:
                    print("💥 Player is out! Goes back to 0.")
                    player_pos = 0

                if com_pos == 100:
                    print("🏆 Computer wins! ")
                    break

                if roll == 6:
                    print("🔥 Computer gets another turn!")
                    turn -= 1











