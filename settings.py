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
    'sword': {'cooldown': 300, 'damage': 15, 'speed': 12, 'graphic': './img/weapons/sword/full.png'},
    'lance': {'cooldown': 600, 'damage': 30, 'speed': 18, 'graphic': './img/weapons/lance/full.png'},
    'axe': {'cooldown': 400, 'damage': 20, 'speed': 14, 'graphic': './img/weapons/axe/full.png'},
    'rapier': {'cooldown': 150, 'damage': 8, 'speed': 8, 'graphic': './img/weapons/rapier/full.png'},
    'sai': {'cooldown': 200, 'damage': 10, 'speed': 9, 'graphic': './img/weapons/sai/full.png'}
}

magic_data = {
    'heal': {'strength': 20, 'cost': 25, 'graphic':'./img/particles/heal/heal.png'},
    'flame': {'strength': 5, 'cost': 18, 'graphic':'./img/particles/flame/fire.png'}
}

monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': './audio/attack/slash.wav',
            'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 90, 'attack_type': 'claw', 'attack_sound': './audio/attack/claw.wav',
            'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 120, 'damage': 40, 'attack_type': 'thunder', 'attack_sound': './audio/attack/fireball.wav',
            'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 150, 'damage': 50, 'attack_type': 'leaf_attack', 'attack_sound': './audio/attack/slash.wav',
            'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}