import resources
from resources import Character, Goblin
from random import randint, shuffle, choice

def fight(players : list, enemies : list):
    participants = players + enemies # Create initiative order
    shuffle(participants)

    for char in participants:
        target = ""
        # Is the character a player or a goblin?
        if char in players:
            target = choice(enemies)
        else:
            target = choice(players)

        target.take_damage(char.get_attack())
        if target.get_health() == 0:
            print(f"{target.get_name()} has died!")
            if type(target) == Goblin:
                enemies.remove(target)
            else:
                players.remove(target)
            participants.remove(target)
        
        else:
            print(f"{target.get_name()} has {target.get_health()} health remaining.")

        if len(enemies) == 0 or len(players) == 0: # If there is no enemies or players left.
            break #dance




if __name__ == "__main__":

    enemies = []
    players = []

    nemy = Character("Emy", 20, 5, 2)
    nick = Character("Nick", 15, 2, 1)
    players.append(nemy)
    players.append(nick)

    enemies.append(Goblin(10, 3, 2, 1))
    enemies.append(Goblin(15, 2, 1, 2))
    enemies.append(Goblin(12, 3, 1, 3))

    round = 1
    while len(enemies) != 0 and len(players) != 0:
        print(f"\nROUND {round}, FIGHT!")
        fight(players, enemies)
        round +=1
    
    if len(enemies) == 0:
        print("The Players won!")
        for x in players:
            print(f"The surviors:\n {x}")

    elif len(players) == 0:
        print("The Goblins won!")
        for x in enemies:
            print(f"The surviors:\n {x}")

    

    
    