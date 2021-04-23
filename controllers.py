from flask import Blueprint, request, jsonify
import requests

rep = Blueprint('api', __name__, url_prefix='/api')

@rep.route('/repos/<username>')
def list_user_repos(username):
    repos_info = requests.get(f'https://api.github.com/users/{username}/repos').json()
    repos = {}
    for repo_info in repos_info:
        repos[repo_info['name']] = repo_info['stargazers_count']

    return repos

@rep.route('/starSum/<username>')
def list_sum_of_stars_for_user_repos(username):
    repos = list_user_repos(username)
    return {'sum': sum(repos.values())}