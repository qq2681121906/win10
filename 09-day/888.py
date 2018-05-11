import pygame
from gws import *
pygame.mixer.init()
class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
    def start_game(self):
        while True:
            self.clock.tick(60)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()
    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.hero = Hero(60)
        self.hero1 = Hero(-60)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero,self.hero1)
    def __event_handler(self):
        for event in pygame.event.get():
            key_pressed = pygame.key.get_pressed()
            key_pressed1 = pygame.key.get_pressed()
            if key_pressed[pygame.K_KP1]:
            	self.hero.fire()
            if key_pressed[pygame.K_RIGHT]:
                print("向右边移动")
                self.hero.speed = 8
            elif key_pressed[pygame.K_LEFT]:
                self.hero.speed = -8
                print("向左边移动")
            elif key_pressed[pygame.K_UP]:
                print("向上边移动")
                self.hero.speed1 = -8
            elif key_pressed[pygame.K_DOWN]:
                print("想下边移动")
                self.hero.speed1 = 8
            else:
                self.hero.speed = 0
                self.hero.speed1 = 0
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("新的敌机产生")
                self.enemy_group.add(Enemy())
            if key_pressed1[pygame.K_SPACE]:
            	self.hero1.fire()
            if key_pressed1[pygame.K_d]:
                print("向右边移动")
                self.hero1.speed = 8
            elif key_pressed1[pygame.K_a]:
                self.hero1.speed = -8
                print("向左边移动")
            elif key_pressed1[pygame.K_w]:
                print("向上边移动")
                self.hero1.speed1 = -8
            elif key_pressed1[pygame.K_s]:
                print("想下边移动")
                self.hero1.speed1 = 8
            else:
                self.hero1.speed = 0
                self.hero1.speed1 = 0
    def __update_sprites(self):
        for xxx in [self.back_group, self.enemy_group, self.hero_group, self.hero.bullets, self.hero1.bullets]:
            xxx.update()
            xxx.draw(self.screen)
    def __check_collide(self):
        pygame.sprite.groupcollide(
            self.enemy_group, self.hero.bullets,True, True)
        enemies = pygame.sprite.spritecollide(
            self.hero, self.enemy_group, True)
        pygame.sprite.groupcollide(
            self.enemy_group, self.hero1.bullets, True, True)
        enemies1 = pygame.sprite.spritecollide(
            self.hero1, self.enemy_group, True)
        if len(enemies) == 1:
            self.hero.kill()
            self.hero.rect.x = -SCREEN_RECT.width
        if len(enemies1) == 1:
            self.hero1.kill()
            self.hero1.rect.x = -SCREEN_RECT.width
        if self.hero.rect.x == -SCREEN_RECT.width and self.hero1.rect.x == -SCREEN_RECT.width:
            self.__game_over()
    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()
if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()