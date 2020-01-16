# imports pygame module
import pygame

# initializes pygame
pygame.init()

# define clock and fps
clock = pygame.time.Clock()
fps = 28

game_over = False

# screen class
class Screen:
    
    #constructor
    def __init__(self):
        self.width = 1000
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bg_img = pygame.image.load('Background.jpg')
        self.bg_img = pygame.transform.scale(self.bg_img, (self.width, self.height))
    
    # redraws all objects and images
    def redraw(self):
        self.screen.blit(self.bg_img, (0, 0))
        self.screen.blit(player.img, (player.x, player.y))
        # playerRect = pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y, player.width, player.height))
        pygame.display.update()

# player class
class Player:
    
    # constructor
    def __init__(self, x, y):
        # assign attributes to player
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.speed = 10
        self.left = False
        self.right = False
        self.jumping = False
        self.health = 10
        self.jump_count = 10
        self.stat_img = pygame.image.load('player.png')
        self.stat_img = pygame.transform.scale(self.stat_img, (self.width, self.height))
        self.images_move = ['player_right0.png', 'player_right1.png', 'player_right2.png', 'player_right3.png', 'player_right4.png', 'player_right5.png', 'player_right6.png']
        self.walkRight = []
        self.walkLeft = []
        self.walk_count = 0
        
        # define walkRight list and scale
        for images in self.images_move:
            img_item = pygame.image.load(images)
            self.walkRight.append(pygame.transform.scale(img_item, (self.width, self.height)))
        
        # define walkLeft list and scale
        for images in self.images_move:
            img_item = pygame.image.load(images)
            img_item = pygame.transform.flip(img_item, True, False)
            self.walkLeft.append(pygame.transform.scale(img_item, (self.width, self.height)))
    
    #update player
    def update(self):
        # defines game_over as global
        global game_over
        
        # 
        # get keys
        keys = pygame.key.get_pressed()
        
        # quits if escape key is pressed
        if keys[pygame.K_ESCAPE]:
            game_over = True

        # checks for left button input and keeps player on screen
        if keys[pygame.K_LEFT] and self.x > self.speed:
            self.x -= self.speed
            self.left = True
            self.right = False
        
        # checks for right button input and keeps player on screen
        elif keys[pygame.K_RIGHT] and self.x < screen.width - self.width - self.speed:
            self.x += self.speed
            self.right = True
            self.left = False
        
        # if not moving
        else:
            self.right = False
            self.left = False
        
        # test if space is pressed, and set jump to true
        if not self.jumping and keys[pygame.K_SPACE]:
            self.jumping = True
        
        # player jump
        if self.jumping:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.jumping = False
                self.jump_count = 10
        
        # reset walk count
        if self.walk_count >= 28:
            self.walk_count = 0
        
        # animation of player
        if self.right:
            self.img = self.walkRight[self.walk_count // 4]
            self.walk_count += 1
        elif self.left:
            self.img = self.walkLeft[self.walk_count // 4]
            self.walk_count += 1
        else:
            self.img = self.stat_img

# defining screen and player
screen = Screen()
player = Player(100, screen.height - 305)

# main game loop
while not game_over:
    
    # test for events
    for event in pygame.event.get():
        #quit if closed
        if event.type == pygame.QUIT:
            game_over = True
    
    # update player, redraw screen and tick clock
    player.update()
    screen.redraw()
    clock.tick(fps)

# quits if main loop is broken
pygame.quit()
