import os
import sys

from combine_service import get_courier_routes
from export_service import generate_excel
from config import Config

cfg = Config()
base_path = cfg.get('base_path')

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle (compiled executable)
    base_path = os.path.join(os.path.dirname(sys.executable), '..')
output_file =  os.path.join(base_path, cfg.get('output_file'))

if __name__ == "__main__":
    generate_excel(get_courier_routes(), output_file)
