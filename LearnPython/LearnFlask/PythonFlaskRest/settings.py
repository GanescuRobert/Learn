from flask import Flask
import os
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Learn/LearnFlask/PythonFlaskRest/database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
