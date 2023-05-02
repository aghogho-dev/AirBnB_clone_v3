#!/usr/bin/python3
"""Create Flask API"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask import render_template, url_for
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
port = int(os.environ.get('HBNB_API_PORT', '5000'))

@app.teardown_appcontext
def teardown_storage_db():
    """Call .close() method"""
    storage.close()

if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
