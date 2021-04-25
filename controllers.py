from flask import Blueprint, jsonify
from services import get_user_repos, get_sum_of_stars_for_user_repos, UserNotFoundException

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/repos/<username>')
def list_user_repos(username):
    try:
        return jsonify(get_user_repos(username))
    except UserNotFoundException:
        return {"message": 'Not Found'}, 404

@api.route('/stars_sum/<username>')
def list_sum_of_stars_for_user_repos(username):
    try:
        return {'sum': get_sum_of_stars_for_user_repos(username)}
    except UserNotFoundException:
        return {"message": 'Not Found'}, 404