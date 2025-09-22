import pygame

def main_menu(screen, clock): 
    font = pygame.font.Font(None, 74)
    pygame.display.set_caption("Mad and madder")

    play_button = pygame.Rect(screen.get_width() / 2 - 100, 300, 200 , 50)
    options_button = pygame.Rect(screen.get_width() / 2 - 100, 400, 200, 50)
    quit_button = pygame.Rect(screen.get_width() / 2 - 100, 500, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return "play"
                if quit_button.collidepoint(event.pos):
                    return "quit"
        
        screen.fill((10, 20, 30))

        tittle_text = font.render("Mad and madder", True, (255, 255, 255))
        screen.blit(tittle_text, (screen.get_width() / 2 - tittle_text.get_width() / 2, 150))

        pygame.draw.rect(screen, (0, 150, 0), play_button)
        play_text = font.render("Play", True, (255, 255, 255))
        screen.blit(play_text, (play_button.x + (play_button.width - play_text.get_width()) / 2, play_button.y))

        pygame.draw.rect(screen, (0, 20, 150), options_button)
        options_button_text = font.render("Options", True, (255, 255, 255))
        screen.blit(options_button_text, (options_button.x + (options_button.width - options_button_text.get_width()) / 2, options_button.y))

        pygame.draw.rect(screen, (150, 0, 0), quit_button)
        quit_text = font.render('Sair', True, (255, 255, 255))
        screen.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) / 2, quit_button.y))

        pygame.display.flip()
        clock.tick(30)



def pause():
    pass