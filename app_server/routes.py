import requests

from flask import Blueprint, render_template, url_for, request, redirect

from config import Config

main_bp = Blueprint('main_bp', __name__)
REST_SERVER_URL = f"http://{Config.REST_SERVER_HOST}:{Config.REST_SERVER_PORT}"


@main_bp.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@main_bp.route("/planets")
def planets():
    try:
        response = requests.get(f"{REST_SERVER_URL}/planets")
        response.raise_for_status()
        response_planets = response.json()
    except requests.RequestException:
        response_planets = []
    return render_template('/planets.html', title='Planet List', planets=response_planets)


@main_bp.route('/add_planet', methods=['GET'])
def add_planet_form():
    return render_template('add_planet.html', title='Add Planet')


@main_bp.route('/add_planet', methods=['POST'])
def add_planet():
    name = request.form['name']
    description = request.form['description']
    discovered_date = request.form['discovered_date']
    try:
        response = requests.post(f"{REST_SERVER_URL}/add_planet",
                                 json={
                                     'name': name,
                                     'description': description,
                                     'discovered_date': discovered_date
                                 })
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.planets'))


@main_bp.route('/update_planet/<int:id>', methods=['GET'])
def update_planet_form(id):
    try:
        response = requests.get(f"{REST_SERVER_URL}/planets/{id}")
        response.raise_for_status()
        response_planet = response.json()[0]
    except requests.RequestException:
        response_planet = None
    return render_template('update_planet.html', title='Update Planet', planet=response_planet)


@main_bp.route('/update_planet/<int:id>', methods=['POST'])
def update_planet(id):
    name = request.form['name']
    description = request.form['description']
    discovered_date = request.form['discovered_date']
    try:
        response = requests.put(f"{REST_SERVER_URL}/planets/{id}",
                                json={
                                    'id': id,
                                    'name': name,
                                    'description': description,
                                    'discovered_date': discovered_date
                                })
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.planets'))


@main_bp.route('/delete_planet', methods=['POST'])
def delete_planet():
    planet_id = request.form['id']
    try:
        response = requests.delete(f"{REST_SERVER_URL}/planets/{planet_id}")
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.planets'))


@main_bp.route("/governments")
def governments():
    try:
        response = requests.get(f"{REST_SERVER_URL}/governments")
        response.raise_for_status()
        response_governments = response.json()
    except requests.RequestException:
        response_governments = []
    return render_template('/governments.html', title='Government List', governments=response_governments)


@main_bp.route('/add_government', methods=['GET'])
def add_government_form():
    return render_template('add_government.html', title='Add Government')


@main_bp.route('/add_government', methods=['POST'])
def add_government():
    planet_id = request.form['planet_id']
    type = request.form['type']
    leader = request.form['leader']
    established_date = request.form['established_date']
    try:
        response = requests.post(f"{REST_SERVER_URL}/governments",
                                 json={
                                     'planet_id': planet_id,
                                     'type': type,
                                     'leader': leader,
                                     'established_date': established_date
                                 })
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.governments'))


@main_bp.route('/update_government/<int:id>', methods=['GET'])
def update_government_form(id):
    try:
        response = requests.get(f"{REST_SERVER_URL}/governments/{id}")
        response.raise_for_status()
        response_government = response.json()[0]
    except requests.RequestException:
        response_government = None
    return render_template('update_government.html', title='Update Government', government=response_government)


@main_bp.route('/update_government/<int:id>', methods=['POST'])
def update_government(id):
    planet_id = request.form['planet_id']
    type = request.form['type']
    leader = request.form['leader']
    established_date = request.form['established_date']
    try:
        response = requests.put(f"{REST_SERVER_URL}/governments/{id}",
                                json={
                                    'id': id,
                                    'planet_id': planet_id,
                                    'type': type,
                                    'leader': leader,
                                    'established_date': established_date
                                })
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.governments'))


