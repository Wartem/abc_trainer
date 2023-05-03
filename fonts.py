import os
import pygame

from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QApplication, QLabel

from typing import Dict, Tuple


def get_font_paths(fonts_folder_path="fonts"):
    file_names = os.listdir(fonts_folder_path)
    
    # Filter out non-TTF files
    ttf_file_names = [file_name for file_name in file_names if file_name.endswith('.ttf')]
    
    # Create list of font file paths
    font_paths = [os.path.join(fonts_folder_path, file_name) for file_name in ttf_file_names]
    
    return sorted(font_paths)


def get_formatted_name(font_path):
    filename, extension = os.path.splitext(font_path)
    name = os.path.basename(filename)
    parts = name.rsplit("-")
    name = parts[0]
    
    name = ''.join(c if c.islower() else f" {c}" for c in name)
    name = name.lstrip()
    
    return name


def get_pygame_fonts(font_paths: list, font_size=16):
    
    # Initialize Pygame and its font module
    pygame.init()
    pygame.font.init()

    fonts = {}
    
    # Load a font
    for font_path in font_paths:
        font = pygame.font.Font(font_path, font_size)
        font_name = get_formatted_name(font_path)
        
        fonts.update({font_name: (font, font_path)})
        
    return fonts


def get_font_paths_dict(font_paths: list):
    paths = {}
   
    for font_path in font_paths:
        font_name = get_formatted_name(font_path)
        paths.update({font_name: font_path})
        
    return paths


def get_pygame_font(font_path: str, size):
    return pygame.font.Font(font_path, size)
    
    
_font_cache = {}


def get_pyside6_font(font_path: str, font_size: int) -> Dict[str, Tuple[QFont, str]]:
    """
    Loads a font from the given file path and returns a dictionary
    containing the font object and the original file path.

    :param font_path: The file path to the font file.
    :param font_size: The desired font size.
    :return: A dictionary containing the font object and the original file path.
    :raises ValueError: If there are no font families for the specified `font_id`.
    """
    
    font = _font_cache.get((font_path, font_size))
    if font is not None:
        return font

    font_name = get_formatted_name(font_path)
    font_id = QFontDatabase.addApplicationFont(font_path)
    families = QFontDatabase.applicationFontFamilies(font_id)

    if not families:
        raise ValueError(f"error font families {font_id} {font_path}")
    
    font_family = families[0]
    font = QFont(font_family, font_size)
    _font_cache[(font_path, font_size)] = {font_name: (font, font_path)}

    return _font_cache[(font_path, font_size)]    
        

def get_pyside6_font_org(font_path, font_size):
    font = None
    font_name = get_formatted_name(font_path)
    font_id = QFontDatabase.addApplicationFont(font_path)
    families = QFontDatabase.applicationFontFamilies(font_id)
    
    if not families:
        print("error font families", font_id, font_path)
        
    else:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, font_size)
        
    return {font_name: (font, font_path)}


def get_pyside6_fonts(font_paths: list, font_size=16):
    fonts = {}

    try:
        for font_path in font_paths:
            fonts.update(get_pyside6_font(font_path, font_size))
    except ValueError as e:
        print(f"Failed to load font: {e}")

    return fonts

