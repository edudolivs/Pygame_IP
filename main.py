import pygame
import random
from scripts import entity, util


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    ASSETS = {
        'environment':{
            'floor': pygame.image.load('data/imgs/environment/floor.png'),
            'background': pygame.image.load('data/imgs/environment/background.png')
        },
        'player':{
            'walk': (util.list_frames('player', 'walk'), 5, True),
            'idle': (util.list_frames('player', 'idle'), 5, True),
            'jump': (util.list_frames('player', 'jump'), 5, True),
            'dash': (util.list_frames('player', 'dash'), 10, False)
        }
    }

    player = entity.get_player(ASSETS, (100, 475), (64, 64))
    movement = [False, False]

    while running:

        print(player['vel'], player['on_ground'])

        screen.blit(ASSETS['environment']['background'], (0,0))
        screen.blit(ASSETS['environment']['floor'], (0, 0))


        entity.update_player(player, (movement[1] - movement[0], 0))
        entity.render_entity(player, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    movement[0] = True
                if event.key == pygame.K_d:
                    movement[1] = True
                if event.key == pygame.K_w and player['on_ground']:
                    entity.jump(player)
                if event.key == pygame.K_j:
                    entity.attack(player)
                if event.key == pygame.K_k and player['on_ground']:
                    entity.dash(player)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    movement[0] = False
                if event.key == pygame.K_d:
                    movement[1] = False

        pygame.display.flip()
    
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
