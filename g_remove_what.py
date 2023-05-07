import random
import pygame

import constants
from game import Game
from strings_on_screen import StringImage
from letter_handler import LetterHandler


class GameRemoveWhat(Game):
    def __init__(self):
        super().__init__()
        self.mode_name = self.trans.tr('Lone letter', self.lang)
        
        self.letter_handler = None
        self.set_letter_handler()
        self.string_in_use = self.letter_handler.set_letter_in_use()
        self.string_image = StringImage(self.font_path, self.get_pic_text(), self.screen, 1800, 0, 0, self.background_color, self.text_color)
        
        #self.mt_unique_txt = self.menu_texts[self.lang_code]["Unique"]
        #pygame.display.set_caption(f"{self.caption} - {self.mt_unique_txt}")
        pygame.display.set_caption(f"{self.caption} - {self.mode_name}")
        

    def get_pic_text(self):
        pic_text = [[self.get_additional() * 2] for _ in range(0, random.randint(1, 2))]
        
        random_index = random.randint(0, len(pic_text)) # changed by chat gpt from len(pic_text) - 1
        pic_text.insert(random_index, self.string_in_use)
        
        return ''.join(' '.join(c) for c in pic_text)
            

    def get_additional(self):
        return self.letter_handler.get_rand_addition()
        
        
    def set_letter_handler(self):
        self.letter_handler = LetterHandler(self.user_name[:4], 4, 7, self.lang, self.repetitions, self.letter_case, self.excluded_chars)
        
        
    def init_extended(self):
        self.draw_mode_welcome()
        self.tts.queue_text(self.trans.tr('Unique', self.lang))
        
        
    def handle_correct_key_pressed(self, key_pressed):
        more_letters = True
            
        if not self.letter_handler.available_letters and not self.letter_handler.letters_to_add:
            more_letters = False
            
        else:
            self.letter_handler.check_add_letter_counter()
        
        if (not more_letters or key_pressed == "") and self.progress != constants.PROGRESS_WIN:
            self.tts.queue_text(self.trans.tr('Passed', self.lang))
            self.tts.queue_text(f"{self.user_name}!")
            self.tts.queue_text(self.trans.tr('Very good', self.lang))
            self.progress = constants.PROGRESS_WIN

            return 
            
        else:  
            self.tts.queue_text(f"{key_pressed}", True)
                
            self.string_in_use = self.letter_handler.set_letter_in_use()
            
            if self.string_in_use:
                if self.instructions:
                    self.tts.queue_text(self.trans.tr('Good', self.lang))
                    self.tts.queue_text(self.trans.tr('Unique', self.lang))
                                        
                self.draw()
                    
                
                self.string_image = StringImage(self.font_path, self.get_pic_text(), self.screen, 1800, 0, 0, self.background_color, self.text_color)
            
            else:
                self.handle_correct_key_pressed("")
        
                
    def handle_key_pressed(self, key_pressed):
        start = not self.tts._audio_queue and self.letter_handler.correct_counter != self.letter_handler.correct_counter_goal
        
        if start:
        
            if key_pressed.upper() == self.string_in_use.upper():
                self.handle_correct_key_pressed(key_pressed)
                return
                
            self.tts.queue_text(f"{self.trans.tr('Try', self.lang)} {self.string_in_use}", True)
            self.letter_handler.correct_counter = 0