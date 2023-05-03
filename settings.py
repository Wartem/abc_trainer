import random
import json

import os

from typing import Union, Optional

# get the current directory
""" current_directory = os.path.dirname(os.path.abspath(__file__))
setup_json = os.path.join(current_directory, 'settings', 'setup.json')
menu_text_json = os.path.join(current_directory, 'settings', 'menu_text.json')
instructions_lang_json = os.path.join(current_directory, 'settings', 'instructions.json')
extra_chars_json = os.path.join(current_directory, 'settings', 'extra_chars.json') """

import sys

if getattr(sys, 'frozen', False):
    current_directory = os.path.dirname(sys.executable)
else:
    current_directory = os.path.dirname(os.path.realpath(__file__))

setup_json = os.path.join(current_directory, 'settings', 'setup.json')
menu_text_json = os.path.join(current_directory, 'settings', 'menu_text.json')
instructions_lang_json = os.path.join(current_directory, 'settings', 'instructions.json')
extra_chars_json = os.path.join(current_directory, 'settings', 'extra_chars_not_yet_in_use.json')


""" import sys
# Get the path to the folder containing the executable file
exe_dir = os.path.dirname(sys.executable)

# Get the path to the settings folder
settings_dir = os.path.join(exe_dir, 'settings')

# Set the paths to the JSON files
setup_json = os.path.join(settings_dir, 'setup.json')
menu_text_json = os.path.join(settings_dir, 'menu_text.json')
instructions_lang_json = os.path.join(settings_dir, 'instructions.json')
extra_chars_json = os.path.join(settings_dir, 'extra_chars.json') """

""" if getattr(sys, 'frozen', False):
    # running from bundled exe
    current_directory = sys._MEIPASS
else:
    # running normally
    current_directory = os.path.dirname(os.path.abspath(__file__))

setup_json = os.path.join(current_directory, 'settings', 'setup.json')
menu_text_json = os.path.join(current_directory, 'settings', 'menu_text.json')
instructions_lang_json = os.path.join(current_directory, 'settings', 'instructions.json')
extra_chars_json = os.path.join(current_directory, 'settings', 'extra_chars.json') """

default_settings = {
    "user_name": "User",
    "slow_speech": False,
    "language": "English",
    "repetitions": 2,
    "letter_case": "UPPER",
    "instructions": True,
    "font": "arial",
    "text_color": "#82b5d1",
    "full_screen": False,
    "window_width": 1400,
    "window_height": 900,
    "background_color": "#82b5d1"
}

class Settings:
    
    @staticmethod
    def _read_settings(setting, rand=False) -> str:
        if rand:
            return random.choice(Settings.all_settings[setting]).upper()
        return Settings.all_settings[setting].upper()
    
    @staticmethod
    def read_json(json_file):
        with open(json_file, "r", encoding="utf-8") as f:
                return dict(json.load(f))
        

        '''
        0 arguments returns the settings.json as a dict.
        arg1 None and arg2 setting returns the setting in the settings.
        2 arguments returns the setting arg2 in the specified dict arg1.
        '''    

    @staticmethod
    def r_setup(settings: Optional[dict] = None, single_setting: Optional[str] = None) -> Union[dict, str]:
        """
        Return setup settings from a JSON file or a provided dictionary.

        Args:
            settings (Optional[dict]): A dictionary containing setup settings. Defaults to None.
            single_setting (Optional[str]): A specific setting to retrieve from the dictionary. Defaults to None.

        Returns:
            Union[dict, str]: A dictionary of all settings or a specific setting value as a string.

        Raises:
            Exception: If there's an error while reading the JSON file.

        Notes:
            - If both `settings` and `single_setting` are provided, return the value for the specified setting.
            - If only `single_setting` is provided, return the value for the specified setting from the JSON file.
            - If `settings` is provided, return the entire dictionary.
            - If no arguments are provided, return the entire dictionary from the JSON file.
            - If an error occurs while reading the JSON file, return default settings.
        """
        
        try:
            if settings is not None and single_setting is not None:
                return settings[single_setting]
            
            if settings is None and single_setting is not None:
                return Settings.read_json(setup_json)[single_setting]

            if settings is not None:
                return settings

            return Settings.read_json(setup_json)
        
        except Exception as e:
            print(f"Error reading setup.json: {e}")
            return default_settings.get(single_setting) if single_setting else default_settings

        
    @staticmethod
    def r_instructions():
        return Settings.read_json(instructions_lang_json)
    
    
    @staticmethod
    def r_extra_chars():
        return Settings.read_json(extra_chars_json)
    

    @staticmethod
    def _read_setting(key):
        return Settings.r_setup()[key]
    
    
    @staticmethod
    def r_menu_text():
        return Settings.read_json(menu_text_json)


    @staticmethod
    def change_setting(key, value):
        with open(setup_json, "r+", encoding="utf-8") as f:

            # json.dump(self.settings, outfile)
            data = json.load(f)
            data[key] = value
            f.seek(0)  # <--- resets file position to the beginning.
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()  # remove remaining part
            
            
    @staticmethod
    def write_settings_defect(settings):
        with open(setup_json, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.update(settings)
            f.seek(0)  # resets file position to the beginning.
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()  # remove remaining part
            
            
    @staticmethod
    def write_settings(settings):
        with open(setup_json, "r+", encoding="utf-8") as f:
            #f.seek(0)  # resets file position to the beginning.
            f.truncate()
            #print(settings)
            json.dump(settings, f, indent=4, ensure_ascii=False)