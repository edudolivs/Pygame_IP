import pygame
from scripts import entities, utils, actions, menus

def game_loop(screen, clock, ASSETS, options):
    game = {
        'screen': screen,
        'clock': clock,
        'assets': ASSETS,
        "options": options
    }
    game.update(
        {
            'player': entities.get_player(game, (100, 528)),
            'boss': entities.get_boss(game, (600, 528+128-256))
        }
    )
    player = game['player']
    boss = game['boss']

    pygame.mixer.music.load(ASSETS["sounds"]["music"]["main_theme"])
    pygame.mixer.music.set_volume(options["volume"])
    pygame.mixer.music.play(-1)

    game['choice'] = 'play'
    while game['choice'] == 'play':

        screen.blit(ASSETS["imgs"]['environment']['background'], (0,0))
        screen.blit(ASSETS["imgs"]['environment']['floor'], (0, 0))

        entities.update_boss(boss)
        entities.update_player(player)
        
        entities.render_boss(boss, screen)
        entities.render_player(player, screen)

        pygame.draw.rect(screen, 'red', (20, 20, 1240 * boss['hp'] // 50, 10))
        font_name = pygame.font.Font("Jacquard24-Regular.ttf", 48)
        name_text = font_name.render("The Mad King", True, (255, 255, 255))
        screen.blit(name_text, (screen.get_width() / 2 - name_text.get_width() / 2, 0))

        if player['show_hearts'] % 10 < 5:
            for i in range(3):
                if i < player['hp']:
                    heart = player['game']['assets']['imgs']['player']['heart1']
                else:
                    heart: pygame.Surface = player['game']['assets']['imgs']['player']['heart0']
                size = heart.get_size()
                screen.blit(
                    heart,
                    (
                        i * size[0],
                        720 - size[1]
                    )
                )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game['choice'] = 'quit'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player['mov'][0] = True
                if event.key == pygame.K_d:
                    player['mov'][1] = True
                if event.key == pygame.K_w and player['on_ground']:
                    actions.player_jump(player)
                if event.key == pygame.K_j and player['on_ground']:
                    actions.player_atk1(player)
                if event.key == pygame.K_k and player['on_ground']:
                    actions.player_roll(player)
                if event.key == pygame.K_l and player['on_ground']:
                    actions.player_pray(player)
                
                if event.key == pygame.K_ESCAPE:
                    player['mov'] = [0,0]
                    game['choice'] = menus.pause_menu(screen, clock, options, ASSETS)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player['mov'][0] = False
                if event.key == pygame.K_d:
                    player['mov'][1] = False
                if event.key == pygame.K_l and player['action'] == 'pray':
                    player['action'] = 'idle'
                
        pygame.display.flip()
        clock.tick(30)
        
    return game['choice']

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    
    options = {"volume": 0.3}
    ASSETS = {
        'imgs': {
            'environment':{
                'floor': pygame.image.load('data/imgs/environment/floor.png'),
                'background': pygame.image.load('data/imgs/environment/background.png')
            },
            "endings": {
                "blessed_victory": {
                    'img': pygame.image.load("data/imgs/endings/blessed_ending.png"),
                    'text': "Você foi curado da loucura, ganha alta e sai feliz com sua família.",
                    'text2': "Após anos internado acreditando que era um cavaleiro",
                    'theme': "data/sounds/endings/sakamoto.mp3"
                },
                    'common_victory': {
                    'img': pygame.image.load("data/imgs/endings/common_ending.png"),
                    'text': "Mas algo não parece estar certo...",
                    'text2': "Você derrotou o rei e ganha uma vida próspera no reino.",
                    'theme': "data/sounds/endings/Daft.mp3"
                },
                    "corrupt_victory": {
                    'img': pygame.image.load("data/imgs/endings/corrupt_ending.png"),
                    'text': "Você acorda ainda achando que é um cavaleiro.",
                    'text2': "Mais um dia no hospício...",
                    'theme': "data/sounds/endings/corrupt_ending.mp3"
                } 
            },
            'player':{
                'aura': utils.load_img('data/imgs/player/aura.png'),
                'heart0': pygame.transform.scale2x(pygame.image.load('data/imgs/player/heart0.png')),
                'heart1': pygame.transform.scale2x(pygame.image.load('data/imgs/player/heart1.png')),
                'walk': (utils.list_frames('player', 'walk'), 5, None),
                'idle': (utils.list_frames('player', 'idle'), 10, None),
                'jump': (utils.list_frames('player', 'jump'), 5, None),
                'roll': (utils.list_frames('player', 'roll'), 3, actions.idle),
                'atk1': (utils.list_frames('player', 'atk1'), 2, actions.player_atk2),
                'atk2': (utils.list_frames('player', 'atk2'), 2, actions.idle),
                'pray': (utils.list_frames('player', 'pray'), 5, actions.player_end_pray),
                'stunned': (utils.list_frames('player', 'stunned'), 5, None)
            },
            'boss':{
                'walk': (utils.list_frames('boss', 'walk'), 5, actions.idle),
                'down1': (utils.list_frames('boss', 'down1'), 10, actions.boss_down2),
                'down2': (utils.list_frames('boss', 'down2'), 5, actions.boss_atk_count),
                'idle': (utils.list_frames('boss', 'idle'), 5, actions.idle),
                'up1':  (utils.list_frames('boss', 'up1'), 10, actions.boss_up2),
                'up2':  (utils.list_frames('boss', 'up2'), 10, actions.boss_end_slash),
                'slash': (utils.list_frames('boss', 'slash'), 10, None),
                'spin1': (utils.list_frames('boss', 'spin1'), 10, actions.boss_spin2),
                'spin2': (utils.list_frames('boss', 'spin2'), 10, actions.boss_atk_count),
                'cool': (utils.list_frames('boss', 'cool'), 10, actions.idle),
                'spikes': (utils.list_frames('boss', 'spikes'), 4, None)
            },
            "window": { 
                "icon": pygame.image.load("data/imgs/window/icon.png")
            }
        },
        'sounds':{
            'player': {
                'jump': pygame.mixer.Sound("data/sounds/player/jump2.mp3"),
                "atk2": pygame.mixer.Sound("data/sounds/player/atk2-2.mp3"),
                "roll": pygame.mixer.Sound("data/sounds/player/roll.mp3"),
                'morri': pygame.mixer.Sound('data/sounds/player/morri.mp3'),
                "hit": pygame.mixer.Sound("data/sounds/player/hit2.mp3"),
                "blessed_hit": pygame.mixer.Sound("data/sounds/player/blessed_hit.mp3")
            },
            "boss": { 
                "up2": pygame.mixer.Sound("data/sounds/boss/hit.mp3"),
                "spin2": pygame.mixer.Sound("data/sounds/boss/boss_slash.mp3"),
                "down2": pygame.mixer.Sound("data/sounds/boss/down.mp3"),
            },
            "ui": {
                "click": pygame.mixer.Sound("data/sounds/ui/click.ogg"),
            },
            "music": { 
                "main_theme": "data/sounds/music/battle.mp3",
                "main_menu": "data/sounds/music/main_menu_theme.mp3"
            }
        }
    }
    icon = ASSETS["imgs"]["window"]["icon"]
    pygame.display.set_icon(icon)

    choice = 'main_menu'
    while choice != 'quit':

        if choice == 'main_menu':
            choice = menus.main_menu(screen, clock, options, ASSETS)

        if choice == 'play':
            choice = game_loop(screen, clock, ASSETS, options)
        
        if choice == 'options':
            choice = menus.options_menu(screen, clock, options, "main_menu", ASSETS)
    
        if choice == 'death_menu':
            choice = menus.death_menu(screen, clock, options, ASSETS)
        
        if "victory" in choice:
            victory_type = choice
            choice = menus.victory_menu(screen, clock, options, ASSETS, victory_type)

    pygame.quit()


if __name__ == '__main__':
    main()
