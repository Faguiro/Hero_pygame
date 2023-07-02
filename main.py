import pygame
from sys import exit
from random import randint, choice
from classes.hero_class import Hero
from classes.obstacle_class import Monster


################### Configurações iniciais: #################
pygame.init()
from config import *
from functions.default import diplay_score, colision_spite

while True:
################ loop de eventos #################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Monster(choice(["fly", "zombie"])))       
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                score = 0
                start_time = pygame.time.get_ticks()

   ################ renderização do jogo ativo #################
    if game_active:
        score = diplay_score()
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 380))
        diplay_score()        
       
        hero.draw(screen)
        hero.update()      
    
        obstacle_group.draw(screen)
        obstacle_group.update()
        game_active = colision_spite()        
   
    else:
        screen.fill((94, 129, 162))
        screen.blit(hero_stand, hero_stand_rect)        
        
        #message        
        score_message = test_font.render( "Score: " + str(score), False, (255, 255, 255)).convert()
        score_message_rect = score_message.get_rect(center=(400, 500))
        screen.blit(game_name, game_name_rect)

        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
