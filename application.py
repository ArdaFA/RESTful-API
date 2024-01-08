from flask import Flask, request
app = Flask(__name__) # creating an instance of a Flask application
from flask_sqlalchemy import SQLAlchemy


#we also need to configure our database so we can connect to it 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# create an instance od database
db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10),unique=False, nullable = False )
    model = db.Column(db.String(20))

    #representation
    def __repr__(self): #special method in python to define in our classes.
        # purpose of this method is to return a string representation of an object
        return f"{self.name} - {self.model}"

@app.route('/')
def mainRoute():
    return {"Main Route KEY ": "Main Route VALUE"}

@app.route('/cars')
def get_cars():
    cars = Car.query.all()
    # we can not directly but the cars inside the return block
    # cuz the Object Type of Car is NOT JSON serializable

    output = []
    for car in cars:
        car_data = {'name': car.name, 'model':car.model}
        output.append(car_data)
    return {"cars": output}

@app.route('/cars/<id>')
def get_car(id):
    car = Car.query.get_or_404(id)
    return {"name": car.name, "model":car.model}

@app.route('/cars', methods=['POST'])
def add_car():
    car = Car(name=request.json['name'], model=request.json['model'])
    db.session.add(car)
    db.session.commit()
    return {'message': 'Successfully added ' + str(car.id)}

@app.route('/cars/<id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get_or_404(id)
    db.session.delete(car)
    db.session.commit()
    return {"message": "deleted!"}

@app.route('/cars/<id>', methods=['PUT'])
def update_car(id):
    car = Car.query.get_or_404(id)
    
    # Check if 'name' or 'model' exist in the request's JSON body and update accordingly.
    if 'name' in request.json:
        car.name = request.json['name']
    if 'model' in request.json:
        car.model = request.json['model']
    
    db.session.commit()
    return {"message": f"Updated car with id {car.id}!"}


