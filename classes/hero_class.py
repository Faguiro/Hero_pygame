import pygame
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.hero_idle_1 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (1).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_2 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (2).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_3 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (3).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_4 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (4).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_5 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (5).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_6 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (6).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_7 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (7).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_8 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (8).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_9 =  pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (9).png').convert_alpha(), 0 , 0.15)
        self.hero_idle_10 = pygame.transform.rotozoom(pygame.image.load('graphics/hero/idle/Idle (10).png').convert_alpha(), 0 , 0.15)
        self.hero_walk = [self.hero_idle_1, self.hero_idle_2, self.hero_idle_3, self.hero_idle_4, self.hero_idle_5, self.hero_idle_6, self.hero_idle_7, self.hero_idle_8, self.hero_idle_9, self.hero_idle_10]
        self.hero_index = 0
        self.hero_jump =pygame.transform.rotozoom( pygame.image.load('graphics/hero/jump/Jump (1).png').convert_alpha(), 0 , 0.15)
                
        self.image = self.hero_walk[self.hero_index]
        self.rect = self.image.get_rect(midbottom=(80, 500))
        self.gravity=0        
        self.sound_jump = pygame.mixer.Sound('sounds/jump.mp3')
        self.sound_jump.set_volume(0.2)
    def hero_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 500:
            self.gravity = -20
            self.sound_jump.play()
    def aply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 500:
            self.rect.bottom = 500            
    def animation_tate(self):     
        if self.rect.bottom < 500:
            self.image = self.hero_jump
        else:
            self.hero_index += 0.1
            if self.hero_index >= len(self.hero_walk):
                self.hero_index = 0
            self.image = self.hero_walk[int(self.hero_index)]
    def update(self):
        self.hero_input()
        self.aply_gravity()
        self.animation_tate()
  