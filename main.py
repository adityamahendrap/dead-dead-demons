import pygame as py
from random import randint

def displayScore():
    currentTime = int(py.time.get_ticks()/100) - startTime
    scoreSurf = font.render(f'{currentTime}', True, "white")
    scoreSurf.set_alpha(150)
    scoreRect = scoreSurf.get_rect(topleft = (5, 5))
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
    
def introScreen():
    screen.blit(introSurf, introRect)
    screen.blit(playSurf, playRect)
    screen.blit(highSoreSurf, highSoreRect)

def gameOverScreen():
    screen.blit(overSurf, overRect)
    screen.blit(scoreMsgSurf, scoreMsgRect)
    screen.blit(playSurf2, playRect2)
    screen.blit(highSoreSurf, highSoreRect2)
    
py.mixer.init(44100, -16, 2, 64)
py.init()
WIDTH, HEIGHT = 800, 400
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Ghost Yeeter")
clock = py.time.Clock()
gameActive = False
startTime = 0
score = 0
left = False
right = True
walkCount = 0
onGround = 325
playerGravity = 0

# Read High Score
f = open("data/high_score.txt", "r")
if f.readline() is not '':
    highScore = int(f.readline())
else: highScore = 0
f.close()

# Environment.
skySurf = py.image.load("assets/img/bg/background.png").convert()
skySurf = py.transform.scale(skySurf, (928 *1.25, 431 *1.25))
groundSurf = py.image.load("assets/img/bg/floor1.png").convert_alpha()
groundSurf2 = py.image.load("assets/img/bg/floor2.png").convert_alpha()

# Font.
font = py.font.Font("assets/font/SFAtarian.ttf", 35)
fontPlay = py.font.Font("assets/font/SFAtarian.ttf", 20)
overFont = py.font.Font("assets/font/SFAtarian.ttf", 125)

# Player.
playerSurf_R = py.image.load("assets/img/sprite/playerR.png").convert_alpha()
playerWalk_R1 = py.image.load("assets/img/sprite/walk/R/walk1.png").convert_alpha()
playerWalk_R2 = py.image.load("assets/img/sprite/walk/R/walk2.png").convert_alpha()
playerWalk_R3 = py.image.load("assets/img/sprite/walk/R/walk3.png").convert_alpha()
playerWalk_R4 = py.image.load("assets/img/sprite/walk/R/walk4.png").convert_alpha()
playerWalk_R5 = py.image.load("assets/img/sprite/walk/R/walk5.png").convert_alpha()
playerWalk_R6 = py.image.load("assets/img/sprite/walk/R/walk6.png").convert_alpha()
playerWalk_R7 = py.image.load("assets/img/sprite/walk/R/walk7.png").convert_alpha()
playerWalk_R8 = py.image.load("assets/img/sprite/walk/R/walk8.png").convert_alpha()
playerWalk_R9 = py.image.load("assets/img/sprite/walk/R/walk9.png").convert_alpha()
playerWalk_R10 = py.image.load("assets/img/sprite/walk/R/walk10.png").convert_alpha()
playerWalk_R11 = py.image.load("assets/img/sprite/walk/R/walk11.png").convert_alpha()
playerWalk_R12 = py.image.load("assets/img/sprite/walk/R/walk12.png").convert_alpha()
playerFrames_R = [playerWalk_R1, playerWalk_R2, playerWalk_R3, playerWalk_R4, playerWalk_R5, playerWalk_R6, playerWalk_R7, playerWalk_R8, playerWalk_R9, playerWalk_R10, playerWalk_R11, playerWalk_R12]
playerFramesIndex_R = 0

