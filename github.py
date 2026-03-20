import os
import requests

class GitHubAPI:
    TOKEN = os.getenv("TOKEN")
    USER_NAME = os.getenv("USER_NAME")

    @staticmethod
    def get_github_repos():
        headers = {"Authorization": f"token {GitHubAPI.TOKEN}"}

        repos = []
        page = 1
        while True:
            url = f"https://api.github.com/user/repos?per_page=100&page={page}"
            r = requests.get(url, headers=headers)
            r.raise_for_status() 
            data = r.json()
            if not data:
                break
                
            for repo in data:
                    if repo["owner"]["login"] == GitHubAPI.USER_NAME:
                        repos.append(repo)
            page += 1

            print("Repositories")
            for repo in repos:
                print(repo["name"])
            print()
        return repos
    