@main_bp.route('/delete_government', methods=['POST'])
def delete_government():
    government_id = request.form['id']
    try:
        response = requests.delete(f"{REST_SERVER_URL}/governments/{government_id}")
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.governments'))


@main_bp.route("/states")
def states():
    try:
        response = requests.get(f"{REST_SERVER_URL}/states")
        response.raise_for_status()
        response_states = response.json()
    except requests.RequestException:
        response_states = []
    return render_template('/states.html', title='State List', states=response_states)


@main_bp.route('/add_state', methods=['GET'])
def add_state_form():
    return render_template('add_state.html', title='Add State')


@main_bp.route('/add_state', methods=['POST'])
def add_state():
    name = request.form['name']
    planet_id = request.form['planet_id']
    population = request.form['population']
    area = request.form['area']
    try:
        response = requests.post(f"{REST_SERVER_URL}/states",
                                 json={
                                     'name': name,
                                     'planet_id': planet_id,
                                     'population': population,
                                     'area': area
                                 })
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.states'))


@main_bp.route('/update_state/<int:id>', methods=['GET'])
def update_state_form(id):
    try:
        response = requests.get(f"{REST_SERVER_URL}/states/{id}")
        response.raise_for_status()
        response_state = response.json()[0]
    except requests.RequestException:
        response_state = None
    return render_template('update_state.html', title='Update State', state=response_state)


@main_bp.route('/update_state/<int:id>', methods=['POST'])
def update_state(id):
    name = request.form['name']
    planet_id = request.form['planet_id']
    population = request.form['population']
    area = request.form['area']
    try:
        response = requests.put(f"{REST_SERVER_URL}/states/{id}",
                                json={
                                    'id': id,
                                    'name': name,
                                    'planet_id': planet_id,
                                    'population': population,
                                    'area': area
                                })
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.states'))


@main_bp.route('/delete_state', methods=['POST'])
def delete_state():
    state_id = request.form['id']
    try:
        response = requests.delete(f"{REST_SERVER_URL}/states/{state_id}")
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.states'))


@main_bp.route("/cities")
def cities():
    try:
        response = requests.get(f"{REST_SERVER_URL}/cities")
        response.raise_for_status()
        response_cities = response.json()
    except requests.RequestException:
        response_cities = []
    return render_template('/cities.html', title='City List', cities=response_cities)


@main_bp.route('/add_city', methods=['GET'])
def add_city_form():
    return render_template('add_city.html', title='Add City')


@main_bp.route('/add_city', methods=['POST'])
def add_city():
    name = request.form['name']
    state_id = request.form['state_id']
    population = request.form['population']
    founded_date = request.form['founded_date']
    try:
        response = requests.post(f"{REST_SERVER_URL}/cities",
                                 json={
                                     'name': name,
                                     'state_id': state_id,
                                     'population': population,
                                     'founded_date': founded_date
                                 })
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.cities'))


@main_bp.route('/update_city/<int:id>', methods=['GET'])
def update_city_form(id):
    try:
        response = requests.get(f"{REST_SERVER_URL}/cities/{id}")
        response.raise_for_status()
        response_city = response.json()[0]
    except requests.RequestException:
        response_city = None
    return render_template('update_city.html', title='Update City', city=response_city)


@main_bp.route('/update_city/<int:id>', methods=['POST'])
def update_city(id):
    name = request.form['name']
    state_id = request.form['state_id']
    population = request.form['population']
    founded_date = request.form['founded_date']
    try:
        response = requests.put(f"{REST_SERVER_URL}/cities/{id}",
                                json={
                                    'id': id,
                                    'name': name,
                                    'state_id': state_id,
                                    'population': population,
                                    'founded_date': founded_date,
                                })
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.cities'))


@main_bp.route('/delete_city', methods=['POST'])
def delete_city():
    city_id = request.form['id']
    try:
        response = requests.delete(f"{REST_SERVER_URL}/cities/{city_id}")
        response.raise_for_status()
    except requests.RequestException:
        pass
    return redirect(url_for('main_bp.cities'))
