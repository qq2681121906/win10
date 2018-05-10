import pygame


SCREEN_RECT = pygame.Rect(0,0,480,700)
#精灵类
class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):
		# 调用父类的初始化方法
		super().__init__()

		# 加载图像
		self.image = pygame.image.load(image_name)
		# 设置尺寸·
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed



	def update(self):
		self.rect.y += self.speed