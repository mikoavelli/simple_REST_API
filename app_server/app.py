import logging

from flask import Flask

from config import Config
from app_server.routes import main_bp

# app initialization
app = Flask(__name__, template_folder='../templates')
app.config.from_object(Config)
app.register_blueprint(main_bp)

# logging configuration
app.config['LOGGING_LEVEL'] = Config.CLIENT_LOGGING_LEVEL
app.config['LOGGING_FILE'] = Config.CLIENT_LOGGING_FILE
logger = logging.getLogger('werkzeug')
log_level = getattr(logging, app.config['LOGGING_LEVEL'].upper(), logging.INFO)
logger.setLevel(log_level)
file_handler = logging.FileHandler(app.config['LOGGING_FILE'])
file_handler.setLevel(log_level)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

if __name__ == '__main__':
    app.run(host=Config.CLIENT_SERVER_HOST, port=Config.CLIENT_SERVER_PORT, debug=Config.CLIENT_DEBUG)
