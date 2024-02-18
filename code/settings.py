# game setup
WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
TILESIZE = 64

HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'E:\Da - real - Second - proper - game\Zelda\graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#00bbf9'
UI_BORDER_COLOR_2 = '#6a994e'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 150,'graphic':'E:\Da - real - Second - proper - game\Zelda\graphics\weapons\sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 300,'graphic':'E:\Da - real - Second - proper - game\Zelda\graphics\weapons\lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 200, 'graphic':'E:\Da - real - Second - proper - game\Zelda\graphics\weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 80, 'graphic':'E:\Da - real - Second - proper - game\Zelda\graphics\weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 100, 'graphic':'E:\Da - real - Second - proper - game\Zelda\graphics\weapons\sai/full.png'}
 }

# magic
magic_data = {
	'flame': {'strength': 500,'cost': 200,'graphic':'E:\Da - real - Second - proper - game\Zelda\graphics\particles/flame/fire.png'},
	'heal' : {'strength': 205,'cost': 100,'graphic':'E:\Da - real - Second - proper - game\Zelda\graphics\particles\heal/heal.png'}
 }


#enemies
monster_data = {
	'squid': {'health': 700,'exp':987,'damage':20,'attack_type': 'slash', 'attack_sound':'E:\Da - real - Second - proper - game\Zelda/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 100000,'exp':2796,'damage':990,'attack_type': 'claw',  'attack_sound':'E:\Da - real - Second - proper - game\Zelda/audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 500,'exp':702,'damage':80,'attack_type': 'thunder', 'attack_sound':'E:\Da - real - Second - proper - game\Zelda/audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 750,'exp':1840,'damage':60,'attack_type': 'leaf_attack', 'attack_sound':'E:\Da - real - Second - proper - game\Zelda/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},
 	#'cyclope': {'health': 500,'exp':250,'damage':60,'attack_type': 'claw',  'attack_sound':'E:\Da - real - Second - proper - game\Zelda/audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	#'frog': {'health': 700,'exp':200,'damage':6000,'attack_type': 'leaf_attack', 'attack_sound':'E:\Da - real - Second - proper - game\Zelda/audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},
 
 }
