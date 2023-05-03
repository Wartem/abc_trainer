import threading
import urllib.request

import threading
import urllib.request
import time

class GetInternetAccess():
    def __init__(self, time_out) -> None:
        self.time_out = time_out
        self.connection_status = False

    def get_status(self):
        def _is_connected():
            try:
                urllib.request.urlopen('https://google.com', timeout=self.time_out)
                return True
            except urllib.request.URLError:
                return False

        self.connection_status = _is_connected()
        print("Internet status: ", self.connection_status)

        return self.connection_status
    

class InternetAccess():
    
    def __init__(self, time_out) -> None:
        self.time_out = time_out
        self.connection_status = False
        self.mutex = threading.Lock()
        
        
    def _start(self):
        def _update_connection_status():
            def _is_connected():
                try:
                    urllib.request.urlopen('https://google.com', timeout=self.time_out)
                    return True
                except urllib.request.URLError:
                    return False
            
            while True:
                with self.mutex:
                    self.connection_status = _is_connected()
                    print("Internet status: ", self.connection_status)
                time.sleep(self.time_out)
            
        threading.Thread(target=_update_connection_status, daemon=True).start()
            
            
    def get_status(self):
        with self.mutex:
            connection_status_copy = self.connection_status
        
        return connection_status_copy
    
    

    """ class InternetAccess():
    
    def __init__(self, time_out) -> None:
        In interval checks for internet connection.

        Args:
            time_out (int): Interval in seconds.
               
        self.time_out = time_out
        self.connection_status = False
        self.mutex = threading.Lock()
        self._start()
        
    def _start(self):
        def _update_connection_status():
            def _is_connected():
                try:
                    urllib.request.urlopen('https://google.com', timeout=self.time_out)
                    return True
                except urllib.request.URLError:
                    return False
            
            with self.mutex:
                self.connection_status = _is_connected()
            
        threading.Thread(target=_update_connection_status).start()
            

    def get_status(self):
        with self.mutex:
            
            return self.connection_status """