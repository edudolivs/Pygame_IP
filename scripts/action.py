import pygame
import random
from scripts import entity


def idle(entity):
    entity['action'] = 'idle'
    entity['vel'] = [0, 0]

def player_jump(entity):
    entity['on_ground'] = False
    entity['action'] = 'jump'
    entity['vel'][1] = -50

def player_atk1(entity):
    entity['on_ground'] = False
    entity['action'] = 'atk1'

def player_atk2(player):
    player['action'] = 'atk2'
    player['blessed'] = False
    hitbox = [128, 160]
    pos = (
        player['pos'][0] + player['size'][0] // 2 - hitbox[0] // 2 + player['side'] * hitbox[0] // 2,
        player['pos'][1] + player['size'][1] - hitbox[1]
    )
    pygame.draw.rect(player['game']['screen'], 'red', (*pos, *hitbox))

def player_roll(entity):
    entity['on_ground'] = False
    entity['action'] = 'roll'

def player_pray(entity):
    entity['on_ground'] = False
    entity['action'] = 'pray'

def player_end_pray(entity):
    entity['blessed'] = True
    idle(entity)

def boss_atk_count(boss):
    boss['attk_count'] = boss['attk_count'] - 1
    if boss['attk_count'] == 0:
        boss['action'] = 'cool'
        boss['attk_count'] = random.randint(5,8)
    else:
        idle(boss)

def boss_up2(boss):
    boss['action'] = 'up2'
    hitbox0 = [320, 300]
    pos0 = (
        boss['pos'][0] + boss['size'][0] // 2 - hitbox0[0] // 2 + boss['side'] * hitbox0[0] // 2,
        boss['pos'][1] + boss['size'][1] - hitbox0[1]
    )
    hitbox1 = [128, 150]
    pos1 = (
        boss['pos'][0] + boss['size'][0] // 2 - hitbox1[0] // 2 - boss['side'] * hitbox1[0] // 2,
        boss['pos'][1] + boss['size'][1] - hitbox1[1] - 150
    )
    pygame.draw.rect(boss['game']['screen'], 'red', (*pos0, *hitbox0))
    pygame.draw.rect(boss['game']['screen'], 'red', (*pos1, *hitbox1))

def boss_spin2(boss):
    boss['action'] = 'spin2'
    hitbox = [400, 150]
    pos = (
        boss['pos'][0] + boss['size'][0] // 2 - hitbox[0] // 2,
        boss['pos'][1] + boss['size'][1] - hitbox[1]
    )
    pygame.draw.rect(boss['game']['screen'], 'red', (*pos, *hitbox))

def boss_down(boss):
    boss['spikes'].extend(
        entity.get_spikes(
            boss['game'],
            (
                boss['pos'][0] + boss['size'][0] // 2 - 96,
                boss['pos'][1] + boss['size'][1] - 96
            )
        )
    )
    boss_atk_count(boss)