playerSurf_L = py.image.load("assets/img/sprite/playerL.png").convert_alpha()
playerWalk_L1 = py.image.load("assets/img/sprite/walk/L/walk1.png").convert_alpha()
playerWalk_L2 = py.image.load("assets/img/sprite/walk/L/walk2.png").convert_alpha()
playerWalk_L3 = py.image.load("assets/img/sprite/walk/L/walk3.png").convert_alpha()
playerWalk_L4 = py.image.load("assets/img/sprite/walk/L/walk4.png").convert_alpha()
playerWalk_L5 = py.image.load("assets/img/sprite/walk/L/walk5.png").convert_alpha()
playerWalk_L6 = py.image.load("assets/img/sprite/walk/L/walk6.png").convert_alpha()
playerWalk_L7 = py.image.load("assets/img/sprite/walk/L/walk7.png").convert_alpha()
playerWalk_L8 = py.image.load("assets/img/sprite/walk/L/walk8.png").convert_alpha()
playerWalk_L9 = py.image.load("assets/img/sprite/walk/L/walk9.png").convert_alpha()
playerWalk_L10 = py.image.load("assets/img/sprite/walk/L/walk10.png").convert_alpha()
playerWalk_L11 = py.image.load("assets/img/sprite/walk/L/walk11.png").convert_alpha()
playerWalk_L12 = py.image.load("assets/img/sprite/walk/L/walk12.png").convert_alpha()
playerFrames_L = [playerWalk_L1, playerWalk_L2, playerWalk_L3, playerWalk_L4, playerWalk_L5, playerWalk_L6, playerWalk_L7, playerWalk_L8, playerWalk_L9, playerWalk_L10, playerWalk_L11, playerWalk_L12]
playerFramesIndex_L = 0

playerJump_R = py.image.load("assets/img/sprite/jump/jumpR.png").convert_alpha()
playerJump_L = py.image.load("assets/img/sprite/jump/jumpL.png").convert_alpha()

playerRect = playerSurf_R.get_rect(midbottom= (WIDTH/2, onGround))
playerImage = playerSurf_R

idleSurf = playerSurf_R
idleRect = idleSurf.get_rect(midbottom= (WIDTH/2 - 3, onGround))

# Obstacles.
mobFrame_R1 = py.image.load("assets/img/sprite/mobR.png").convert_alpha()
mobFrame_R1.set_alpha(150)
mobFrame_R2 = py.image.load("assets/img/sprite/mobR2.png").convert_alpha()
mobFrame_R2.set_alpha(150)
mobFrames_R = [mobFrame_R1, mobFrame_R2]
mobFramesIndex_R = 0
mobSurf_R = mobFrames_R[mobFramesIndex_R]

mobFrame_L1 = py.image.load("assets/img/sprite/mobL.png").convert_alpha()
mobFrame_L1.set_alpha(150)
mobFrame_L2 = py.image.load("assets/img/sprite/mobL2.png").convert_alpha()
mobFrame_L2.set_alpha(150)
mobFrames_L = [mobFrame_L1, mobFrame_L2]
mobFramesIndex_L = 0
mobSurf_L = mobFrames_L[mobFramesIndex_L]

flyFrame_R1 = py.image.load("assets/img/sprite/flyR.png").convert_alpha()
flyFrame_R1.set_alpha(150)
flyFrame_R2 = py.image.load("assets/img/sprite/flyR2.png").convert_alpha()
flyFrame_R2.set_alpha(150)
flyFrames_R = [flyFrame_R1, flyFrame_R2]
flyFramesIndex_R = 0
flySurf_R = flyFrames_R[flyFramesIndex_R]

flyFrame_L1 = py.image.load("assets/img/sprite/flyL.png").convert_alpha()
flyFrame_L1.set_alpha(150)
flyFrame_L2 = py.image.load("assets/img/sprite/flyL2.png").convert_alpha()
flyFrame_L2.set_alpha(150)
flyFrames_L = [flyFrame_L1, flyFrame_L2]
flyFramesIndex_L = 0
flySurf_L = flyFrames_L[flyFramesIndex_L]

obsRectList = []
obsRectListL = []

