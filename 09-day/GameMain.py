import pygame
from PlanSprite import *
class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size) 
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        #定时器 毫秒
        #第一个参数是事件的名字
        #第二个参数是多长时间执行一次时间
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)

        #敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)

        

    def start_game(self):
        print("游戏开始...")
        while  True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update() 
        

    def __event_handler(self):
        # pass
        
        for event in pygame.event.get():
        # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:#定时器事件
                enemy = Enemy()
                self.enemy_group.add(enemy)



    def __check_collide(self):
        pass
    
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)


        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        

        
        

    @staticmethod       
    def game_over():
        pygame.quit
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()