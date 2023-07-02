import pygame
from classes.hero_class import Hero

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hero, the game!")
clock = pygame.time.Clock()
test_font = pygame.font.Font("fonts/VanillaCaramel.otf", 40)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('sounds/music.wav')

bg_music.set_volume(0.2)
bg_music.play(loops=-1)

hero = pygame.sprite.GroupSingle()
hero.add(Hero())

obstacle_group = pygame.sprite.Group()

################### Tela do jogo: #################
# background
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()


################### Timer do jogo: #################
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1900)

################# Tela de introdução: #################
game_name = test_font.render("Hero, the game!", False, (64, 64, 64)).convert()
game_name_rect = game_name.get_rect(center=(400, 80))
hero_stand = pygame.transform.rotozoom(pygame.image.load(
    "graphics/hero/hero_big.png").convert_alpha(), 0, 0.4)  # rotation, scale
hero_stand_rect = hero_stand.get_rect(center=(400, 300))
game_message = test_font.render(
    "Pressione espaço para começar", False, (64, 64, 64)).convert()
game_message_rect = game_message.get_rect(center=(400, 500))
#########################################################
