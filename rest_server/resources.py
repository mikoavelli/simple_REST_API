from flask import request
from datetime import datetime
from flask_restful import Resource

from db import execute_query, call_procedure

def parse_date(date_str):
    if not date_str:
        raise ValueError("Date cannot be empty")
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Date cannot be parsed")

class PlanetResource(Resource):
    def get(self, id=None):
        if not id:
            query = f"SELECT * FROM planets;"
        else:
            query = f"SELECT * FROM planets WHERE id = {id};"
        result = execute_query(query)
        for planet in result:
            planet['discovered_date'] = planet['discovered_date'].isoformat() if planet['discovered_date'] else None
        if not result:
            return {"message": "Planets not found"}, 404
        return result, 200

    def post(self):
        data = request.json
        try:
            discovered_date = parse_date(data.get('discovered_date'))
            call_procedure('add_planet', {
                'name': data['name'],
                'description': data['description'],
                'discovered_date': discovered_date
            })
            return {"message": "Planet added successfully"}, 201
        except Exception as e:
            return {"message": f"Error adding planet: {str(e)}"}, 400

    def put(self, id):
        data = request.json
        query = f"SELECT * FROM planets WHERE id = {id};"
        if not execute_query(query):
            return {"message": f"The planet with id {id} doesn't exist"}, 400

        try:
            discovered_date = parse_date(data.get('discovered_date'))
            call_procedure('update_planet', {
                'id': id,
                'name': data['name'],
                'description': data['description'],
                'discovered_date': discovered_date
            })
            return {"message": "Planet updated successfully"}, 200
        except Exception as e:
            return {"message": f"Error updating planet: {str(e)}"}, 400

    def delete(self, id):
        query = f"SELECT * FROM planets WHERE id = {id};"
        if not execute_query(query):
            return {"message": f"The planet with id {id} doesn't exist"}, 400

        try:
            call_procedure('delete_planet', {
                'id': id
            })
            return {"message": "Planet deleted successfully"}, 200
        except Exception as e:
            return {"message": f"Error deleting planet: {str(e)}"}, 400


class GovernmentResource(Resource):
    def get(self, id=None):
        if not id:
            query = f"SELECT * FROM governments;"
        else:
            query = f"SELECT * FROM governments WHERE id = {id};"
        result = execute_query(query)
        for government in result:
            government['established_date'] = government['established_date'].isoformat() if government['established_date'] else None
        if not result:
            return {"message": "Government not found"}, 404
        return result, 200

    def post(self):
        data = request.json
        try:
            established_date = parse_date(data.get('established_date'))
            call_procedure('add_government', {
                'planet_id': data['planet_id'],
                'type': data['type'],
                'leader': data['leader'],
                'established_date': established_date
            })
            return {"message": "Government added successfully"}, 201
        except Exception as e:
            return {"message": f"Error adding government: {str(e)}"}, 400

    def put(self, id):
        data = request.json
        query = f"SELECT * FROM governments WHERE id = {id};"
        if not execute_query(query):
            return {"message": f"The government with id {id} doesn't exist"}, 400

        try:
            established_date = parse_date(data.get('established_date'))
            call_procedure('update_government', {
                'id': id,
                'planet_id': data['planet_id'],
                'type': data['type'],
                'leader': data['leader'],
                'established_date': established_date
            })
            return {"message": "Government updated successfully"}, 200
        except Exception as e:
            return {"message": f"Error updating government: {str(e)}"}, 400

    def delete(self, id):
        query = f"SELECT * FROM governments WHERE id = {id};"
        if not execute_query(query):
            return {"message": f"The government with id {id} doesn't exist"}, 400

        try:
            call_procedure('delete_government', {
                'id': id
            })
            return {"message": "Government deleted successfully"}, 200
        except Exception as e:
            return {"message": f"Error deleting government: {str(e)}"}, 400


class StateResource(Resource):
    def get(self, id=None):
        if not id:
            query = f"SELECT * FROM states;"
        else:
            query = f"SELECT * FROM states WHERE id = {id};"
        result = execute_query(query)
        for state in result:
            state['area'] = float(state['area']) if state['area'] else None
        if not result:
            return {"message": "State not found"}, 404
        return result, 200

    def post(self):
        data = request.json
        try:
            area = float(data.get('area'))
            call_procedure('add_state', {
                'name': data['name'],
                'planet_id': data['planet_id'],
                'population': data['population'],
                'area': area
            })
            return {"message": "State added successfully"}, 201
        except Exception as e:
            return {"message": f"Error adding state: {str(e)}"}, 400

    def put(self, id):
        data = request.json
        query = f"SELECT * FROM states WHERE id = {id};"
        if not execute_query(query):
            return {"message": f"The state with id {id} doesn't exist"}, 400

        try:
            area = float(data.get('area'))
            call_procedure('update_state', {
                'id': id,
                'name': data['name'],
                'planet_id': data['planet_id'],
                'population': data['population'],
                'area': area
            })
            return {"message": "State updated successfully"}, 200
        except Exception as e:
            return {"message": f"Error updating state: {str(e)}"}, 400

    def delete(self, id):
        query = f"SELECT * FROM states WHERE id = {id};"
        if not execute_query(query):
            return {"message": f"The state with id {id} doesn't exist"}, 400

        try:
            call_procedure('delete_state', {
                'id': id
            })
            return {"message": "State deleted successfully"}, 200
        except Exception as e:
            return {"message": f"Error deleting state: {str(e)}"}, 400

class CityResource(Resource):
    def get(self, id=None):
        if not id:
            query = f"SELECT * FROM cities;"
        else:
            query = f"SELECT * FROM cities WHERE id = {id};"
        result = execute_query(query)
        for city in result:
            city['founded_date'] = city['founded_date'].isoformat() if city['founded_date'] else None
        if not result:
            return {"message": "City not found"}, 404
        return result, 200

    def post(self):
        data = request.json
        try:
            founded_date = parse_date(data.get('founded_date'))
            call_procedure('add_city', {
                'name': data['name'],
                'state_id': data['state_id'],
                'population': data['population'],
                'founded_date': founded_date
            })
            return {"message": "City added successfully"}, 201
        except Exception as e:
            return {"message": f"Error adding city: {str(e)}"}, 400

    def put(self, id):
        data = request.json
        query = f"SELECT * FROM cities WHERE id = {id};"
        if not execute_query(query):
            return {"message": f"The city with id {id} doesn't exist"}, 400

        try:
            founded_date = parse_date(data.get('founded_date'))
            call_procedure('update_city', {
                'id': id,
                'name': data['name'],
                'state_id': data['state_id'],
                'population': data['population'],
                'founded_date': founded_date
            })
            return {"message": "City updated successfully"}, 200
        except Exception as e:
            return {"message": f"Error updating city: {str(e)}"}, 400

    def delete(self, id):
        query = f"SELECT * FROM cities WHERE id = {id};"
        if not execute_query(query):
            return {"message": f"The city with id {id} doesn't exist"}, 400

        try:
            call_procedure('delete_city', {
                'id': id
            })
            return {"message": "City deleted successfully"}, 200
        except Exception as e:
            return {"message": f"Error deleting city: {str(e)}"}, 400
