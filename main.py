import pygame
import random
from scripts import entity, util, menu

def game_loop(screen, clock, ASSETS):
    player = entity.get_player(ASSETS, (100, 475), (64, 64))
    movement = [False, False]
    running = True

    while running:

        screen.blit(ASSETS["imgs"]['environment']['background'], (0,0))
        screen.blit(ASSETS["imgs"]['environment']['floor'], (0, 0))
        
        entity.update_player(player, (movement[1] - movement[0], 0))
        entity.render_entity(player, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    movement[0] = True
                if event.key == pygame.K_d:
                    movement[1] = True
                if event.key == pygame.K_w and player['on_ground']:
                    entity.jump(player)
                if event.key == pygame.K_j and player['on_ground']:
                    entity.attk(player)
                if event.key == pygame.K_k and player['on_ground']:
                    entity.roll(player)
                if event.key == pygame.K_l and player['on_ground']:
                    entity.pray(player)
                if event.key == pygame.K_ESCAPE:
                    menu.pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    movement[0] = False
                if event.key == pygame.K_d:
                    movement[1] = False
                if event.key == pygame.K_l and player['action'] == 'pray':
                    player['action'] = 'idle'
                


        pygame.display.flip()
    
        clock.tick(30)

    return


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    
    

    ASSETS = {
        'imgs': {
            'environment':{
                'floor': pygame.image.load('data/imgs/environment/floor.png'),
                'background': pygame.image.load('data/imgs/environment/background.png')
            },
            'player':{
                'walk': (util.list_frames('player', 'walk'), 5, True),
                'idle': (util.list_frames('player', 'idle'), 5, True),
                'jump': (util.list_frames('player', 'jump'), 5, True),
                'roll': (util.list_frames('player', 'roll'), 3, False),
                'attk': (util.list_frames('player', 'attk'), 10, False),
                'pray': (util.list_frames('player', 'pray'), 30, False)
            }
        },
        'audio':{
            'player': {
                'jump': (util.sound('player', 'jump'), False)
            }
        }
    }

    choice = None
    while choice != 'quit':
        choice = menu.main_menu(screen, clock)

        if choice == 'play':
            game_loop(screen, clock, ASSETS)
        
        if choice == 'options':
            pass


    

    pygame.quit()


if __name__ == '__main__':
    main()
