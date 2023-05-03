import pygame
import constants
from settings import Settings
from color_constants import ColorConst
from input_func import InputFunc
from fonts import get_font_paths, get_font_paths_dict
import tts
from translator import Translator
from strings_on_screen import StringImage
from text_icon_gen import Gen


class Game:
    #TODO: Make specical characters requiring multiple presses work
    #TODO: Fix distorted tts voices for chars in some languages.
    
    def __init__(self) -> None:
        
        self.SCREEN_WIDTH = 0
        self.SCREEN_HEIGHT = 0
        
        self.user_name = ""
        self.full_screen = 0
        self.SCREEN_WIDTH_WINDOWED = 0
        self.SCREEN_HEIGHT_WINDOWED = 0
        self.lang = ""
        self.slow_speech = 0
        self.repetitions = 1
        self.instructions = 1
        
        self.screen = None
        self.progress = constants.PROGRESS_START
        self.FPS = 5
        self.background_color = ColorConst.BEIGE
        
        self.mode_name = "Welcome"
        #were gags invented in 1985? KEKW
        # Clock
        self.clock = pygame.time.Clock()
        
        # Translator
        self.trans = Translator()
        
        # Read Settings
        self.read_settings()
        if not self.user_name:
            self.user_name = "User"
        
        
        self.settings = Settings.r_setup()
        self.menu_texts = Settings.r_menu_text()
        self.lang_code = self.trans.get_code(self.settings["language"])
        self.extra_chars = Settings.r_extra_chars()
        
        # Caption
        self.caption = Settings.r_instructions()[self.lang]["Caption"]
        pygame.display.set_caption(self.caption)
        
        # TTS
        self.tts = tts.TTS(self.lang, self.slow_speech, caller_instance=self)
                
        # Screen
        infoObject = pygame.display.Info()
        self.MAX_SCREEN_WIDTH = infoObject.current_w
        self.MAX_SCREEN_HEIGHT = infoObject.current_h
        self.adjust_window_size()

        # Font
        self.font_paths = get_font_paths()
        self.font_paths_dict = get_font_paths_dict(self.font_paths)
        self.font_path = self.font_paths_dict[self.font_name_in_use]
        
        self.gen = Gen()
        
        # Create the Exit button in the upper left corner    
        # Save png to file
        back_img_file = "back_button.png"
        self.gen.create_exit_button(back_img_file)
        self.exit_button = pygame.image.load(back_img_file) #pygame.Rect(0, 0, 50, 25)
        self.string_image = StringImage(self.font_path, "", self.screen, 1800, 0, 0, self.background_color, self.text_color)
        
        self.size = pygame.RESIZABLE
        
    
    def read_settings(self):
        settings = Settings.r_setup()
        self.user_name = settings["user_name"]
        self.slow_speech = settings["slow_speech"]
        self.lang = self.trans.get_code(settings["language"])
        self.repetitions = settings["repetitions"]
        self.instructions = settings["instructions"]
        self.letter_case = settings["letter_case"]
        self.excluded_chars = settings["excluded_characters"]
        self.font_name_in_use = settings["font"]
        self.full_screen = settings["full_screen"]
        self.SCREEN_WIDTH_WINDOWED = settings["window_width"]
        self.SCREEN_HEIGHT_WINDOWED = settings["window_height"]
        self.text_color = settings["text_color"]
        self.background_color = settings["background_color"]
        
    
    def adjust_window_size(self):
        if int(self.full_screen):
            self.set_display_size_mode(constants.DISPLAY_MODE_FULLSCREEN)
        else:
            self.set_display_size_mode(constants.DISPLAY_MODE_WINDOWED)
    
        
    def set_display_size_mode(self, display_mode):
        resizeable = (display_mode == constants.DISPLAY_MODE_WINDOWED)
        self.size = pygame.RESIZABLE if resizeable else pygame.FULLSCREEN
        
        if resizeable:
            self.SCREEN_WIDTH = self.SCREEN_WIDTH_WINDOWED
            self.SCREEN_HEIGHT = self.SCREEN_HEIGHT_WINDOWED
            
        else:
            self.SCREEN_WIDTH = self.MAX_SCREEN_WIDTH
            self.SCREEN_HEIGHT = self.MAX_SCREEN_HEIGHT
            
        if self.screen:
            self.screen = pygame.transform.scale(self.screen, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) 
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), self.size)
        pygame.display.update()


    def draw(self):
        self.string_image.update()
        self.screen.blit(self.exit_button, (25, 25))
        pygame.display.flip() # update the whole screen (pygame.display.update() for certain parts only)
        
        
    def handle_correct_key_pressed(self, key_pressed):
        pass
                

    def handle_key_pressed(self, key_pressed):
        pass
            
            
    def init_extended(self):
        pass
    
    
    # Changed April 30
    def draw_error_no_internet(self):
        self.string_image = StringImage(self.font_path, "ERROR - No Internet Connection!", self.screen)
        self.string_image.background_color = ColorConst.RED4
        self.string_image.update()
        pygame.display.flip()
        
    
    # Changed April 30
    def draw_mode_welcome(self):
        string_image = StringImage(self.font_path, self.mode_name, self.screen) #self.tr(self.mode_name), self.screen)
        string_image.background_color = self.background_color # ColorConst.GREEN3 #YELLOW3
        string_image.text_color = self.text_color
        string_image.update()
        pygame.display.flip()
        
        
    def handle_key_input(self, events):
        """
        Handle keyboard input events.

        Parameters:
            events (list): A list of pygame events.

        Returns:
            None
        """
            
        if InputFunc.exit_event_pressed(events) or InputFunc.esc_pressed_event(events):
            self.progress = constants.PROGRESS_END
            return
        
        if not self.tts.first_done:
            return

        key_pressed = InputFunc.get_key_pressed_if_any(events)
        if not key_pressed:
            return

        self.handle_key_pressed(key_pressed) 
    
    
    def handle_mouse_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if self.exit_button.get_rect().collidepoint(mouse):
                    self.progress = constants.PROGRESS_END
                    
            
    def handle_window_size_changed(self, events):
        #ToDo:The standard approach to handling window movement and resizing in Pygame will pause 
        #ToDo:the event loop while the window is being moved or resized. One way to mitigate this 
        #ToDo:and keep the event loop running while the window is being moved or resized is to use 
        #ToDo:a separate thread to handle the window events.
        
        for event in events:
            if event.type == pygame.VIDEORESIZE:
                # ToDO: save to settings
                #self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                
                self.window_min_size_enforcement()
                self.string_image.update_text_size()
                self.draw()
    
    
    def window_min_size_enforcement(self):
        '''
        Ensures that the size of the Pygame display window meets a minimum size requirement of 400 pixels 
        in both the horizontal and vertical dimensions. 
        
        If the window size is less than 400 pixels in either dimension, the method sets the window size 
        to 400 pixels in that dimension.
        '''
        
        x, y = pygame.display.get_window_size()
        x = max(x, 400)
        y = max(y, 400)
        
        self.screen = pygame.display.set_mode((x, y), pygame.RESIZABLE)
    
    '''
    Potential issue:
    
    The end_after_tts() method is checking if self.tts.get_busy() is False before setting self.progress to constants.PROGRESS_END. 
    However, there is no guarantee that the TTS will finish playing within the same loop iteration, so this check may be incorrect.
    '''
    def end_after_tts(self):
        if not self.tts.get_busy():
            self.progress = constants.PROGRESS_END
    
    
    def get_events(self):
        return pygame.event.get()
    
    
    def extern_run_no_internet(self):
        self.clock.tick(self.FPS)
        events = self.get_events()
        self.handle_key_input(events)
        self.handle_mouse_input(events)
        self.handle_window_size_changed(events)
        #self.tts.check_queue()
        self.draw_error_no_internet()
        self.draw()
        
    
    def run(self):
        while self.progress:
            if self.progress == constants.PROGRESS_WIN:
                self.end_after_tts()

            self.clock.tick(self.FPS) 
            
            #if self.internet_access.get_status(): 
            #print("Internet OK")
            
            events = self.get_events()
            
            self.handle_key_input(events)
            self.handle_mouse_input(events)
            
            self.handle_window_size_changed(events)
            
            self.tts.check_queue()
            
            if not self.tts.get_busy():
                self.draw()
    
    
    def game_loop(self):
        print(self.mode_name)
        self.init_extended()
        self.run()