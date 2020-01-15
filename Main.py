import pygame

pygame.init()

screen_width, screen_height = 1680, 1050
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
fps = 60

game_over = False

class Player:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.speed = 10
        self.left = False
        self.right = False
        self.jumping = False
        self.health = 10
        
    
player = Player(100, 900)


while not game_over:

    keys = pygame.key.get_pressed()
    
    if keys[ord("W")]:
        player.x -= player.speed
    elif keys[ord("S")]:
        player.x += player.speed
    if keys[ord("A")]:
        player.y -= player.speed
        player.left = True
    elif keys[ord("D")]:
        player.y += player.speed
        player.right = True
    
    screen.fill((0,0,255))
    
    playerRect = pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y, player.width, player.height))
    pygame.display.update()
    clock.tick(fps)
    
    
