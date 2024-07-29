from flask import Flask
from models.user import User
from database import db


app = Flask(__name__)
app.config['SECURIT_KEY'] = "my_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route("/initial", methods=(['GET']))
def initial():
    return "Initial OK"

if __name__ == '__main__':
    app.run(debug=True)