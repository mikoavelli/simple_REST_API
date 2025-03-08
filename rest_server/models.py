from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text)
    discovered_date = db.Column(db.Date)

    government = db.relationship('Government', back_populates='planet', uselist=False, cascade='all, delete-orphan')
    states = db.relationship('State', back_populates='planet', cascade='all, delete-orphan')

    def repr(self):
        return f"<Planet {self.name}>"

class Government(db.Model):
    __tablename__ = 'governments'
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    leader = db.Column(db.String(100))
    established_date = db.Column(db.Date)

    planet = db.relationship('Planet', back_populates='government')

    def repr(self):
        return f"<Government {self.type} on Planet {self.planet_id}>"

class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    population = db.Column(db.Integer)
    area = db.Column(db.Float)

    planet = db.relationship('Planet', back_populates='states')
    cities = db.relationship('City', back_populates='state', cascade='all, delete-orphan')

    def repr(self):
        return f"<State {self.name} on Planet {self.planet_id}>"

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    population = db.Column(db.Integer)
    founded_date = db.Column(db.Date)

    state = db.relationship('State', back_populates='cities')

    def repr(self):
        return f"<City {self.name} in State {self.state_id}>"