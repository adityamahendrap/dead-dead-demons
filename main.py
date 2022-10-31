import pygame
from random import randint

def displayScore():
    currentTime = int(pygame.time.get_ticks()/100) - startTime
    scoreSurf = font.render(f'{currentTime}', True, "black")
    scoreRect = scoreSurf.get_rect(topleft = (0, 0))
    screen.blit(scoreSurf, scoreRect)
    return currentTime
    
def obsMov(obsList, onGround):
    if obsList:
        for obsRect in obsList:
            obsRect.x -= 4
            
            if obsRect.bottom == onGround - 10:
                screen.blit(mobSurf, obsRect)
            else:
                screen.blit(flySurf_R, obsRect)
            
        obsList = [obs for obs in obsList if obs.x > -100]
        
        return obsList
    else:
        return[]

def obsMovL(obsList, onGround):
    if obsList:
        for obsRect in obsList:
            obsRect.x += 4
            
            if obsRect.bottom == onGround - 10:
                screen.blit(mobLSurf, obsRect)
            else:
                screen.blit(flyLSurf, obsRect)
            
        obsList = [obs for obs in obsList if obs.x < 900]
        
        return obsList
    else:
        return[]

def checkCol(player, obs):
    if obs:
        for obsRect in obs:
            if player.colliderect(obsRect): 
                return False
    return True

def idleAnimation():
    global idleSurf, idleIndex
    
    idleIndex += 0.015
    if idleIndex >= len(idle):
        idleIndex = 0
    idleSurf = idle[int(idleIndex)]
    

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("image")
clock = pygame.time.Clock()
gameActive = False
startTime = 0
score = 0

# Background.
skySurf = pygame.image.load("image/sky.png").convert()
groundSurf = pygame.image.load("image/ground.png").convert()
onGround = 325

font = pygame.font.Font("font/SFAtarian.ttf", 50)

idle_R = pygame.image.load("image/idleR.png").convert_alpha()
idle_L = pygame.image.load("image/idleL.png").convert_alpha()
idle = [idle_R, idle_L]
idleIndex = 0

idleSurf = idle[idleIndex]
idleRect = idleSurf.get_rect(bottomleft= (WIDTH/2 -32, onGround))

# Player.
playerSurf = pygame.image.load("image/playerR.png").convert_alpha()
playerLSurf = pygame.image.load("image/playerR.png").convert_alpha()
playerRect = playerSurf.get_rect(bottomleft= (WIDTH/2 -32, onGround))
playerGravity = 0

# Obstacles.
mobSurf = pygame.image.load("image/mobR.png").convert_alpha()
# mobRect = mobSurf.get_rect(bottomleft= (1000, onGround - 10)) 

mobLSurf = pygame.image.load("image/mobL.png").convert_alpha()
# mobLRect = mobLSurf.get_rect(bottomleft= (-200, onGround - 10)) 

flyFrame_R1 = pygame.image.load("image/flyR.png").convert_alpha()
flyFrame_R2 = pygame.image.load("image/flyR2.png").convert_alpha()
flyFrames_R = [flyFrame_R1, flyFrame_R2]
flyFramesIndex_R = 0
flySurf_R = flyFrames_R[flyFramesIndex_R]


# flySurf = pygame.image.load("image/flyR.png").convert_alpha()
# flyRect = flySurf.get_rect(bottomleft= (1000, 150))

flyLSurf = pygame.image.load("image/flyL.png").convert_alpha()
# flyLRect = flyLSurf.get_rect(bottomleft= (-200, 150))

obsRectList = []
obsRectListL = []

# Timer.
obsTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obsTimer, randint(1400, 2500))

flyAnimationTimer = pygame.USEREVENT + 2
pygame.time.set_timer(flyAnimationTimer, 300)

# GAME LOOP.
while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if gameActive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if playerRect.bottom == onGround:
                        playerGravity = -20
                        print("space pressed")
        else: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameActive = True
                    startTime = int(pygame.time.get_ticks()/100)
        
        if event.type == obsTimer and gameActive:
            if randint(0, 2):
                obsRectList.append(mobSurf.get_rect(bottomleft= (randint(800, 1100), onGround - 10)))
            else:
                obsRectList.append(flySurf_R.get_rect(bottomleft= (randint(900, 1100), 150)))
                
            if randint(0, 2):
                obsRectListL.append(mobLSurf.get_rect(bottomleft= (randint(-300, -100), onGround - 10)))
            else:
                obsRectListL.append(flyLSurf.get_rect(bottomleft= (randint(-300, -100), 150)))

# Control.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        playerRect.x += 7
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        playerRect.x -= 7
        
    if playerRect.left < 0:
        playerRect.left = 0
    if playerRect.right > WIDTH:
        playerRect.right = WIDTH

# UPDATE.
    if gameActive:
        
        # Gravity.
        playerGravity += 1
        playerRect.y += playerGravity
        if playerRect.bottom >= onGround:
            playerRect.bottom = onGround
        
        # Colliision.
        # if mobRect.colliderect(playerRect):
        #     print("z")
        #     gameActive = False
    
        # DRAW.
        screen.blit(skySurf, (0, 0))
        screen.blit(groundSurf, (0, onGround))
        screen.blit(playerSurf, playerRect)
        
        obsRectList = obsMov(obsRectList, onGround)
        obsRectListL = obsMovL(obsRectListL, onGround)
        
        # screen.blit(mobSurf, mobRect)
        # mobRect.left += -5
        # if mobRect.left < -72:
        #     mobRect.left = WIDTH
        
        # screen.blit(flySurf, flyRect)
        
        if gameActive:
            gameActive = checkCol(playerRect, obsRectList)
        if gameActive:
            gameActive = checkCol(playerRect, obsRectListL)
        
        score = displayScore()

    else:
        
        
        screen.blit(skySurf, (0, 0))
        screen.blit(groundSurf, (0, onGround))
        
        
        obsRectList.clear()
        obsRectListL.clear()
        
        playerRect.bottomleft = (WIDTH/2 - 24, onGround)
        playerGravity = 0
        
        overFont = pygame.font.Font("font/SFAtarian.ttf", 125)
        overSurface = overFont.render("GAME OVER", True, "black")
        overRect = overSurface.get_rect(center= (WIDTH/2, HEIGHT/2 - 70))
        scoreMsgSurf = font.render(f'Your Score : {score}', True, "black")
        scoreMsgRect = scoreMsgSurf.get_rect(center= (WIDTH/2, HEIGHT/2))
        
        
        introSurf = overFont.render("AVOID THE BICH", True, "black")
        introRect = introSurf.get_rect(center= (WIDTH/2, HEIGHT/2 - 70))
        
        idleAnimation()
        screen.blit(idleSurf, idleRect)
        
        
        if score == 0:
            screen.blit(introSurf, introRect)
        else:
            screen.blit(overSurface, overRect)
            screen.blit(scoreMsgSurf, scoreMsgRect)
            
    
    
    pygame.display.update()
    clock.tick(90)