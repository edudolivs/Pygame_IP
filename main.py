import pygame
from scripts import entity, util, action, menu

def game_loop(screen, clock, ASSETS, options):
    game = {
        'screen': screen,
        'clock': clock,
        'assets': ASSETS
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
        
        entity.render_entity(boss, screen)
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
                    action.jump(player)
                if event.key == pygame.K_j and player['on_ground']:
                    action.attk(player)
                if event.key == pygame.K_k and player['on_ground']:
                    action.roll(player)
                if event.key == pygame.K_l and player['on_ground']:
                    action.pray(player)
                
                if event.key == pygame.K_ESCAPE:
                    player['mov'] = [0,0]
                    choice = menu.pause_menu(screen, clock, options)
            
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
                'idle': (util.list_frames('player', 'idle'), 5, None),
                'jump': (util.list_frames('player', 'jump'), 5, None),
                'roll': (util.list_frames('player', 'roll'), 3, action.idle),
                'attk': (util.list_frames('player', 'attk'), 2, action.player_hit),
                'pray': (util.list_frames('player', 'pray'), 3, action.end_pray)
            },
            'boss':{
                'walk': (util.list_frames('boss', 'walk'), 10, action.idle),
                'idle': (util.list_frames('boss', 'idle'), 5, action.idle),
                'sweep': (util.list_frames('boss', 'attk2'), 5, action.boss_sweep),
                'slam': (util.list_frames('boss', 'attk'), 5, action.boss_slam),
                'cool': (util.list_frames('boss', 'cool'), 10, action.idle),
            },
            "window": { 
                "icon": pygame.image.load("data/imgs/window/icon.png")
            }
        },
        'audio':{
            'player': {
                'jump': (util.sound('player', 'jump'), False)
            }
        }
    }
    
    pygame.display.set_caption("Mad and madder")
    pygame.display.set_icon(ASSETS["imgs"]["window"]["icon"])

    choice = None
    while choice != 'quit':
        choice = menu.main_menu(screen, clock, options)

        if choice == 'play':
            choice = game_loop(screen, clock, ASSETS, options)
        
        if choice == 'options':
            choice = menu.options_menu(screen, clock, options, "main_menu")
    pygame.quit()


if __name__ == '__main__':
    main()
