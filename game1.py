import sys 
import pygame 

from settings import Settings

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	#screen = pygame.display.set_mode((1200, 800))
	pygame. display.set_caption("alien invasion")

	#更换背景颜色
	bg_color = (230, 230, 230)

	#开始游戏的主循环

	while True:

		#监测键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys. exit()

		#每次循环时都重新绘制屏幕
		screen.fill(ai_settings.bg_color)
		#screen.fill(bg_color)

		#让最近绘制的屏幕可见
		pygame.display.flip()


run_game()




