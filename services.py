import requests

def get_user_repos(username):
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    if(response.status_code == 404):
        raise UserNotFoundException()

    repos_info = response.json()
    repos = []
    for repo_info in repos_info:
        repos.append({'name': repo_info['name'], 'stars': repo_info['stargazers_count']})

    return repos

def get_sum_of_stars_for_user_repos(username):
    repos = get_user_repos(username)
    return sum([repo['stars'] for repo in repos])

class UserNotFoundException(Exception):
    pass