################### Scope ####################

enemies = 1


def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # error

# global scope
player_health = 10
def game():
    def drink_potions():
        potion_strength = 2
        print(player_health)
    drink_potions()

drink_potions()
print(player_health)

# there is no block scope in python

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # perfectly fine

# how to modify global variable

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

def increase():
    return enemies + 1
enemies = increase()

# global constants
PI = 3.141596254