from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:admin123@127.0.0.1:3306/flask-crud"
login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

#login view
login_manager.login_view = 'login'

@login_manager.user_loader 
def load_user(user_id):
    return User.query.get(user_id)

#Login route
@app.route('/login', methods=["POST"])
def login():

    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            return jsonify({"message": "Authentication successful"})

    return jsonify ({"message": "Invalid Credentials"}), 400


#Logout route
@app.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()    
    return jsonify({"message": "Logout successful"})    

@app.route("/", methods=["GET"])
def teste():
    return "Hello"


@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    
    hashed = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


    if username and password and email:

        user = User(username= username, password=hashed, email=email, role='user')    
        db.session.add(user)
        db.session.commit()

        return jsonify({"message": "Successful"})

    return jsonify({"message": "Invalid args"}), 400


@app.route("/user/<int:id_user>", methods=["GET"])
@login_required
def read_user(id_user):

    user = User.query.get(id_user)

    if user:
        return {"username": user.username}
    
    return jsonify({"message": "User not found"}), 404


@app.route("/user/<int:id_user>", methods=["PUT"])
@login_required
def update_user(id_user):

    data = request.json
    user = User.query.get(id_user)

    

    if user and data.get("password"):

        user.password = data.get("password")
        db.session.commit()

        return jsonify({"message": f"User {id_user} updated!"})
    
    return jsonify({"message": "User not found"}), 404


@app.route("/user/<int:id_user>", methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if user is None:
        return jsonify({"message": "User not found"}), 404

    if id_user == current_user.id:
        return jsonify({
            "message": "You cannot delete your own user"
        }), 403

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "message": f"User {id_user} deleted!"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)