import pygame
import random
SCREEN_RECT = pygame.Rect(0, 0, 480,700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):
	def __init__(self,new_image,new_speed=1):
		super().__init__()
		self.image = pygame.image.load(new_image)
		self.rect = self.image.get_rect()
		self.speed = new_speed
	def update(self):
		self.rect.y += self.speed
class Background(GameSprite):
	def __init__(self,is_alt=False):
		super().__init__('./images/background.png')
		if is_alt:
			self.rect.y = -self.rect.height
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -self.rect.height
class Enemy(GameSprite):
	def __init__(self):
		super().__init__('./images/enemy1.png')
		self.speed = random.randint(1, 3)
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0, max_x)
		def update(self):
			super().update()
			if self.rect.y >= SCREEN_RECT.height:
				print("敌机飞出屏幕")
				self.kill()
class Hero(GameSprite):
	def __init__(self,a):
		super().__init__('./images/hero1.png',0)
		self.rect.centerx = SCREEN_RECT.centerx + a
		self.rect.bottom = SCREEN_RECT.bottom 
		self.bullets = pygame.sprite.Group()
		self.speed1 = 0
	def update(self):
		self.rect.x += self.speed
		self.rect.y += self.speed1
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right >SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		if self.rect.bottom > SCREEN_RECT.height:
			self.rect.bottom = SCREEN_RECT.height
		if self.rect.top < 0:
			self.rect.top = 0
	def fire(self):
		print("发射子弹....")
		for i in (1,2,3):
			bullet = Bullet()
			gws = Bullet()
			sst = Bullet()
			bullet.rect.bottom = self.rect.y -20
			bullet.rect.centerx = self.rect.centerx
			gws.rect.bottom = self.rect.y -20
			gws.rect.centerx = self.rect.centerx +15
			sst.rect.bottom = self.rect.y -20
			sst.rect.centerx = self.rect.centerx -15
			self.bullets.add(bullet,gws,sst)
		self.image_hit = pygame.image.load("images/enemy1_down1.png")  # 加载中型敌机中弹图片
		self.image_hit = pygame.image.load("images/enemy2_down2.png")  # 加载大型敌机中弹图片
class Bullet(GameSprite):
	def __init__(self):
		super().__init__('./images/bullet1.png',-10)
	def update(self):
		super().update()
		if self.rect.bottom < 0:
			self.kill()