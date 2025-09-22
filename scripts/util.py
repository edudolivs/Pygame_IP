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


def get_animation(entity: dict, frame_duration: int, loop: bool = True) -> dict:
        asset = entity['assets']["imgs"][entity['type']][entity['action']]
        return {
            'imgs': asset[0],
            'frame': 0,
            'duration': asset[1],
            'len': len(asset[0]) * asset[1],
            'action': entity['action'],
            'loop': asset[2]
        }

def get_frame(entity) -> pygame.Surface:
    if entity['action'] != entity['animation']['action']:
        entity['animation'] = get_animation(entity, 5)
    animation = entity['animation']

    if animation['loop']:
        frame = animation['frame'] % animation['len']
        frame = frame // animation['duration']
        animation['frame'] = (animation['frame'] + 1) % animation['len']
        return animation['imgs'][frame]
    else:
         if animation['frame'] == animation['len'] - 2:
              entity['action'] = 'idle'
         animation['frame'] += 1
         frame = animation['frame'] // animation['duration']
         return animation['imgs'][frame]
         
def sound(actor, event):
     pass