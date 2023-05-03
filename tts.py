import os
from gtts import gTTS
from pygame import mixer
import time
import socket

from translator import Translator
from settings import Settings

import internet_access


class TTS:
    def __init__(self, lang, slow_speech, caller_instance=None) -> None:
       
        self.caller_instance = caller_instance
        
        self._audio_queue = []
        self.tts = None
        self.slow = slow_speech
        self.lang = lang
        self.audio_dir = "./audio/"
        self.audio_format = ".mp3"
        self.create_folders()
        self.slow = False
        self.has_been_busy = False
        self.first_done = False
        mixer.init()
        self.settings = Settings.r_setup()
        mixer.music.set_volume(self.settings["volume"]/100)
        self.no_internet = 0
        
        # Internet
        self.internet_access = internet_access.GetInternetAccess(5) # 60
        
    
    def create_folders(self):
        sub_folders = [f'{self.audio_dir}{k}/' for k in Translator().keys()]

        os.makedirs(self.audio_dir, exist_ok=True)

        for sub_folder in sub_folders:
            os.makedirs(sub_folder, exist_ok=True)
            os.makedirs(os.path.join(sub_folder, "normal"), exist_ok=True)
            os.makedirs(os.path.join(sub_folder, "slow"), exist_ok=True)


    def queue_text(self, text, stop_current=False):
        
        print("Text added for playing: -->" + text + "<-- ")
        
        if stop_current:
            self.stop_playing()
        
        speed = "slow" if self.slow else "normal"
        file_name = os.path.join(self.audio_dir, self.lang, speed, f"{text}{self.audio_format}")
        
        if self._save_tts(text, file_name):
            self._audio_queue.append((file_name, stop_current))
        
        
    def simulate_no_internet(func):
        def wrapper(*args, **kwargs):
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Set the timeout value to 0.001 seconds
            s.settimeout(0.001)
            try:
                # Attempt to call the function
                result = func(*args, **kwargs)
            except socket.timeout:
                # If the socket times out, return None to simulate no internet
                result = None
            finally:
                # Close the socket object
                s.close()
            return result
        
        return wrapper
        
    
    def _remove_bad_file(self, file_path, max_retries=3):
        if os.path.isfile(file_path):
            # Check if the saved file is corrupt
            file_size = os.path.getsize(file_path)
    
            if file_size <= 1:
                # Remove the file if its size is 1 byte or lower
                os.remove(file_path)
                print(f"File {file_path} removed.")
            else:
                print(f"File {file_path} not removed. File size is {file_size} bytes.")
        
    
    def wait_for_internet(self, max_sec):
        internet = False
        start_time = time.time()
        
        while not internet:
            if time.time() - start_time >= max_sec:
                internet = self.internet_access.get_status()
                print("Internet:", internet)
                return internet
                
            self.caller_instance.extern_run_no_internet()

        print("Internet access found") 
        return True
    
    
    def wait_(self, max_sec):
        start_time = time.time()
        
        while time.time() - start_time < max_sec:
            self.caller_instance.extern_run_no_internet()
               
                
    def _save_tts(self, text:str, file_name: str):
        self._remove_bad_file(file_name)

        # Only save if not already existing
        if not os.path.isfile(file_name):
            try:
                # generate text-to-speech output
                self.tts = gTTS(text, lang=self.lang, slow=self.slow)
                self.tts.save(file_name)
                return True
                        
            except Exception as e:
                print(f"_save_tts error {file_name}: {e}")
                if self.wait_(3):
                    return False
                    #self._save_tts(text, file_name)
                    #pass # uncomment this line if you need to do something here later

        #if not self._remove_bad_file(file_name):
        return True
                
                
    def get_busy(self):
        busy = mixer.music.get_busy()
        
        if busy:
            self.has_been_busy = True
            
        if not busy and self.has_been_busy:  
            self.first_done = True
            
        #return mixer.music.get_busy()
        return busy
    

    def check_queue(self):
        if self._audio_queue and not mixer.music.get_busy():
            next_file, stop = self._audio_queue.pop(0)

            if os.path.exists(next_file):
                
                try:
                    mixer.music.load(next_file)
                    mixer.music.play()
                except Exception as e:
                    print(f"_play_file error for {next_file}: {e}")
                    #self._remove_bad_file(next_file)
            else:
                print(f"{next_file} doesn't exist.")
                
        
    def check_queue_old(self):
        
        if self._audio_queue and not mixer.music.get_busy():
            next_file = self._audio_queue.pop(0)
            
            try:
                mixer.music.load(next_file[0])
                #print(next_file[0])
                mixer.music.play()
                
            except OSError:
                    print(f"{next_file[0]} doesn't exists.")
            except:
                    print("_play_file error for", next_file[0])
        
        
    def stop_playing(self):
        mixer.music.stop()
        self.clean_queue()
        
        
    def clean_queue(self):
        self._audio_queue.clear()