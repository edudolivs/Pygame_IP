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
    

def check_click_button(event, button, ASSETS, options):
    if event.type == pygame.MOUSEBUTTONDOWN and button["rect"].collidepoint(event.pos):
        sfx = ASSETS["sounds"]["ui"]["click"]
        sfx.set_volume(options["volume"])
        sfx.play()
        return True
    return False

def main_menu(screen, clock, options, ASSETS): 
    font_title = pygame.font.Font("Jacquard24-Regular.ttf", 130)
    font_button = pygame.font.Font("Jacquard24-Regular.ttf", 55)

    pygame.display.set_caption("Mad and madder")

    base_text_color = (150, 150, 180)
    base_text_hover = (255, 255, 255)

    play_button = create_button(
    screen.get_width() / 2 - 50, 310, 100, 55, "Play",
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

    pygame.mixer.music.load(ASSETS["sounds"]["music"]["main_theme"])
    pygame.mixer.music.set_volume(options["volume"])
    pygame.mixer.music.play(-1)

    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if check_click_button(event, play_button, ASSETS, options):
                return "play"
            if check_click_button(event, options_button, ASSETS, options):
                return "options"
            if check_click_button(event, quit_button, ASSETS, options):
                return "quit"
        
        for button in buttons:
            update_hover_button(button)
        
        screen.fill('#0a141e')

        tittle_text = font_title.render("Mad and madder", True, (255, 255, 255))
        screen.blit(tittle_text, (screen.get_width() / 2 - tittle_text.get_width() / 2, 100))

        for button in buttons:
            draw_button(screen, button)

        pygame.display.flip()
        clock.tick(30)
    
    return choice


def death_menu(screen, clock, options, ASSETS):
    font_title = pygame.font.Font("Jacquard24-Regular.ttf", 130)
    font_button = pygame.font.Font("Jacquard24-Regular.ttf", 55)

    pygame.display.set_caption("Mad and madder")

    base_text_color = (150, 150, 180)
    base_text_hover = (255, 255, 255)


    retry_button = create_button(
        screen.get_width() / 2 - 75, 300, 150, 60, "Retry",
        font_button, base_text_color, base_text_hover
    )
    main_menu_button = create_button(
    screen.get_width() / 2 - 75, 400, 150, 60, "Main menu",
    font_button, base_text_color, base_text_hover
    )

    buttons = [retry_button, main_menu_button]

    pygame.mixer.music.load(ASSETS["sounds"]["music"]["main_theme"])
    pygame.mixer.music.set_volume(options["volume"])
    pygame.mixer.music.play(-1)

    fundo = pygame.Surface((1280,720))
    fundo.set_alpha(4)
    fundo.fill('dark red')

    for i in range(61):
        
        screen.blit(fundo, (0,0))
        pygame.display.flip()
        clock.tick(30)

    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if check_click_button(event, retry_button, ASSETS, options):
                return "play"
            if check_click_button(event, main_menu_button, ASSETS, options):
                return "main_menu"
            
        
        for button in buttons:
            update_hover_button(button)
        
            #screen.fill('#0a141e00')
            

        tittle_text = font_title.render("You lose", True, (139, 0, 0))
        tittle_shadow = font_title.render("You lose", True, (0, 0, 0))
        screen.blit(tittle_shadow, (screen.get_width() / 2 - tittle_shadow.get_width() / 2 + 5, 105))
        screen.blit(tittle_text, (screen.get_width() / 2 - tittle_text.get_width() / 2, 100))

        for button in buttons:
            draw_button(screen, button)

        pygame.display.flip()
        clock.tick(30)
    
    return choice


def pause_menu(screen, clock, options, ASSETS):
    font_title = pygame.font.Font("Jacquard24-Regular.ttf", 130)
    font_button = pygame.font.Font("Jacquard24-Regular.ttf", 55)
    
    base_text_color = (150, 150, 180)
    base_text_hover = (255, 255, 255)

    resume_button = create_button(
        screen.get_width() / 2 - 70, 300, 140, 50, "Resume", font_button, base_text_color, base_text_hover
    )
    options_button = create_button(
        screen.get_width() / 2 - 75, 390, 150, 60, "Options",
        font_button, base_text_color, base_text_hover
    )
    main_menu_button = create_button(
        screen.get_width() / 2 - 110, 500, 220, 45, "Main Menu", font_button, base_text_color, base_text_hover
    ) 

    buttons = [resume_button, options_button, main_menu_button]

    choice = None

    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "play"        
            if check_click_button(event, resume_button, ASSETS, options):
                return "play"
            if check_click_button(event, options_button, ASSETS, options):
                options_menu(screen, clock, options, "pause", ASSETS) 
            if check_click_button(event, main_menu_button, ASSETS, options):
                return "main_menu"
        
        for button in buttons:
            update_hover_button(button)

        screen.fill((10, 20, 30))

        tittle_text = font_title.render("Paused", True, (255, 255, 255))
        screen.blit(tittle_text, (screen.get_width() / 2 - tittle_text.get_width() / 2, 100))

        for button in buttons:
            draw_button(screen, button)

        pygame.display.flip()
        clock.tick(30)
        
    return choice

def options_menu(screen, clock, options, return_to, ASSETS):
    font_title = pygame.font.Font("Jacquard24-Regular.ttf", 130)
    font_button = pygame.font.Font("Jacquard24-Regular.ttf", 55)
    font_value = pygame.font.Font("Jacquard24-Regular.ttf", 50)

    base_text_color = (150, 150, 180)
    base_text_hover = (255, 255, 255)
    pygame.display.set_caption("Mad and madder")

    back_button = create_button(
        screen.get_width() / 2 - 50, 500, 100, 55, "Back",
        font_button, base_text_color, base_text_hover
    )
    buttons = [back_button]

    slider_barra_rect = pygame.Rect(screen.get_width() / 2 - 150, 320, 300, 10)
    x_button = slider_barra_rect.x + (slider_barra_rect.width * options["volume"])
    slider_button_rect = pygame.Rect(x_button - 5, 310, 10, 30)

    slider_arrastando = False
    choice = None

    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if check_click_button(event, back_button, ASSETS, options):
                return return_to
            
            if event.type == pygame.MOUSEBUTTONDOWN and slider_button_rect.collidepoint(event.pos):
                slider_arrastando = True
            if event.type == pygame.MOUSEBUTTONUP:
                slider_arrastando = False

            if event.type == pygame.MOUSEMOTION:
                if slider_arrastando:
                    mouse_x = event.pos[0]
                    new_volume = (mouse_x - slider_barra_rect.x) / slider_barra_rect.width

                    if new_volume < 0:
                        new_volume = 0
                    if new_volume > 1:
                        new_volume = 1
                    
                    new_volume *= 100
                    new_volume = round(new_volume)
                    new_volume /= 100
                    
                    options["volume"] = new_volume
                    pygame.mixer.music.set_volume(options["volume"])

        for button in buttons:
            update_hover_button(button)

        slider_button_rect.centerx = slider_barra_rect.x + (slider_barra_rect.width * options["volume"])

        screen.fill((10, 20, 30))

        tittle_text = font_title.render("Options", True, (255, 255, 255))
        screen.blit(tittle_text, (screen.get_width() / 2 - tittle_text.get_width() / 2, 100))

        value_in_text = f"{int(options['volume'] * 100)}%"
        texto_volume_surface = font_value.render(value_in_text, True, (255, 255, 255))
        text_x = slider_barra_rect.right + 15
        text_y = slider_barra_rect.centery
        screen.blit(texto_volume_surface, (text_x, text_y - texto_volume_surface.get_height() / 2))
        
        pygame.draw.rect(screen, base_text_color, slider_barra_rect)
        pygame.draw.rect(screen, (255, 255, 255), slider_button_rect)

        for button in buttons:
            draw_button(screen, button)

        pygame.display.flip()
        clock.tick(60)
    
    return choice

def victory_menu(screen, clock, options, ASSETS):
    font_title = pygame.font.Font("Jacquard24-Regular.ttf", 150)
    font_button = pygame.font.Font("Jacquard24-Regular.ttf", 50)

    base_text_color = (150, 150, 180)
    base_text_hover = (255, 255, 255)
    pygame.display.set_caption("Mad and madder")

    main_menu_button = create_button(
    screen.get_width() / 2 - 110, 500, 220, 45, "Main Menu", font_button, base_text_color, base_text_hover
    ) 

    buttons = [main_menu_button]

    choice = None
    while choice is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
            if check_click_button(event, main_menu_button, ASSETS, options):
                return "main_menu"
            
        for button in buttons:
            update_hover_button(button)

        screen.fill((10, 20, 30))

        tittle_text = font_title.render("VICTORY", True, (255, 255, 255))
        screen.blit(tittle_text, (screen.get_width() / 2 - tittle_text.get_width() / 2, 200))

        for button in buttons:
            draw_button(screen, button)
    
        pygame.display.flip()
        clock.tick(30)

    return choice