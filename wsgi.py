from core import create_app
from config import config_options

app = create_app(config_options['production'])

