#!/usr/bin/python3
"""
Default flask app. Registers the app_views blueprint.
Defines the teardown_appcontext which closes the database.
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown():
    storage.close()

if __name == "__main__":
    if getenv("HBNB_API_HOST") != None or getenv("HBNB_API_HOST") != "":
        app.config['HBNB_API_HOST'] = '0.0.0.0'
    if getenv("HBNB_API_PORT") != None or getenv("HBNB_API_PORT") != "":        
        app.config['HBNB_API_PORT'] = "5000"
    app.run(threaded=True)
