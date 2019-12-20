import pygame

pygame.init()

taustavärv = (255,255,150)
väljak_x = 700
väljak_y = 700
x1 = 350
y1 = 600
x2 = 600
y2 = 350
x_seier = 1
y_seier = 0
samm = 5
menüü = 1
mäng = 0
punktekokku = 0
uusmäng = 0
mitmesvise = 1
helehall = (220,220,220)
hall = (150,150,150)
tumehall = (75,75,75)
raskusaste = 2

win = pygame.display.set_mode((väljak_x,väljak_y))

pygame.display.set_caption("Noolem2ng")

def kirjuta(tekst, suurus, asukoht, taust = taustavärv, värv = (0,0,0)):
    font = pygame.font.Font('freesansbold.ttf', suurus)
    text = font.render(tekst, True, värv, taust)
    textRect = text.get_rect()
    textRect.center = asukoht
    win.blit(text, textRect)

def mängulaud():
    win.fill(taustavärv)
    keskpunkt_x = väljak_x // 2
    keskpunkt_y = väljak_y // 2
    raadius = 200
    misvärvi = 0
    while raadius >= 20:
        värv = (255, 255, 255)
        if misvärvi % 2 != 0:
            värv = (0,0,0)
        if misvärvi == 9:
            värv = (255,0,0)
        pygame.draw.circle(win, värv, (keskpunkt_x, keskpunkt_y), raadius)
        raadius -= 20
        misvärvi += 1

def menyy():
    win.fill(taustavärv)
    kirjuta("Mängujuhend:", 15,(350,250))
    kirjuta("Et määrata noole suund viskamisel, vajuta SPACEBAR", 15, (350, 270))
    kirjuta("Et määrata noole kõrgus viskamisel, vajuta ENTER", 15, (350, 290))
    kirjuta("Mängijal on 10 viset", 15, (350, 310))
    kirjuta("Noolemäng", 72, (350,200))
    pygame.draw.rect(win, (0,200,0), (200,350,150,100))
    kirjuta("Mängi",24, (275,400), (0,200,0))
    pygame.draw.rect(win, (200,0,0), (350,350,150,100))
    kirjuta("Välju",24, (425,400), (200,0,0))
    if 200 <= mouseX <= 350 and 350 <= mouseY <= 500:
        pygame.draw.rect(win, (0,255,0), (200,350,150,100))
        kirjuta("Mängi",24, (275,400), (0,255,0), (255,255,255))
    if 350 <= mouseX <= 500 and 350 <= mouseY <= 500:
        pygame.draw.rect(win, (255,0,0), (350,350,150,100))
        kirjuta("Välju",24, (425,400), (255,0,0), (255,255,255))
    pygame.draw.rect(win, helehall, (180,500,100,40))
    kirjuta("Kerge", 20, (230,520), helehall)
    pygame.draw.rect(win, helehall, (290,500,120,40))
    kirjuta("Keskmine", 20, (350,520), helehall)
    pygame.draw.rect(win, helehall, (420,500,100,40))
    kirjuta("Raske", 20, (470,520), helehall)
    if 180 <= mouseX <= 280 and 500 <= mouseY <= 540 and raskusaste != 1:
        pygame.draw.rect(win, hall, (180,500,100,40))
        kirjuta("Kerge", 20, (230,520), hall)
    if 290 <= mouseX <= 410 and 500 <= mouseY <= 540 and raskusaste != 1:
        pygame.draw.rect(win, hall, (290,500,120,40))
        kirjuta("Keskmine", 20, (350,520), hall)
    if 420 <= mouseX <= 520 and 500 <= mouseY <= 540 and raskusaste != 1:
        pygame.draw.rect(win, hall, (420,500,100,40))
        kirjuta("Raske", 20, (470,520), hall)
    if raskusaste == 1:
        pygame.draw.rect(win, tumehall, (180,490,100,60))
        kirjuta("Kerge", 20, (230,520), tumehall, (255,255,255))
    if raskusaste == 2:
        pygame.draw.rect(win, tumehall, (290,490,120,60))
        kirjuta("Keskmine", 20, (350,520), tumehall, (255,255,255))
    if raskusaste == 3:
        pygame.draw.rect(win, tumehall, (420,490,100,60))
        kirjuta("Raske", 20, (470,520), tumehall, (255,255,255))
    
    pygame.display.update()
    
def mitu_punkti(x,y):
    kaugus = ((x-350)**2 + (y-350)**2)**(1/2)
    if kaugus > 200:
        return 0
    elif kaugus > 180:
        return 1
    elif kaugus > 160:
        return 2
    elif kaugus > 140:
        return 3
    elif kaugus > 120:
        return 4
    elif kaugus > 100:
        return 5
    elif kaugus > 80:
        return 6
    elif kaugus > 60:
        return 7
    elif kaugus > 40:
        return 8
    elif kaugus > 20:
        return 9
    else:
        return 10

