from flask import Blueprint, request, jsonify
import requests

rep = Blueprint('repos', __name__, url_prefix='/api/repos')

@rep.route('/<username>')
def hello(username):
    return jsonify(requests.get(f'https://api.github.com/users/{username}/repos').json())
