# Scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"Enemies inside functions: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


# Local Scope

def drink_potion():
    potion_strength = 2
    print(f"Potion strength value: {potion_strength}")


drink_potion()

# Global Scope

player_health = 10


def game():
    def health():
        health_potion = 10
        print(f"Health potion value: {health_potion}")

    health()


game()
print(f"Player health value: {player_health}")

# There is no Block Scope

game_level = 3


def create_enemy():
    enemy = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemy[0]

    print(new_enemy)


create_enemy()
# print(new_enemy)