run = True

while run:
    if raskusaste == 1:
        kaadri_viivitus = 10
    if raskusaste == 2:
        kaadri_viivitus = 5
    if raskusaste == 3:
        kaadri_viivitus = 1
    
    pygame.time.delay(kaadri_viivitus)
    (mouseX, mouseY) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if menüü == 1:
        menyy()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 200 <= mouseX <= 350 and 350 <= mouseY <= 450:
                print('mäng algab: '+ str(mitmesvise))
                menüü = 0
                mäng = 1
                if mitmesvise > 1:
                    uusmäng = 1
                    menüü = 0
                    mäng = 0
            if 350 <= mouseX <= 500 and 350 <= mouseY <= 450:
                run = False
            if 180 <= mouseX <= 280 and 500 <= mouseY <= 540:
                raskusaste = 1
            if 290 <= mouseX <= 410 and 500 <= mouseY <= 540:
                raskusaste = 2
            if 420 <= mouseX <= 520 and 500 <= mouseY <= 540:
                raskusaste = 3
    
      
    if uusmäng == 1:
        #menyy()
        menüü = 0
        mäng = 0
        win.fill(taustavärv)
        pygame.draw.rect(win, (191,239,255), (200,125,150,100))
        kirjuta("Uus mäng",24, (275,175), (191,239,255))
        pygame.draw.rect(win, (24,116,205), (350,125,150,100))
        kirjuta("Jätka vana",24, (425,175), (24,116,205))
        if 200 <= mouseX <= 350 and 125 <= mouseY <= 225:
            pygame.draw.rect(win, (191,239,255), (200,125,150,100))
            kirjuta("Uus mäng",24, (275,175), (191,239,255), (255,255,255))
        if 350 <= mouseX <= 500 and 125 <= mouseY <= 225:
            pygame.draw.rect(win, (24,116,205), (350,125,150,100))
            kirjuta("Jätka vana",24, (425,175), (24,116,205), (255,255,255))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 200 <= mouseX <= 350 and 125 <= mouseY <= 225:
                menüü = 0
                uusmäng = 0
                mitmesvise = 1
                mäng = 1
                punktekokku = 0
            elif 350 <= mouseX <= 500 and 125 <= mouseY <= 225:
                menüü = 0
                uusmäng = 0
                mäng = 1
                   
    if mäng == 1:
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            vise_x = x1
            x_seier = 0
            y_seier = 1
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and y_seier == 1:
            vise_y = y2
            y_seier = 0
            pygame.draw.circle(win, (200,0,0), (x1,y2 + 5), 5)
            kirjuta(str(mitu_punkti(x1,y2)) + " punkti!", 32, (350,100))
            pygame.display.update()
            pygame.time.delay(1500)
            punktekokku += mitu_punkti(x1,y2)
            mitmesvise += 1
            x_seier = 1
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 590 <= mouseX <= 690 and 10 <= mouseY <= 60:
                menüü = 1
                mäng = 0
        
        mängulaud()
        
        if not mitmesvise == 11:
            kirjuta("vise: " + str(mitmesvise) + "/10", 32, (100,50))
            kirjuta("punkte: " + str(punktekokku), 32, (100, 100))
        
        if mitmesvise == 11:
            win.fill(taustavärv)
            kirjuta("Tubli, said kokku " + str(punktekokku) + " punkti!", 32, (350,350))
            pygame.display.update()
            pygame.time.delay(2000)
            menüü = 1
            mäng = 0
            punktekokku = 0
            mitmesvise = 1
            
        
        if 590 <= mouseX <= 690 and 10 <= mouseY <= 60:
            pygame.draw.rect(win, (100,100,255), (590,10,100,50))
            kirjuta("Tagasi", 22, (640,35), (100,100,255), (255,255,255))
        else:
            pygame.draw.rect(win, (100,100,200), (590,10,100,50))
            kirjuta("Tagasi", 22, (640,35), (100,100,200), (0,0,0))
        
        #pygame.display.update()
        
        if x_seier == 1:
            pygame.draw.polygon(win, (0,0,0), [(x1,y1),(x1-10,y1+40),(x1+10,y1+40)])
            if x1 / 550 == 1:
                samm = -5
            if x1 / 150 == 1:
                samm = 5
            x1 += samm
        
        if y_seier == 1:
            pygame.draw.polygon(win, (0,0,0), [(x1,y1),(x1-10,y1+40),(x1+10,y1+40)])
            pygame.draw.polygon(win, (0,0,0), [(x2,y2),(x2+40,y2-10),(x2+40,y2+10)])
            if y2 / 150 == 1:
                samm = 5
            if y2 / 550 == 1:
                samm = -5
            y2 += samm
        
    pygame.display.update()
        

pygame.quit()