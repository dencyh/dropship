from combine_service import get_courier_routes
from export_service import generate_excel
from config import Config

if __name__ == "__main__":
    generate_excel(get_courier_routes(),  Config().get('output_file'))
