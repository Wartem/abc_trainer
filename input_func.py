import pygame
import unicodedata

'''
Potential issues:

It seems that the InputFunc class is meant to be used as a utility class, 
with all of its methods being static. Therefore, it may be better to declare 
them as such by adding the @staticmethod decorator.
The get_key_pressed_if_any method only returns the uppercase representation 
of the key pressed, which may not be desirable in all cases. It may be better 
to return a tuple containing both the uppercase and lowercase representation 
of the key pressed, to allow for more flexibility.
The unicodedata module may not work as expected for all languages and character 
sets, so it may be necessary to consider other approaches for filtering input.
'''

#from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT

class InputFunc:
 
    def exit_event_pressed(events):
        for event in events:
            if event.type == pygame.QUIT:
                return True

        return False

    def esc_pressed_event(events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
                

    def get_key_pressed_if_any(events):
        '''
         We only want letters. 
         unicodedata.category() function returns a string that starts with a letter 
         indicating the category of the character.
         "L" : Letters
         "N" : Numbers
        '''
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.unicode and unicodedata.category(event.unicode)[0] in "LN":
                    return pygame.key.name(event.key).upper()

        return False