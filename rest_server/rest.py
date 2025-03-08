import logging

from flask_restful import Api

from config import Config
from rest_server import create_app
from rest_server.resources import PlanetResource, GovernmentResource, StateResource, CityResource

# app initialization
app = create_app()
api = Api(app)

# logging configuration
app.config['LOGGING_LEVEL'] = Config.REST_LOGGING_LEVEL
app.config['LOGGING_FILE'] = Config.REST_LOGGING_FILE
logger = logging.getLogger('werkzeug')
log_level = getattr(logging, app.config['LOGGING_LEVEL'].upper(), logging.INFO)
logger.setLevel(log_level)
file_handler = logging.FileHandler(app.config['LOGGING_FILE'])
file_handler.setLevel(log_level)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# resource connect
api.add_resource(PlanetResource,
                 '/planets',
                 '/planets/<int:id>',
                 '/add_planet',
                 '/update_planet/<int:id>',
                 '/delete_planet/<int:id>'
                 )
api.add_resource(GovernmentResource,
                 '/governments',
                 '/governments/<int:id>',
                 '/add_government',
                 '/update_government/<int:id>',
                 '/delete_government/<int:id>'
                 )
api.add_resource(StateResource,
                 '/states',
                 '/states/<int:id>',
                 '/add_state',
                 '/update_state/<int:id>',
                 '/delete_state/<int:id>'
                 )
api.add_resource(CityResource,
                 '/cities',
                 '/cities/<int:id>',
                 '/add_city',
                 '/update_city/<int:id>',
                 '/delete_city/<int:id>'
                 )


@app.route('/forbidden', methods=['GET'])
def forbidden():
    return {"message": "Forbidden access"}, 403


@app.route('/method_not_allowed', methods=['GET, POST'])
def method_not_allowed():
    return {"message": "Method not allowed"}, 405

@app.route('/error', methods=['GET'])
def trigger_error():
    return 1 / 0


if __name__ == '__main__':
    app.run(host=Config.REST_SERVER_HOST, port=Config.REST_SERVER_PORT, debug=Config.REST_DEBUG)
