import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)
#刷新帧率
FRAME_PER_SEC = 60
#敌机事件的常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.y += self.speed	




class Background(GameSprite):

	def __init__(self,is_alt=False):
		image_name = "./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y = -self.rect.height

	
	def update(self):
		super().update()
		if self.rect.y > SCREEN_RECT.height:
			self.rect.y = -self.rect.height




#1、随机x值 一定要有最大值 随机数
#2、初始化速度  随机1-?
#3、初始化y的位置

class Enemy(GameSprite):
	def __init__(self):
		image_name = "./images/enemy-1.gif"
		super().__init__(image_name)
		self.speed  = random.randint(1,3)

		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)#随机位置

		self.rect.bottom = 0

	def update(self):
		super().update()