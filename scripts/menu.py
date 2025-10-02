import pygame

def create_button(x, y, width, height, text, font, base_text_color, hover_text_color):
    
    rectangle = pygame.Rect(x, y, width, height)

    button_data = {
        "rect": rectangle,
        "text": text,
        "font": font,
        "base_text_color": base_text_color,
        "hover_text_color": hover_text_color,
        "actual_text_color": base_text_color, 
    }
    return button_data

def draw_button(screen, button):
    text_surface = button["font"].render(button["text"], True, button["actual_text_color"])
    rect_text = text_surface.get_rect(center=button["rect"].center)
    screen.blit(text_surface, rect_text)

def update_hover_button(button):
    pos_mouse = pygame.mouse.get_pos()
    
    if button["rect"].collidepoint(pos_mouse):
        button["actual_text_color"] = button["hover_text_color"]
    else:
        button["actual_text_color"] = button["base_text_color"]
    

def check_click_button(evento, button):
    if evento.type == pygame.MOUSEBUTTONDOWN and button["rect"].collidepoint(evento.pos):
        return True
    return False

def main_menu(screen, clock): 
    font_title = pygame.font.Font("Jacquard24-Regular.ttf", 80)
    font_button = pygame.font.Font("Jacquard24-Regular.ttf", 55)

    pygame.display.set_caption("Mad and madder")

    base_text_color = (150, 150, 180)
    base_text_hover = (255, 255, 255)

    play_button = create_button(
    screen.get_width() / 2 - 50, 300, 100, 55, "Play",
    font_button, base_text_color, base_text_hover
    )
    options_button = create_button(
        screen.get_width() / 2 - 75, 400, 150, 60, "Options",
        font_button, base_text_color, base_text_hover
    )
    quit_button = create_button(
        screen.get_width() / 2 - 50, 500, 100, 55, "Quit",
        font_button, base_text_color, base_text_hover
    )

    buttons = [play_button, options_button, quit_button]

    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if check_click_button(event, play_button):
                return "play"
            if check_click_button(event, options_button):
                return "options"
            if check_click_button(event, quit_button):
                return "quit"
        
        for button in buttons:
            update_hover_button(button)
        
        screen.fill((10, 20, 30))

        tittle_text = font_title.render("Mad and madder", True, (255, 255, 255))
        screen.blit(tittle_text, (screen.get_width() / 2 - tittle_text.get_width() / 2, 150))

        for button in buttons:
            draw_button(screen, button)

        pygame.display.flip()
        clock.tick(30)
    
    return choice

def pause_menu(screen, clock):
    font_title = pygame.font.Font("Jacquard24-Regular.ttf", 80)
    font_button = pygame.font.Font("Jacquard24-Regular.ttf", 55)
    
    base_text_color = (150, 150, 180)
    base_text_hover = (255, 255, 255)

    overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 0))

    resume_button = create_button(
        screen.get_width() / 2 - 70, 300, 140, 50, "Resume", font_button, base_text_color, base_text_hover
    )
    main_menu_button = create_button(
        screen.get_width() / 2 - 110, 400, 220, 45, "Main Menu", font_button, base_text_color, base_text_hover
    ) 

    buttons = [resume_button, main_menu_button]

    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "play"
                
            if check_click_button(event, resume_button):
                return "play"
            if check_click_button(event, main_menu_button):
                return "main_menu"
        
        for button in buttons:
            update_hover_button(button)
            
        screen.blit(overlay, (0, 0))

        tittle_text = font_title.render("Paused", True, (255, 255, 255))
        screen.blit(tittle_text, (screen.get_width() / 2 - tittle_text.get_width() / 2, 150))

        for button in buttons:
            draw_button(screen, button)

        pygame.display.flip()
        clock.tick(30)
        
    return choice
