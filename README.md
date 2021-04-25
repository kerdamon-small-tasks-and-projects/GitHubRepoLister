# GitHubRepoLister
Simple api for listing GitHub repos for given user written in Python using Flask framework.
This api is hosted on heroku - https://git-hub-repo-lister.herokuapp.com/

## Endpoints
Currently there are two endpoints.

`api/repos/<username>` - lists all public repositories for given username
Example: https://git-hub-repo-lister.herokuapp.com/api/repos/kerdamon

`api/stars_sum/<username>` - returns sum of stars for all repos for given username
Example: https://git-hub-repo-lister.herokuapp.com/api/stars_sum/kerdamon

## How to launch app localy
cd into folder with app.py. Then install requirements by enering following command: `pip install -r requirements.txt`. After everything have been installed, enter `flask run` to launch server.

## Ideas for future development
- listing all repositories for given username from organizations that only this user is member of (because some people are using organizations as "folders" for grouping repositories)
