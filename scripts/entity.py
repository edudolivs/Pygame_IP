import pygame
from scripts.util import get_frame, get_animation

def get_entity(assets, type: str, pos: list | tuple, size: tuple) -> dict:
    return {
        'assets': assets,
        'type': type,
        'pos': list(pos),
        'size': size,
        'vel': [0,0],
        'action': 'idle',
        'side': 1
    }

def get_player(assets, pos, size):
    player = get_entity(assets, 'player', pos, size)
    player.update(
        {
            'animation': get_animation(player, 10)
        }
    )
    return player

def get_rect(entity):
    return pygame.Rect(*entity['pos'], *entity['size'])

def update_entity(entity, movement=(0, 0)) -> None:

    entity['vel'][1] += 5

    frame_movement = (entity['vel'][0] + movement[0], entity['vel'][1] + movement[1])

    if frame_movement[0]:
        entity['action'] = 'walk'
    else:
        entity['action'] = 'idle'

    entity['pos'][0] += frame_movement[0]*10
    entity['pos'][1] += frame_movement[1]


def update_player(entity, movement=(0, 0)) -> None:
    update_entity(entity, movement)

    if entity['side'] != movement[0] and movement[0] != 0:
        entity['side'] = movement[0]

    if entity['pos'][0] > 1150:
        entity['pos'][0] = 1150
    if entity['pos'][0] < -80:
        entity['pos'][0] = -80
    if entity['pos'][1] > 475:
        entity['pos'][1] = 475
        entity['vel'][1] = 0
        entity['on_ground'] = True


def render_entity(entity: dict, surface: pygame.Surface) -> None:
    surface.blit(pygame.transform.flip(get_frame(entity), not bool(entity['side'] + 1), False), entity['pos'])


def jump(entity):
    entity['vel'][1] = -50


def attack(entity):
    pass

def dash(entity):
    pass