import pygame
from scripts import action
from scripts.util import get_frame, get_animation
import random

def get_entity(game, type, pos):
    entity = {
        'game': game,
        'assets': game['assets'],
        'type': type,
        'pos': list(pos),
        'size': (0,0),
        'vel': [0,0],
        'action': 'idle',
        'side': 1,
        'on_ground': True,
        'base_speed': 1,
        'offset': (0, 0)
    }
    entity['animation'] = get_animation(entity)
    return entity

def get_player(game, pos):
    player = get_entity(game, 'player', pos)
    player.update(
        {
            'size': (96, 128),
            'mov': [False, False],
            'blessed': False,
            'base_speed': 10,
            'offset': (-144, -256)
        }
    )
    return player

def get_boss(game, pos):
    boss = get_entity(game, 'boss', pos)
    boss.update(
        {
            'type': 'boss',
            'size': (128, 256),
            'base_speed': 5,
            'offset': (-128, -128),
            'attk_count': 5
        }
    )
    return boss

def get_rect(entity):
    return pygame.Rect(*entity['pos'], *entity['size'])

def update_entity(entity, movement = 0):

    frame_movement = (entity['vel'][0] + movement, entity['vel'][1])

    animation = entity['animation']
    if animation['effect'] and animation['tick'] == animation['len'] - 1:
        animation['effect'](entity)

    entity['pos'][0] += frame_movement[0] * entity['base_speed']
    entity['pos'][1] += frame_movement[1]


def update_player(player):

    movement = player['mov'][1] - player['mov'][0]

    if player['action'] == 'roll':
        player['vel'][0] = player['side'] * 2
        movement = 0
    elif player['action'] == 'attk' or player['action'] == 'pray':
        movement = 0
    else:
        player['vel'][0] = 0
        player['vel'][1] += 5

    update_entity(player, movement)

    if player['pos'][0] > 1208:
        player['pos'][0] = 1208
    if player['pos'][0] < -24:
        player['pos'][0] = -24
    if player['pos'][1] > 528:
        player['pos'][1] = 528
        player['vel'][1] = 0
        player['on_ground'] = True
    
    if player['on_ground']:
        if movement:
            player['action'] = 'walk'
        else:
            player['action'] = 'idle'
    
    if player['side'] == -movement:
        player['side'] *= -1

def update_boss(boss):
    player = boss['game']['player']

    dist = player['pos'][0] - boss['pos'][0]

    if boss['action'] == 'idle' and dist:
        boss['side'] = dist/abs(dist)
    
    if boss['action'] != 'cool':
        if abs(dist) > 250:
            if boss['action'] == 'idle':
                boss['vel'][0] = 0
                boss['action'] = random.choice(['walk', 'sweep'])
            if boss['action'] == 'walk':
                boss['vel'][0] = dist/abs(dist)
        elif boss['action'] in {'idle', 'walk'}:
            boss['vel'] = [0, 0]
            boss['action'] = random.choice(['sweep','slam'])

    update_entity(boss)

def render_entity(entity, surface):
    pygame.draw.rect(surface, 'green', (*entity['pos'], *entity['size']))
    surface.blit(
        pygame.transform.flip(get_frame(entity),bool(entity['side'] - 1), False),
        (
            entity['pos'][0] + entity['offset'][0],
            entity['pos'][1] + entity['offset'][1]
        )
    )


def render_player(player, surface: pygame.Surface):
    render_entity(player, surface)
    if player['blessed'] == True:
        print('blessed')
        surface.blit(
            player['game']['assets']['imgs']['player']['aura'],
            (
            player['pos'][0] + player['offset'][0],
            player['pos'][1] + player['offset'][1]
            )
        )

