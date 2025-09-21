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


def get_animation(entity, frame_duration: int) -> dict:
        imgs = entity['assets'][entity['type']][entity['action']]
        return {
            'imgs': imgs,
            'frame': 0,
            'duration': frame_duration,
            'len': len(imgs) * frame_duration,
            'action': entity['action']
        }

def get_frame(entity) -> pygame.Surface:
    if entity['action'] != entity['animation']['action']:
        entity['animation'] = get_animation(entity, 10)
    animation = entity['animation']
    animation['frame'] = (animation['frame'] + 1) % animation['len']
    frame = animation['frame'] // animation['duration']
    return animation['imgs'][frame]
