from random import randint
# player_name = "Chris"
# player_attack = 10
# player_heal = 5
# player_health = 100

# this is a list in python, it can store different type of data
# player = ["Chris", 10, 5, 100]


game_running = True

# game begin here
# while game_running is true, its gonna repeat runing this block of code


def rand_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running:
    # this is a dictionary, it can store key-matching value
    player = {"name": "Chris", "attack": 10, "heal": 20, "health": 100}
    monster = {'name': 'MadMax', 'attack_min': 5, 'attack_max': 30, 'health': 100}
    # enter player name
    print('---' * 10)
    print('enter player name')
    player["name"] = input()
    print(player["name"] + " has " + str(player["health"]) + " health")
    print("monster has " + str(monster['health']) + " health")
    print('---' * 10)

    # while this round is not false
    new_round = True
    while new_round:
        player_won = False
        monster_won = False

        print("Monster's health now:")
        print(monster['health'])

        print("Player's health now: ")
        print(player["health"])
        print('---' * 10)
        print('Please select a action')
        print('---' * 10)
        print('1) attack')
        print('2) heal')
        print('3) Exit Game')

        player_choice = input()

        # 1
        if player_choice == 1:
            monster['health'] = monster['health'] - player["attack"]
            # if monster is dead
            if monster['health'] <= 0:
                player_won = True
            else:
                player["health"] =  player["health"] - rand_monster_attack()
                # if you are dead
                if player["health"] <= 0:
                    monster_won = True


        # 2
        elif player_choice == 2:
            player["health"] = player["health"] + player["heal"]
            player["health"] = player["health"] - rand_monster_attack()
            if player["health"] <= 0:
                monster_won = True
        # 3
        elif player_choice == 3:
            game_running = False
            new_round = False
        else:
            print("Invalid input")

        # if either player or monster won the game
        if player_won:
            print("game over, you win!")
            new_round = False
        if monster_won:
            print("game over, you lose!")
            new_round = False


