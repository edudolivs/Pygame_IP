import pygame
import img 

def run(game_state):
    while game_state["running"]:

        game_state["player_pos"][0] += (game_state["movement"][1] - game_state["movement"][0])  * game_state["player_speed"]
        
        game_state["screen"].blit(game_state["background"], game_state["background_pos"])
        game_state["screen"].blit(game_state["pillars"], game_state["background_pos"])
        game_state["screen"].blit(game_state["floor"], game_state["background_pos"])
        game_state["screen"].blit(game_state["character"], game_state["player_pos"])

        character_hitbox = pygame.Rect(game_state["player_pos"][0], game_state["player_pos"][1], game_state["character"].get_width(), game_state["character"].get_height())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state["running"] = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game_state["movement"][0] = True
                if event.key == pygame.K_d:
                    game_state["movement"][1] = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    game_state["movement"][0] = False
                if event.key == pygame.K_d:
                    game_state["movement"][1] = False

            if character_hitbox.colliderect(game_state["collision_area"]):
                pygame.draw.circle(game_state["screen"], (0, 100, 255), game_state["player_pos"], 40)
        
        
        pygame.display.update()
        game_state["clock"].tick(60)

def main():
    
    pygame.init()
    pygame.display.set_caption("O rei corrompido")

    game_state = {
    "screen": pygame.display.set_mode((1280, 720)),
    "clock": pygame.time.Clock(),
    "running": True,
    "background": img.resized_background,
    "floor": img.resized_floor,
    "pillars": img.resized_pillars,
    "background_pos": [0, 0],
    "movement": [False, False],
    "player_pos": [20, 500],
    "player_speed": 3,
    "character": img.resized_character,
    "collision_area": pygame.Rect(300, 500, 300, 50)
    } 

    run(game_state)


if __name__ == "__main__":
    main()