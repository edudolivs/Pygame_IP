import pygame
import os

IMG_DIR = 'data/imgs'

def load_img(path: str) -> pygame.Surface:
    img = pygame.image.load(path)
    size = img.get_size()
    return pygame.transform.scale(img, (size[0]*3, size[1]*3))

def list_frames(type: str, action: str) -> list[pygame.Surface]:
    imgs = []
    action_dir = os.path.join(IMG_DIR, type, action)
    file_names = sorted(os.listdir(action_dir))
    for file_name in file_names:
        file_path = os.path.join(action_dir, file_name)
        img = load_img(file_path)
        imgs.append(img)
    return imgs


def get_animation(entity):
        asset = entity['assets']["imgs"][entity['type']][entity['action']]
        return {
            'frames': asset[0],
            'tick': 0,
            'duration': asset[1],
            'len': len(asset[0]) * asset[1],
            'action': entity['action'],
            'effect': asset[2]
        }

def get_frame(entity) -> pygame.Surface:
    if entity['action'] != entity['animation']['action']:
        entity['animation'] = get_animation(entity)
    animation = entity['animation']

    tick = animation['tick'] // animation['duration']
    animation['tick'] = (animation['tick'] + 1) % animation['len']
    print(animation['action'], tick) if entity['type'] == 'boss' else None
    return animation['frames'][tick]
         
def sound(actor, event):
    pass