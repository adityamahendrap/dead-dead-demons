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
            obsRect.x -= 6
            
            if obsRect.bottom == onGround - 10:
                screen.blit(mobSurf_R, obsRect)
            else:
                screen.blit(flySurf_R, obsRect)
            
        obsList = [obs for obs in obsList if obs.x > -100]
        
        return obsList
    else:
        return[]

def obsMovL(obsList, onGround):
    if obsList:
        for obsRect in obsList:
            obsRect.x += 6
            
            if obsRect.bottom == onGround - 10:
                screen.blit(mobSurf_L, obsRect)
            else:
                screen.blit(flySurf_L, obsRect)
            
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

# def idleAnimation():
#     global idleSurf, idleIndex
    
#     idleIndex += 0.015
#     if idleIndex >= len(idle):
#         idleIndex = 0
#     idleSurf = idle[int(idleIndex)]

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("image")
clock = pygame.time.Clock()
gameActive = False
startTime = 0
score = 0
left = False
right = True
walkCount = 0

# Background.
skySurf = pygame.image.load("image/sky.png").convert()
groundSurf = pygame.image.load("image/ground.png").convert()
onGround = 325

font = pygame.font.Font("font/SFAtarian.ttf", 50)


# Player.
playerSurf_R = pygame.image.load("image/playerR.png").convert_alpha()
playerWalk_R1 = pygame.image.load("walk/R/walk1.png").convert_alpha()
playerWalk_R2 = pygame.image.load("walk/R/walk2.png").convert_alpha()
playerWalk_R3 = pygame.image.load("walk/R/walk3.png").convert_alpha()
playerWalk_R4 = pygame.image.load("walk/R/walk4.png").convert_alpha()
playerWalk_R5 = pygame.image.load("walk/R/walk5.png").convert_alpha()
playerWalk_R6 = pygame.image.load("walk/R/walk6.png").convert_alpha()
playerWalk_R7 = pygame.image.load("walk/R/walk7.png").convert_alpha()
playerWalk_R8 = pygame.image.load("walk/R/walk8.png").convert_alpha()
playerWalk_R9 = pygame.image.load("walk/R/walk9.png").convert_alpha()
playerWalk_R10 = pygame.image.load("walk/R/walk10.png").convert_alpha()
playerWalk_R11 = pygame.image.load("walk/R/walk11.png").convert_alpha()
playerWalk_R12 = pygame.image.load("walk/R/walk12.png").convert_alpha()
playerFrames_R = [playerWalk_R1, playerWalk_R2, playerWalk_R3, playerWalk_R4, playerWalk_R5, playerWalk_R6, playerWalk_R7, playerWalk_R8, playerWalk_R9, playerWalk_R10, playerWalk_R11, playerWalk_R12]
playerFramesIndex_R = 0

playerSurf_L = pygame.image.load("image/playerL.png").convert_alpha()
playerWalk_L1 = pygame.image.load("walk/L/walk1.png").convert_alpha()
playerWalk_L2 = pygame.image.load("walk/L/walk2.png").convert_alpha()
playerWalk_L3 = pygame.image.load("walk/L/walk3.png").convert_alpha()
playerWalk_L4 = pygame.image.load("walk/L/walk4.png").convert_alpha()
playerWalk_L5 = pygame.image.load("walk/L/walk5.png").convert_alpha()
playerWalk_L6 = pygame.image.load("walk/L/walk6.png").convert_alpha()
playerWalk_L7 = pygame.image.load("walk/L/walk7.png").convert_alpha()
playerWalk_L8 = pygame.image.load("walk/L/walk8.png").convert_alpha()
playerWalk_L9 = pygame.image.load("walk/L/walk9.png").convert_alpha()
playerWalk_L10 = pygame.image.load("walk/L/walk10.png").convert_alpha()
playerWalk_L11 = pygame.image.load("walk/L/walk11.png").convert_alpha()
playerWalk_L12 = pygame.image.load("walk/L/walk12.png").convert_alpha()
playerFrames_L = [playerWalk_L1, playerWalk_L2, playerWalk_L3, playerWalk_L4, playerWalk_L5, playerWalk_L6, playerWalk_L7, playerWalk_L8, playerWalk_L9, playerWalk_L10, playerWalk_L11, playerWalk_L12]
playerFramesIndex_L = 0

