from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECURIT_KEY'] = "my_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

@app.route("/initial", methods=(['GET']))
def initial():
    return "Initial OK"

if __name__ == '__main__':
    app.run(debug=True)