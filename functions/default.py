from config import test_font, start_time, screen, hero, obstacle_group
import pygame

####### Funções: #######	
def diplay_score():
    current_time = round(int(pygame.time.get_ticks() - start_time)/1000)
    score_surf = test_font.render(f'Score: {current_time}', False, (220, 220, 220))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def colision_spite():
    if pygame.sprite.spritecollide(hero.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True
