import pygame
import random


def idle(entity):
    entity['action'] = 'idle'
    entity['vel'] = [0, 0]

def jump(entity):
    entity['on_ground'] = False
    entity['action'] = 'jump'
    entity['vel'][1] = -50

def attk(entity):
    entity['on_ground'] = False
    entity['blessed'] = False
    entity['action'] = 'attk'

def player_hit(player):
    hitbox = [100, 40]
    pos = (
        player['pos'][0] + player['size'][0] // 2 - hitbox[0] // 2 + player['side'] * hitbox[0],
        player['pos'][1] + player['size'][1] // 2
    )
    pygame.draw.rect(player['game']['screen'], 'green', (*pos, *hitbox))
    player['action'] = 'idle'

def roll(entity):
    entity['on_ground'] = False
    entity['action'] = 'roll'

def pray(entity):
    entity['on_ground'] = False
    entity['action'] = 'pray'

def end_pray(entity):
    entity['blessed'] = True
    idle(entity)

def boss_sweep(boss):
    hitbox = [500, 300]
    pos = (
        boss['pos'][0] + boss['size'][0] // 2 - hitbox[0] // 2 + boss['side'] * 150,
        boss['pos'][1] + boss['size'][1] // 2 - hitbox[1] // 2
    )
    pygame.draw.rect(boss['game']['screen'], 'red', (*pos, *hitbox))
    
    boss['attk_count'] = boss['attk_count'] - 1
    if boss['attk_count'] == 0:
        boss['action'] = 'cool'
        boss['attk_count'] = random.randint(5,8)
    else:
        idle(boss)

def boss_slam(boss):
    hitbox = [500, 300]
    pos = (
        boss['pos'][0] + boss['size'][0] // 2 - hitbox[0] // 2,
        boss['pos'][1] + boss['size'][1] // 2 - hitbox[1] // 2
    )
    pygame.draw.rect(boss['game']['screen'], 'red', (*pos, *hitbox))
    
    boss['attk_count'] = boss['attk_count'] - 1
    if boss['attk_count'] == 0:
        boss['action'] = 'cool'
        boss['attk_count'] = random.randint(5,8)
    else:
        idle(boss)