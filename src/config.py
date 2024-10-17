import os
import sys

import yaml

class Config:
    _instance = None

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Determine the base path for the files
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle (compiled executable)
        base_path = sys._MEIPASS

    def __new__(cls, config_file= os.path.join(base_path, './config.yaml')):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            with open(config_file) as f:
                cls._instance.cfg = yaml.load(f, Loader=yaml.FullLoader)
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Determine the base path for the files
        if getattr(sys, 'frozen', False):
            # If the application is run as a bundle (compiled executable)
            base_path = os.path.join(os.path.dirname(sys.executable), '..')


        cls._instance.cfg['base_path'] = base_path
        return cls._instance

    def get(self, key):
        return self.cfg.get(key)