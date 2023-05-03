import string
import pygame
import sys
import os

#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

#from color_constants import ColorConst
from color_constants import ColorConst
from fonts import get_pygame_font


class StringImage(pygame.sprite.Sprite):
    def __init__(self, font_path: str, letter_str: str, screen: pygame.Surface, font_size = 1800, x: int = 0, y: int = 0, bg_color = ColorConst.BEIGE, text_color=ColorConst.BLACK):
        self.text = letter_str
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.x = x
        self.y = y
        #self.font_name = font_name
        self.font_size = font_size
        self.font = None
        self.font_path = font_path
        self.background_color = bg_color
        self.text_color = text_color
        self.move = lambda x: self.rect.move_ip(*x)
        self.img = None
        self.rect = None
        
        self.update_text_size()


    def update_text_size(self):
        #self.font = self._generate_font() 
        self.font = get_pygame_font(self.font_path, self.font_size)
        self.img = self._generate_img()
        self.img = self.scale_img(self.img)
        self.rect = self.img.get_rect()
        self.center_text(self.screen)
    
    
    def center_text(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.screen_rect.centerx - self.rect.centerx 
        self.rect.y = self.screen_rect.centery - self.rect.centery 
            
        
    def _draw(self):
        self.screen.fill(self.background_color)
    
        self.screen.blit(
            self.img,
            (
                self.rect.x,
                self.rect.y,
            ),
        )
        
        
    def update(self):
        #self._check_pos_limits()
        self._draw()
        
        
    def scale_img(self, image_surface: pygame.Surface) -> pygame.Surface:
        """Scales the image to fit the screen.
        
        Black box fix:
        The issue is likely that you are trying to scale a surface that has a colorkey set. When you scale the surface, 
        the colorkey is not being scaled with the rest of the surface, so the area that should be transparent is instead 
        being filled with the colorkey color, which is black by default.

        One way to fix this is to not set a colorkey when creating the surface, or to remove the colorkey after 
        scaling the surface. Another option is to use the pygame.Surface.convert_alpha() method on the surface 
        before scaling it, which will preserve the transparent areas when scaling.

        Args:
            image_surface (pygame.Surface): The image to be scaled.

        Returns:
            _type_: Scaled version of the image.
        """
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w - 50
        screen_height = screen_info.current_h - 50
        
        surface = image_surface
        surface_width, surface_height = surface.get_size()
        
        scale_x = screen_width / surface_width if surface_width else screen_width
        scale_y = screen_height / surface_height if surface_height else screen_height

        scale = min(scale_x, scale_y)

        return pygame.transform.scale(
            surface, (int(surface_width * scale), int(surface_height * scale))
            #surface, (int(surface_width * 0.5), int(surface_height * 0.5))
        ).convert_alpha()
        
        
    def _generate_img(self):
        return self.font.render(
            self.text, True, self.text_color
        )
