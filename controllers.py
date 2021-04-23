from flask import Blueprint, jsonify
from services import get_user_repos, get_sum_of_stars_for_user_repos

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/repos/<username>')
def list_user_repos(username):
    return jsonify(get_user_repos(username))

@api.route('/starSum/<username>')
def list_sum_of_stars_for_user_repos(username):
    return {'sum': get_sum_of_stars_for_user_repos(username)}