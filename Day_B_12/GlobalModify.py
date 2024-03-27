# Modifying Global Score

enemies = 1


def increase_enemies():
    # global enemies
    # enemies += 1
    print(f"Enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@csajkasnorbert"


def calc():
    pass

