import pygame
from random import randint

 
class Monster(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == "zombie":
            self.zombie_walk_1 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (1).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_2 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (2).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_3 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (3).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_4 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (4).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_5 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (5).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_6 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (6).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_7 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (7).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_8 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (8).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_9 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (9).png').convert_alpha(), 0 , 0.15), True, False)
            self.zoombie_walk_10 = pygame.transform.flip(pygame.transform.rotozoom(pygame.image.load('graphics/monster/walk/Walk (10).png').convert_alpha(), 0 , 0.15), True, False)
            self.frames=[self.zombie_walk_1, self.zoombie_walk_2, self.zoombie_walk_3, self.zoombie_walk_4, self.zoombie_walk_5, self.zoombie_walk_6, self.zoombie_walk_7, self.zoombie_walk_8, self.zoombie_walk_9, self.zoombie_walk_10]         
            y_pos = 500      
        else:
            self.fly_1 = pygame.transform.rotozoom(pygame.image.load('graphics/monster/fly/Fly1.png').convert_alpha(), 0 , 1)
            self.fly_2 = pygame.transform.rotozoom(pygame.image.load('graphics/monster/fly/Fly2.png').convert_alpha(), 0 , 1)
            self.frames = [self.fly_1, self.fly_2]
            y_pos = 300
      
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))
    def animation_state (self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]        
    def update(self):
        #print(self.rect.x)
        self.animation_state() 
        self.rect.x -= 2
        self.destroy()
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
  