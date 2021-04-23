from flask import Blueprint, request, jsonify
from services import get_user_repos, get_sum_of_stars_for_user_repos


rep = Blueprint('api', __name__, url_prefix='/api')

@rep.route('/repos/<username>')
def list_user_repos(username):
    return get_user_repos(username)

@rep.route('/starSum/<username>')
def list_sum_of_stars_for_user_repos(username):
    return {'sum': get_sum_of_stars_for_user_repos(username)}