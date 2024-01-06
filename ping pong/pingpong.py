import pygame, sys, random

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 - 10
    ball.y = random.randint(10,100)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])

def point_won(winner):
    global cpu_points, player_points

    if winner == "cpu":
        cpu_points += 1
    if winner == "player":
        player_points += 1

    reset_ball()

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1

    if ball.right >= screen_width:
        point_won("cpu")

    if ball.left <= 0:
        point_won("player")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1
        collision.play()

def animate_player():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height

def animate_cpu():
    global cpu_speed
    cpu.y += cpu_speed

    if ball.centery <= cpu.centery:
        cpu_speed = -7
    if ball.centery >= cpu.centery:
        cpu_speed = 7

    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= screen_height:
        cpu.bottom = screen_height

pygame.init()

screen_width = 800
screen_height = 600
collision=pygame.mixer.Sound("resource/colli.wav") # add sound
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pingpongchingchong") # it's just a joke ( I'm Asian ) 
clock = pygame.time.Clock()

ball = pygame.Rect(0,0,30,30)
ball.center = (screen_width/2, screen_height/2)

cpu = pygame.Rect(0,0,20,100)
cpu.centery = screen_height/2

player = pygame.Rect(0,0,20,100)
player.midright = (screen_width, screen_height/2)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
cpu_speed = 7

cpu_points, player_points = 0, 0

score_font = pygame.font.Font(None, 75)

screen.fill((0,0,0))
#text
def text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
#main menu
menu=True
mode=1
textmode=''
button=pygame.font.Font(None,40)
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    button_1 = pygame.Rect(50, 100, 250, 50)
    button_2 = pygame.Rect(50, 200, 250, 50)
    pygame.draw.rect(screen, (192, 192, 192), button_1)
    pygame.draw.rect(screen, (192, 192, 192), button_2)
    text('MAIN MENU', pygame.font.Font(None,75), (255, 255, 255), screen, 20, 20)
    pos= pygame.mouse.get_pos()
    if mode==1:
        textmode='MOUSE'
    if mode==0:
        textmode='BUTTON'
    
    text('START', button, (255, 255, 255), screen, 80, 120)
    text(('MODE:' + textmode), button, (255, 255, 255), screen, 80, 220)
    if pygame.mouse.get_pressed()[0] == 1:
        if button_1.collidepoint(pos):
            menu=False
        if button_2.collidepoint(pos):
            mode=1-mode
    pygame.display.update()
    
run=True
quit=False
#ping pong game
while run:
    #Check if anyone win
    if cpu_points==5 or player_points==5:
        run=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit = True
        if mode==0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed = -7
                if event.key == pygame.K_DOWN:
                    player_speed = 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player_speed = 0
                    if event.key == pygame.K_DOWN:
                        player_speed = 0
    #Make paddle parallel with mouse ( if mouse)
    if mode==1:
        player = pygame.Rect((screen_width-20,pygame.mouse.get_pos()[1]),(20,100))
    if mode==0:
        pygame.Rect(0,0,20,100)
    #Change the positions of the game objects
    animate_ball()
    animate_player()
    animate_cpu()
        
    #Clear the screen
    screen.fill((0,128,0))

    #Draw the score
    cpu_score_surface = score_font.render(str(cpu_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")
    screen.blit(cpu_score_surface,(screen_width/4,20))
    screen.blit(player_score_surface,(3*screen_width/4,20))

    #Draw the game objects
    pygame.draw.aaline(screen,'white',(screen_width/2, 0), (screen_width/2, screen_height))
    pygame.draw.rect(screen,'white',cpu)
    pygame.draw.rect(screen,'white',player)
    pygame.draw.circle(screen,(192,192,192), (screen_width/2, screen_height/2), 100)
    pygame.draw.ellipse(screen,'white',ball)

    #Update the display
    pygame.display.update()
    clock.tick(60)
#result
if quit==False:
    winner=''
    if(cpu_points > player_points):
        winner="CPU IS THE WINNER"
    if(cpu_points < player_points):
        winner="HOOMAN IS THE WINNER"
    end_font=pygame.font.Font(None,25)
    end=True
    while end==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
        Truewinner = score_font.render(winner, True , (0,0,0))
        screen.blit((Truewinner),(screen_width/2-225, screen_height/2))
        pygame.display.update()
pygame.quit()
sys.exit()
