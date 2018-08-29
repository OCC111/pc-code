import pygame

from pygame.locals import *
from MySprite import *


pygame.font.init()
my_font = pygame.font.Font("./comicbd.ttf", 16)

class PlaneGame(object):
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		self.__create_sprites()

		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#敌机定时事件
#pygame.time.set_timer(FIRE_BULLET,200)#子弹定时事件
		#self.enemy_group = pygame.sprite.Group() #敌机精灵组
		self.count = 0
		#得分
		self.score = 0
	def start_game(self):
		while True:
			#self.__event_handler()
			self.count += 1
			# 1. 设置刷新帧率
			self.clock.tick(60)
			# 2. 事件监听
			self.__event_handler()
			# 3. 碰撞检测
			self.__check_collide()
			# 4. 更新精灵组
			self.__update_sprites()
			# 5. 更新屏幕显示
			pygame.display.update()

	def __create_sprites(self):#创建精灵组和精灵组
		BG1 = BackGroundSprite()
		BG2 = BackGroundSprite(True)
		self.bg_group = pygame.sprite.Group(BG1,BG2)

		self.enemy1_down_group = pygame.sprite.Group()#摧毁效果精灵组
		self.enemy_group = pygame.sprite.Group()#创建敌机精灵组

		self.hero = HeroSprite()
		self.hero_group = pygame.sprite.Group(self.hero)


	def __event_handler(self):
		"""事件监听"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				# print("事件被触发了")
				enemy = EnemySprite()
				self.enemy_group.add(enemy)#通过add方法添加
			elif event.type == FIRE_BULLET:
				self.hero.fire()
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 5
			self.hero.speed1 = 0
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -5
			self.hero.speed1 = 0
		elif keys_pressed[pygame.K_UP]:
			self.hero.speed1 = -5
			self.hero.speed = 0
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speed1 = 5
			self.hero.speed = 0
		else:
			self.hero.speed1 = 0
			self.hero.speed = 0


		if keys_pressed[pygame.K_SPACE]:
			#print("子弹成功发射")
			self.hero.fire()


	def __check_collide(self):
		"""碰撞检测"""
		#英雄摧毁敌机
		enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.hero.bullet_group, True, True)

		enemy1_down_group.add(enemy_down)
		# 英雄被敌机摧毁
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)


		if len(enemies) > 0:
	        # 让英雄牺牲
			self.hero.kill()

	        # 结束游戏
			PlaneGame.__game_over()
	def __update_sprites(self):
		"""更新精灵组"""
		self.bg_group.update()
		self.bg_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.drawText(str(self.score),SCREEN_RECT.width - 30,50)

		for enemy1_down in  enemy1_down_group:
			self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
			if self.count % 15 == 0:
				enemy1_down.down_index += 1
				if enemy1_down.down_index == 3:
					self.score += 5
					enemy1_down_group.remove(enemy1_down)
					print(self.score)
		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)

	@staticmethod
	def __game_over():
	   """游戏结束"""

	   print("游戏结束")
	   pygame.quit()
	   exit()


	def drawText(self, text, posx, posy, textHeight=48, fontColor=(0, 0, 0), backgroudColor=(255, 255, 255)):
		fontObj = pygame.font.Font(None, textHeight)  # 通过字体文件获得字体对象
		textSurfaceObj = fontObj.render(text, True, fontColor, backgroudColor)  # 配置要显示的文字
		textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
		textRectObj.center = (posx, posy)  # 设置显示对象的坐标
		self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字

if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()

