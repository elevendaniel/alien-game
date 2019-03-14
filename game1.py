#import sys 
import pygame 


from settings import Settings
from ship import Ship #引入 ship中的ship功能
import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	#screen = pygame.display.set_mode((1200, 800))
	pygame. display.set_caption("alien invasion")

	#创建一艘飞船
	ship = Ship(screen)

	#更换背景颜色
	bg_color = (230, 230, 230)

	#开始游戏的主循环

	while True:
		#for event in pygame.event.get():
			#if event.type == pygame.QUIT:
				#sys. exit()
		gf.check_events()
		gf.update_screen(ai_settings, screen, ship)

	
		#每次循环时都重新绘制屏幕
		#screen.fill(ai_settings.bg_color)

		#ship.blitme()

		#screen.fill(bg_color)

		#让最近绘制的屏幕可见
		#pygame.display.flip()


run_game()




