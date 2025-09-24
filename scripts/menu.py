import pygame

def main_menu(screen, clock): 
    font = pygame.font.Font(None, 74)
    pygame.display.set_caption("Mad and madder")

    play_button = pygame.Rect(screen.get_width() / 2 - 100, 300, 200 , 50)
    options_button = pygame.Rect(screen.get_width() / 2 - 100, 400, 200, 50)
    quit_button = pygame.Rect(screen.get_width() / 2 - 100, 500, 200, 50)

    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choice = "quit"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    choice = "play"
                if quit_button.collidepoint(event.pos):
                    choice = "quit"
        
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
    
    return choice

def pause_menu(screen, clock):
    font = pygame.font.Font(None, 74)

    overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 0))

    resume_button = pygame.Rect(screen.get_width()/ 2 - 150, 300, 300, 50)
    main_menu_button = pygame.Rect(screen.get_width() / 2 - 150, 400, 300, 50)

    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                choice = "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    choice = "play"
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    choice = "play"
                if main_menu_button.collidepoint(event.pos):
                    choice = "main_menu"
                
        screen.blit(overlay, (0, 0))

        pause_text = font.render('PAUSED', True, (255, 255, 255))
        screen.blit(pause_text, (screen.get_width() / 2 - pause_text.get_width() / 2, 150))

        pygame.draw.rect(screen, (0, 150, 0), resume_button)
        resume_text = font.render("Continue", True, (255, 255, 255))
        screen.blit(resume_text, (resume_button.x + (resume_button.width - resume_text.get_width()) / 2, resume_button.y))

        pygame.draw.rect(screen, (150, 0, 0), main_menu_button)
        main_menu_text = font.render("Main Menu", True, (255, 255, 255))
        screen.blit(main_menu_text, (main_menu_button.x + (main_menu_button.width - main_menu_text.get_width()) / 2, main_menu_button.y))

        pygame.display.flip()
        clock.tick(30)
        
    return choice
