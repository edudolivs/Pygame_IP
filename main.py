import pygame
from scripts import entity, util, action, menu

def game_loop(screen, clock, ASSETS, options):
    game = {
        'screen': screen,
        'clock': clock,
        'assets': ASSETS,
        "options": options
    }
    game.update(
        {
            'player': entity.get_player(game, (100, 528)),
            'boss': entity.get_boss(game, (600, 528+128-256))
        }
    )
    player = game['player']
    boss = game['boss']

    choice = 'play'
    while choice == 'play':

        screen.blit(ASSETS["imgs"]['environment']['background'], (0,0))
        screen.blit(ASSETS["imgs"]['environment']['floor'], (0, 0))

        entity.update_boss(boss)
        entity.update_player(player)
        
        entity.render_boss(boss, screen)
        entity.render_player(player, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choice = 'quit'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player['mov'][0] = True
                if event.key == pygame.K_d:
                    player['mov'][1] = True
                if event.key == pygame.K_w and player['on_ground']:
                    action.player_jump(player)
                if event.key == pygame.K_j and player['on_ground']:
                    action.player_atk1(player)
                if event.key == pygame.K_k and player['on_ground']:
                    action.player_roll(player)
                if event.key == pygame.K_l and player['on_ground']:
                    action.player_pray(player)
                
                if event.key == pygame.K_ESCAPE:
                    player['mov'] = [0,0]
                    choice = menu.pause_menu(screen, clock, options, ASSETS)
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player['mov'][0] = False
                if event.key == pygame.K_d:
                    player['mov'][1] = False
                if event.key == pygame.K_l and player['action'] == 'pray':
                    player['action'] = 'idle'
                
        pygame.display.flip()
        clock.tick(30)
        
    return choice

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    
    options = {"volume": 0.5}
    ASSETS = {
        'imgs': {
            'environment':{
                'floor': pygame.image.load('data/imgs/environment/floor.png'),
                'background': pygame.image.load('data/imgs/environment/background.png')
            },
            'player':{
                'aura': util.load_img('data/imgs/player/aura.png'),
                'walk': (util.list_frames('player', 'walk'), 5, None),
                'idle': (util.list_frames('player', 'idle'), 10, None),
                'jump': (util.list_frames('player', 'jump'), 5, None),
                'roll': (util.list_frames('player', 'roll'), 3, action.idle),
                'atk1': (util.list_frames('player', 'atk1'), 2, action.player_atk2),
                'atk2': (util.list_frames('player', 'atk2'), 2, action.idle),
                'pray': (util.list_frames('player', 'pray'), 5, action.player_end_pray)
            },
            'boss':{
                'walk': (util.list_frames('boss', 'walk'), 5, action.idle),
                'down': (util.list_frames('boss', 'down'), 5, action.boss_down),
                'idle': (util.list_frames('boss', 'idle'), 5, action.idle),
                'up1':  (util.list_frames('boss', 'up1'), 10, action.boss_up2),
                'up2':  (util.list_frames('boss', 'up2'), 10, action.boss_atk_count),
                'spin1': (util.list_frames('boss', 'spin1'), 10, action.boss_spin2),
                'spin2': (util.list_frames('boss', 'spin2'), 10, action.boss_atk_count),
                'cool': (util.list_frames('boss', 'cool'), 10, action.idle),
                'spikes': (util.list_frames('boss', 'spikes'), 2, None)
            },
            "window": { 
                "icon": pygame.image.load("data/imgs/window/icon.png")
            }
        },
        'sounds':{
            'player': {
                'jump': pygame.mixer.Sound("data/sounds/player/jump.ogg"),
                "attk": pygame.mixer.Sound("data/sounds/player/attk.ogg"),
                "roll": pygame.mixer.Sound("data/sounds/player/roll.ogg"),
            },
            "boss": { 
                "sweep": pygame.mixer.Sound("data/sounds/boss/sweep.ogg"),
                "slam": pygame.mixer.Sound("data/sounds/boss/slam.ogg"),
            },
            "ui": {
                "click": pygame.mixer.Sound("data/sounds/ui/click.ogg"),
            },
            "music": { 
                "main_theme": "data/sounds/music/music.ogg"
            }
        }
    }
    
    pygame.display.set_caption("Mad and madder")
    pygame.display.set_icon(ASSETS["imgs"]["window"]["icon"])

    choice = None
    while choice != 'quit':
        choice = menu.main_menu(screen, clock, options, ASSETS)

        if choice == 'play':
            choice = game_loop(screen, clock, ASSETS, options)
        
        if choice == 'options':
            choice = menu.options_menu(screen, clock, options, "main_menu", ASSETS)
    pygame.quit()


if __name__ == '__main__':
    main()
