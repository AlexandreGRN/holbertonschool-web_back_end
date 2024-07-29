#!/usr/bin/env python3
"""
Flask APP
"""
from flask import Flask, jsonify, abort, request, redirect
from flask_cors import (CORS, cross_origin)
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def get_request() -> str:
    """ get request """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