# Sound.
jumpSound = py.mixer.Sound("assets/sound/jump.mp3")
music = py.mixer.music.load("assets/sound/forest.mp3")
py.mixer.music.play(-1)
# Timer.
obsTimer = py.USEREVENT + 1
py.time.set_timer(obsTimer, randint(1400, 2500))

flyAnimationTimer = py.USEREVENT + 2
py.time.set_timer(flyAnimationTimer, randint(300, 500))

flyAnimationTimer2 = py.USEREVENT + 3
py.time.set_timer(flyAnimationTimer2, randint(300, 500))

mobAnimationTimer = py.USEREVENT + 4
py.time.set_timer(mobAnimationTimer, randint(1000, 2000))

mobAnimationTimer2 = py.USEREVENT + 5
py.time.set_timer(mobAnimationTimer2, randint(1000, 2000))

# Game Loop.
while True:
    screen.fill((0, 0, 0))
    
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
            
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
                exit()

        if gameActive:
            # Set Player Jump
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE or event.key == py.K_UP or event.key == py.K_w:
                    if playerRect.bottom == onGround:
                        jumpSound.play()
                        playerGravity = -20
                        
        else: 
            # Score Start Counter.
            if event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    gameActive = True
                    startTime = int(py.time.get_ticks()/100)
                    
        if gameActive:
            # Obstacle Spawn Random Position.
            if event.type == obsTimer:
                if randint(0, 2):
                    obsRectList.append(mobSurf_R.get_rect(bottomleft= (randint(800, 1100), onGround - 10)))
                else:
                    obsRectList.append(flySurf_R.get_rect(bottomleft= (randint(900, 1100), 150)))
                if randint(0, 2):
                    obsRectListL.append(mobSurf_L.get_rect(bottomleft= (randint(-300, -100), onGround - 10)))
                else:
                    obsRectListL.append(flySurf_L.get_rect(bottomleft= (randint(-300, -100), 150)))
            # Right Fly Obstacle Animation
            if event.type == flyAnimationTimer:
                if flyFramesIndex_R == 0:
                    flyFramesIndex_R = 1
                else:
                    flyFramesIndex_R = 0
                flySurf_R = flyFrames_R[flyFramesIndex_R]
            # Left Fly Obstacle Animation.
            if event.type == flyAnimationTimer2:
                if flyFramesIndex_L == 0:
                    flyFramesIndex_L = 1
                else:
                    flyFramesIndex_L = 0
                flySurf_L = flyFrames_L[flyFramesIndex_L]
            # Right Mob Obstacle Animation
            if event.type == mobAnimationTimer:
                if mobFramesIndex_R == 0:
                    mobFramesIndex_R = 1
                else:
                    mobFramesIndex_R = 0
                mobSurf_R = mobFrames_R[mobFramesIndex_R]
            # Left Mob Obstacle Animation
            if event.type == mobAnimationTimer2:
                if mobFramesIndex_L == 0:
                    mobFramesIndex_L = 1
                else:
                    mobFramesIndex_L = 0
                mobSurf_L = mobFrames_L[mobFramesIndex_L]

    keys = py.key.get_pressed()

    # Set Player Idle Frame GameActive = 1.
    if right:
        playerImage = playerSurf_R
    elif left:
        playerImage = playerSurf_L
    
    if keys[py.K_RIGHT] or keys[py.K_d]:
        # Set Direction Bool
        right = True
        left = False
        # Set Player Idle Frame GameActive = 0.
        idleSurf = playerSurf_R
        # Player Movement to Right Animation.
        playerImage = playerFrames_R[playerFramesIndex_R]
        playerFramesIndex_R = (playerFramesIndex_R + 1) % len(playerFrames_R)
        # Speed Player Movement to Right
        playerRect.x += 7
        
    elif keys[py.K_LEFT] or keys[py.K_a]:
        # Set Direction Bool
        left = True
        right = False
        # Set Player Idle Frame GameActive = 0.
        idleSurf = playerSurf_L
        # Player Movement to Left Animation.
        playerImage = playerFrames_L[playerFramesIndex_L]
        playerFramesIndex_L = (playerFramesIndex_L + 1) % len(playerFrames_L)
        playerRect.x -= 7
        
    # Set Player Jamp Frame.
    if playerRect.bottom < onGround:
        if right:
            playerImage = playerJump_R
        if left:
            playerImage = playerJump_L
            
    # Cancel Player Offset from Screen
    if playerRect.left < 0:
        playerRect.left = 0
    if playerRect.right > WIDTH:
        playerRect.right = WIDTH

    if gameActive:
        # Apply Gravity.
        playerGravity += 1
        playerRect.y += playerGravity
        # Set Player Landing
        if playerRect.bottom >= onGround:
            playerRect.bottom = onGround
    
        # Draw Player & Environment GameActive = 1.
        screen.blit(skySurf, (0, -140))
        screen.blit(playerImage, playerRect)
        screen.blit(groundSurf, (0, onGround - 25))
        screen.blit(groundSurf2, (0, onGround - 10))
        screen.blit(groundSurf2, (0, onGround + 20))
        
        # Spawm Obstacle.
        obsRectList = obsMov(obsRectList, onGround)
        obsRectListL = obsMovL(obsRectListL, onGround)
        
        # Player & Obstacle Collision Check
        if gameActive:
            gameActive = checkCol(playerRect, obsRectList)
        if gameActive:
            gameActive = checkCol(playerRect, obsRectListL)
        
        # Display Score Counter
        score = displayScore()
    else:
        # Draw Player & Environment GameActive = 0.
        screen.blit(skySurf, (0, -140))
        screen.blit(idleSurf, idleRect)
        screen.blit(groundSurf, (0, onGround - 25))
        screen.blit(groundSurf2, (0, onGround - 10))
        screen.blit(groundSurf2, (0, onGround + 20))
        
        # Disable Obstacle.
        obsRectList.clear()
        obsRectListL.clear()
        
        # Set Default Player Position.
        playerGravity = 0
        playerRect.bottomleft = (WIDTH/2 - 24, onGround)
        
        # Set Intro Text.
        introSurf = overFont.render("GHOST YEETER", True, "white")
        introSurf.set_alpha(150)
        introRect = introSurf.get_rect(center= (WIDTH/2, HEIGHT/2 - 20))
        
        # Set Start Game Menu
        playSurf = fontPlay.render("press ENTER to play", True, "white")
        playSurf.set_alpha(150)
        playRect = playSurf.get_rect(center= (WIDTH/2, HEIGHT - 30))

        # High Score Check
        if score > highScore:
            highScore = score
        
        # Set Highscore Menu
        highSoreSurf = fontPlay.render(f"HIGH SCORE: {highScore}", True, "white")
        highSoreSurf.set_alpha(150)
        highSoreRect = highSoreSurf.get_rect(center= (WIDTH/2, 125))
        highSoreRect2 = highSoreSurf.get_rect(center= (WIDTH/2, 68))
        
        # Set Text When Game Over.
        overSurf = overFont.render("GAME OVER", True, "white")
        overSurf.set_alpha(150)
        overRect = overSurf.get_rect(center= (WIDTH/2, HEIGHT/2 - 20))
        
        # Set Show Final Score.
        scoreMsgSurf = font.render(f'your score : {score}', True, "white")
        scoreMsgSurf.set_alpha(150)
        scoreMsgRect = scoreMsgSurf.get_rect(center= (WIDTH/2, 40))
        
        # Set How to Play Again.
        playSurf2 = fontPlay.render("press ENTER to play again", True, "white")
        playSurf2.set_alpha(150)
        playRect2 = playSurf2.get_rect(center= (WIDTH/2, HEIGHT - 30))
        
        if score == 0:
            # Display when Intro
            introScreen()
        else:
            # Display when Game Over
            gameOverScreen()
            
    py.display.update()
    clock.tick(60)
    
    f = open("data/high_score.txt", "w")
    f.write(f"{highScore}")
    f.close() 
