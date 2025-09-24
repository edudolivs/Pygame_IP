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

def roll(entity):
    entity['on_ground'] = False
    entity['action'] = 'roll'

def pray(entity):
    entity['on_ground'] = False
    entity['action'] = 'pray'

def end_pray(entity):
    entity['blessed'] = True

def boss_attk(boss):
    boss['attk_count'] = boss['attk_count'] - 1
    if boss['attk_count'] == 0:
        boss['action'] = 'cool'
        boss['attk_count'] = random.randint(5,8)
    else:
        idle(boss)