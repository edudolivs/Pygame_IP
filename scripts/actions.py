import pygame
import random
from scripts import utils, entities

def idle(entity):
    entity['action'] = 'idle'
    entity['vel'] = [0, 0]

def player_jump(player):
    player['on_ground'] = False
    player['action'] = 'jump'
    player['vel'][1] = -50
    utils.sound(player, "jump")

def player_atk1(player):
    player['on_ground'] = False
    player['action'] = 'atk1'

def player_atk2(player):
    player['action'] = 'atk2'
    hitbox = [128, 160]
    pos = (
        player['pos'][0] + player['size'][0] // 2 - hitbox[0] // 2 + player['side'] * hitbox[0] // 2,
        player['pos'][1] + player['size'][1] - hitbox[1]
    )

    boss = player['game']['boss']
    if pygame.Rect(*pos, *hitbox).colliderect(entities.rect(boss)):
        
        if player['blessed']:
            utils.sound(player, "blessed_hit")
            boss['hp'] -= 15
        else:
            utils.sound(player, "hit")
            player['pure'] = False
            boss['hp'] -= 3

        if boss['hp'] <= 0:
            if player['pure']:
                player['game']['choice'] = "blessed_victory" 
            elif player['corrupt']:
                player['game']['choice'] = "corrupt_victory" 
            else:
                player['game']['choice'] = "common_victory"

    player['blessed'] = False
    utils.sound(player, "atk2")

def player_roll(player):
    player['on_ground'] = False
    player['action'] = 'roll'
    utils.sound(player, "roll")

def player_pray(player):
    player['on_ground'] = False
    player['action'] = 'pray'

def player_end_pray(player):
    player['blessed'] = True
    player['corrupt'] = False
    idle(player)

def player_hurt(player):
    utils.sound(player, "hit")
    player['on_ground'] = False
    player['action'] = 'stunned'
    player['vel'] = [player['side'] * -1, -20]
    player['iframes'] = 30
    player['show_hearts'] = 31
    player['hp'] -= 1
    if player['hp'] == 0:
        utils.sound(player, 'morri')
        player['game']['choice'] = 'death_menu'

def boss_atk_count(boss):
    boss['attk_count'] = boss['attk_count'] - 1
    if boss['attk_count'] == 0:
        boss['action'] = 'cool'
        boss['attk_count'] = random.randint(5,8)
    else:
        idle(boss)

def boss_up2(boss):
    boss['action'] = 'up2'
    boss['slash'] = entities.get_slash(boss['game'], boss['pos'])
    hitbox0 = [275, 300]
    pos0 = (
        boss['pos'][0] + boss['size'][0] // 2 - hitbox0[0] // 2 + boss['side'] * hitbox0[0] // 2,
        boss['pos'][1] + boss['size'][1] - hitbox0[1]
    )
    hitbox1 = [128, 150]
    pos1 = (
        boss['pos'][0] + boss['size'][0] // 2 - hitbox1[0] // 2 - boss['side'] * hitbox1[0] // 2,
        boss['pos'][1] + boss['size'][1] - hitbox1[1] - 150
    )
    #pygame.draw.rect(boss['game']['screen'], 'red', (*pos0, *hitbox0))
    #pygame.draw.rect(boss['game']['screen'], 'red', (*pos1, *hitbox1))

    player = boss['game']['player']
    if (pygame.Rect(*pos0, *hitbox0).colliderect(entities.rect(player))\
    or pygame.Rect(*pos1, *hitbox1).colliderect(entities.rect(player)))\
    and not player['iframes']:
        player_hurt(player)
    
    utils.sound(boss, 'up2')

def boss_end_slash(boss):
    del boss['slash']
    boss_atk_count(boss)

def boss_spin2(boss):
    boss['action'] = 'spin2'
    hitbox = [400, 150]
    pos = (
        boss['pos'][0] + boss['size'][0] // 2 - hitbox[0] // 2,
        boss['pos'][1] + boss['size'][1] - hitbox[1]
    )
    #pygame.draw.rect(boss['game']['screen'], 'red', (*pos, *hitbox))

    player = boss['game']['player']
    if pygame.Rect(*pos, *hitbox).colliderect(entities.rect(player))\
    and not player['iframes']:
        player_hurt(player)
    
    utils.sound(boss, 'spin2')

def boss_down2(boss):
    boss['action'] = 'down2'

    utils.sound(boss, 'down2')

    boss['spikes'].extend(
        entities.get_spikes(
            boss['game'],
            (
                boss['pos'][0] + boss['size'][0] // 2 - 96 + boss['side'] * 32,
                boss['pos'][1] + boss['size'][1] - 16
            )
        )
    )