playerJump_R = pygame.image.load("jump/jumpR.png").convert_alpha()
playerJump_L = pygame.image.load("jump/jumpL.png").convert_alpha()

# playerJump = pygame.image.load("image/jumpL.png").convert_alpha()
playerRect = playerSurf_R.get_rect(midbottom= (WIDTH/2, onGround))
playerGravity = 0

playerImage = playerSurf_R

idleSurf = playerSurf_R
idleRect = idleSurf.get_rect(midbottom= (WIDTH/2 - 3, onGround))

# Obstacles.

mobFrame_R1 = pygame.image.load("image/mobR.png").convert_alpha()
mobFrame_R1.set_alpha(150)
mobFrame_R2 = pygame.image.load("image/mobR2.png").convert_alpha()
mobFrames_R = [mobFrame_R1, mobFrame_R2]
mobFramesIndex_R = 0
mobSurf_R = mobFrames_R[mobFramesIndex_R]

# mobSurf = pygame.image.load("image/mobR.png").convert_alpha()
# mobRect = mobSurf.get_rect(bottomleft= (1000, onGround - 10)) 

mobFrame_L1 = pygame.image.load("image/mobL.png").convert_alpha()
mobFrame_L2 = pygame.image.load("image/mobL2.png").convert_alpha()
mobFrames_L = [mobFrame_L1, mobFrame_L2]
mobFramesIndex_L = 0
mobSurf_L = mobFrames_L[mobFramesIndex_L]

# mobLSurf = pygame.image.load("image/mobL.png").convert_alpha()
# mobLRect = mobLSurf.get_rect(bottomleft= (-200, onGround - 10)) 

flyFrame_R1 = pygame.image.load("image/flyR.png").convert_alpha()
flyFrame_R2 = pygame.image.load("image/flyR2.png").convert_alpha()
flyFrames_R = [flyFrame_R1, flyFrame_R2]
flyFramesIndex_R = 0
flySurf_R = flyFrames_R[flyFramesIndex_R]

# flySurf = pygame.image.load("image/flyR.png").convert_alpha()
# flyRect = flySurf.get_rect(bottomleft= (1000, 150))

flyFrame_L1 = pygame.image.load("image/flyL.png").convert_alpha()
flyFrame_L2 = pygame.image.load("image/flyL2.png").convert_alpha()
flyFrames_L = [flyFrame_L1, flyFrame_L2]
flyFramesIndex_L = 0
flySurf_L = flyFrames_L[flyFramesIndex_L]

# flyLSurf = pygame.image.load("image/flyL.png").convert_alpha()
# flyLRect = flyLSurf.get_rect(bottomleft= (-200, 150))

obsRectList = []
obsRectListL = []

# Timer.
obsTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obsTimer, randint(1400, 2500))

flyAnimationTimer = pygame.USEREVENT + 2
pygame.time.set_timer(flyAnimationTimer, randint(300, 500))

flyAnimationTimer2 = pygame.USEREVENT + 3
pygame.time.set_timer(flyAnimationTimer2, randint(300, 500))

mobAnimationTimer = pygame.USEREVENT + 4
pygame.time.set_timer(mobAnimationTimer, randint(1000, 2000))

mobAnimationTimer2 = pygame.USEREVENT + 5
pygame.time.set_timer(mobAnimationTimer2, randint(1000, 2000))




