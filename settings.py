WIDTH = 1280
HEIGHT = 720

FPS = 144
tilesize = 64

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = './img/joystix.ttf'
UI_FONT_SIZE = 18

#general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'



weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'speed': 6, 'graphic': './img/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'speed': 12, 'graphic': './img/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'speed': 9, 'graphic': './img/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'speed': 3, 'graphic': './img/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'speed': 4, 'graphic': './img/weapons/sai/full.png'}
}

magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic':'../img/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic':'../img/particles/heal/heal.png'}
}