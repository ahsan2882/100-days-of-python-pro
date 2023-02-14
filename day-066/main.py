import os
from pathlib import Path
from random import choice
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request

DB_PATH = Path(
    Path(__file__).parent.resolve(), 'cafes.db'
).resolve()
DOTENV_PATH = Path(
    Path(__file__).parent.resolve(), '.env'
).resolve()
load_dotenv(DOTENV_PATH)

API_KEY = os.getenv('API_KEY')
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random():
    random_cafe = choice(db.session.query(Cafe).all())
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=["GET"])
def get_all():
    all_cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=["GET"])
def search():
    location = request.args.get("loc")
    cafes = db.session.query(Cafe).filter_by(location=location).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })
# HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add_cafe():
    errors = {}
    num_of_errors = 0
    new_cafe = request.get_json()
    if new_cafe.get("can_take_calls") is None:
        new_cafe["can_take_calls"] = False
    if new_cafe.get("has_sockets") is None:
        new_cafe["has_sockets"] = False
    if new_cafe.get("has_toilet") is None:
        new_cafe["has_toilet"] = False
    if new_cafe.get("has_wifi") is None:
        new_cafe["has_wifi"] = False
    if new_cafe.get("coffee_price") is None:
        errors["coffee_price"] = "Coffee price is required."
        num_of_errors += 1
    else:
        new_cafe["coffee_price"] = f"£{new_cafe['coffee_price']}"
    if new_cafe.get("location") is None:
        errors["location"] = "Location is required."
        num_of_errors += 1
    if new_cafe.get("img_url") is None:
        errors["img_url"] = "Image URL is required."
        num_of_errors += 1
    if new_cafe.get("map_url") is None:
        errors["map_url"] = "Map URL is required."
        num_of_errors += 1
    if new_cafe.get("name") is None:
        errors["name"] = "Name is required."
        num_of_errors += 1
    if new_cafe.get("seats") is None:
        errors["seats"] = "Number of Seats is required."
        num_of_errors += 1
    if new_cafe.get("id") is None:
        prev_id = db.session.query(Cafe).order_by(Cafe.id.desc()).first().id
        new_id = prev_id + 1
        new_cafe["id"] = new_id
    if num_of_errors > 0:
        return jsonify(response={"details": f"{num_of_errors} properties missing.", "errors": errors})
    else:
        cafe = Cafe(**new_cafe)
        db.session.add(cafe)
        db.session.commit()
        return jsonify(response={
            "success": "Successfully added the new cafe.",
            "cafe": new_cafe
        })


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    if new_price is None:
        return jsonify(error={
            "Missing Parameter": "Please provide a new price."
        })
    coffee_store = Cafe.query.get(cafe_id)
    if not coffee_store:
        return jsonify(error={
            "Not Found": "Sorry a cafe with that id was not found in the database."
        })
    coffee_store.coffee_price = f"£{new_price}"
    db.session.commit()
    return jsonify(response={
        "success": "Successfully updated the price.",
        "store": coffee_store.to_dict()
    })

# HTTP DELETE - Delete Record


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key != API_KEY:
        return jsonify(error={
            "Forbidden": "You are not authorized to perform this action. Make sure you have the correct API key."
        })
    coffee_store = Cafe.query.get(cafe_id)
    if not coffee_store:
        return jsonify(error={
            "Not Found": "Sorry a cafe with that id was not found in the database."
        })
    db.session.delete(coffee_store)
    db.session.commit()
    return jsonify(response={
        "success": "Successfully deleted the cafe.",
    })


if __name__ == '__main__':
    app.run(debug=True)
