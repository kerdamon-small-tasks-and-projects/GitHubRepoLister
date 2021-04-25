# GitHubRepoLister
Simple api for listing GitHub repos for given user written in Python using Flask framework.
This api is hosted on heroku - 

## Endpoints
Currently there are two endpoints.

`api/repos/<username>` - lists all public repositories for given username

`api/stars_sum/<username>` - returns sum of stars for all repos for given username

## How to launch app localy
cd into folder with app.py. Then install requirements by enering following command: `pip install -r requirements.txt`. After everything have been installed, enter `flask run` to launch server.
