import pygame
import img 

def get_entity(e_type, pos, size):
    return {
        'type': e_type,
        'pos': list(pos),
        'size': size,
        'vel': [0, 0],
        'rect': pygame.Rect(pos, size),
        'action': 'still'
    }

def run(game):
    player = game['player'] 

    while game["running"]:
       
        player_velocity_x = (player['movement'][1] - player['movement'][0]) * player['speed']
        
        
        player['pos'][0] += player_velocity_x

        
        player['rect'].x = player['pos'][0]
        
      
        game["screen"].blit(game["background"], game["background_pos"])
        game["screen"].blit(game["pillars"], game["background_pos"])
        game["screen"].blit(game["floor"], game["background_pos"])
        
       
        game["screen"].blit(player['image'], player['pos'])

       
        if player['rect'].colliderect(game["collision_area"]):
            
            center_pos = (player['pos'][0] + player['size'][0] // 2, player['pos'][1] + player['size'][1] // 2)
            pygame.draw.circle(game["screen"], (0, 100, 255), center_pos, 40)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game["running"] = False
                break
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player['movement'][0] = True 
                if event.key == pygame.K_d:
                    player['movement'][1] = True 
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player['movement'][0] = False
                if event.key == pygame.K_d:
                    player['movement'][1] = False
        
        pygame.display.update()
        game["clock"].tick(60)

def main():

    pygame.init()
    pygame.display.set_caption("O rei corrompido")

    
    character_img = img.resized_character
    player_size = character_img.get_size() 
    player_start_pos = (20, 500)
    
    player_entity = get_entity('player', player_start_pos, player_size)
    
    player_entity['speed'] = 4
    player_entity['image'] = character_img
    player_entity['movement'] = [False, False] 

    game_state = {
        "screen": pygame.display.set_mode((1280, 720)),
        "clock": pygame.time.Clock(),
        "running": True,
        "background": img.resized_background,
        "floor": img.resized_floor,
        "pillars": img.resized_pillars,
        "background_pos": [0, 0],
        "collision_area": pygame.Rect(300, 500, 300, 50),
        "player": player_entity
    } 

    run(game_state)

if __name__ == "__main__":
    main()