# GAME LOOP.
while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        
        # keys = pygame.key.get_pressed()
        
        # right = True
        
        # if event.type == playerAnimationTimer:
        #     if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #         playerFramesIndex_R = 1
        #         playerImage = playerFrames_R[playerFramesIndex_R]
        #         # playerImage = playerSurf_R
                
        #     if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #         playerImage = playerSurf_L
        
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        #         playerImage = playerSurf_R
        #     if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        #         playerImage = playerSurf_L
            
        
        if gameActive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                    if playerRect.bottom == onGround:
                        playerGravity = -20
                        print("jump") 
        else: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameActive = True
                    startTime = int(pygame.time.get_ticks()/100)
                    
                    
                    
        if gameActive:
            if event.type == obsTimer:
                if randint(0, 2):
                    obsRectList.append(mobSurf_R.get_rect(bottomleft= (randint(800, 1100), onGround - 10)))
                else:
                    obsRectList.append(flySurf_R.get_rect(bottomleft= (randint(900, 1100), 150)))
                    
                if randint(0, 2):
                    obsRectListL.append(mobSurf_L.get_rect(bottomleft= (randint(-300, -100), onGround - 10)))
                else:
                    obsRectListL.append(flySurf_L.get_rect(bottomleft= (randint(-300, -100), 150)))
                    
            if event.type == flyAnimationTimer:
                # Right Fly Animation
                if flyFramesIndex_R == 0:
                    flyFramesIndex_R = 1
                else:
                    flyFramesIndex_R = 0
                flySurf_R = flyFrames_R[flyFramesIndex_R]
                
            if event.type == flyAnimationTimer2:
                # Left Fly Animation
                if flyFramesIndex_L == 0:
                    flyFramesIndex_L = 1
                else:
                    flyFramesIndex_L = 0
                flySurf_L = flyFrames_L[flyFramesIndex_L]
                
            if event.type == mobAnimationTimer:
                # Right Mob Animation
                if mobFramesIndex_R == 0:
                    mobFramesIndex_R = 1
                else:
                    mobFramesIndex_R = 0
                mobSurf_R = mobFrames_R[mobFramesIndex_R]
            
            if event.type == mobAnimationTimer2:
                # Left Mob Animation
                if mobFramesIndex_L == 0:
                    mobFramesIndex_L = 1
                else:
                    mobFramesIndex_L = 0
                mobSurf_L = mobFrames_L[mobFramesIndex_L]
            
            
# Control.

    keys = pygame.key.get_pressed()
    
    if right:
        playerImage = playerSurf_R
    elif left:
        playerImage = playerSurf_L
    
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        
        right = True
        left = False
        # player = pygame.image.load(images[counter])
        # counter = (counter + 1) % len(images)
        
        idleSurf = playerSurf_R
        
        playerImage = playerFrames_R[playerFramesIndex_R]
        playerFramesIndex_R = (playerFramesIndex_R + 1) % len(playerFrames_R)
        playerRect.x += 7
        
    
        
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        left = True
        right = False
        
        idleSurf = playerSurf_L
        
        playerImage = playerFrames_L[playerFramesIndex_L]
        playerFramesIndex_L = (playerFramesIndex_L + 1) % len(playerFrames_L)
        playerRect.x -= 7
        
    if playerRect.bottom < onGround:
        if right:
            playerImage = playerJump_R
        if left:
            playerImage = playerJump_L
    # else:
    #     playerImage = idle_L
        
    
        
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
        

        
        screen.blit(playerImage, playerRect)
        # if right:
        #     screen.blit(playerFrames_R, playerRect)
        # elif left:
        #     screen.blit(playerSurf_L, playerRect)
        # else:
        #     screen.blit(idle_R, playerRect)
        
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
        
        # idleAnimation()
        screen.blit(idleSurf, idleRect)
        
        if score == 0:
            screen.blit(introSurf, introRect)
        else:
            screen.blit(overSurface, overRect)
            screen.blit(scoreMsgSurf, scoreMsgRect)
    
    pygame.display.update()
    clock.tick(60)
