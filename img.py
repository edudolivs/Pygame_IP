import pygame

screen_res = (1280, 720)

orginal_background = pygame.image.load("c:/Users/João/Downloads/pygame/jogo/data/images/background.png")
original_floor = pygame.image.load("c:/Users/João/Downloads/pygame/jogo/data/images/floor.png")
original_pillars = pygame.image.load("c:/Users/João/Downloads/pygame/jogo/data/images/pillars.png")
original_character = pygame.image.load("c:/Users/João/Downloads/pygame/jogo/data/images/character.png")

resized_background = pygame.transform.scale(orginal_background, screen_res)
resized_floor = pygame.transform.scale(original_floor, screen_res)
resized_pillars = pygame.transform.scale(original_pillars, screen_res)
resized_character = pygame.transform.scale(original_character, (192, 192))
