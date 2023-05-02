#!/usr/bin/python3
"""Index module"""
from api.v1.views import app_views
from flask import jsonify, request

@app_views.route('/status', methods=['GET'])
def status():
    """Stauts route"""
    if request.method == "GET":
        return jsonify({"status": "OK"})
